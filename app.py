import os
import uuid
import tempfile
import threading
import re

import streamlit as st
from dotenv import load_dotenv
from gtts import gTTS
from pdf2image import convert_from_bytes

from camel_agents import MedicalReportAssistant

# ---------------------------
# 1. Load environment
# ---------------------------
load_dotenv("api.env")

# ---------------------------
# 2. Session state init
# ---------------------------
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "file_bytes" not in st.session_state:
    st.session_state.file_bytes = None

def clear_file():
    """Reset stored file in session state."""
    st.session_state.uploaded_file = None
    st.session_state.file_bytes = None

st.session_state.clear_file = clear_file

# ---------------------------
# 3. Page configuration
# ---------------------------
st.set_page_config(
    page_title="MedAI Pro ⚡",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# 4. Custom CSS & Header
# ---------------------------
st.markdown("""
<style>
  /* App background & text styling */
  [data-testid=stAppViewContainer] {
      background-color: #121212;
  }
  .stTextArea textarea {
      color: white !important;
  }

  /* Header styles */
  .header-container {
      text-align: center;
      margin: 2rem 0;
  }
  .header-container .title {
      font-size: 2.8rem;
      font-weight: 700;
      color: #ffffff;
      vertical-align: middle;
      margin: 0 1rem;
  }
  .header-container img {
      vertical-align: middle;
      margin: 0 1rem;
  }

  /* Result box styling */
  .result-box {
      background: #1e1e1e;
      padding: 1rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
  }
  .result-box h1, .result-box h2, .result-box h3, .result-box h4 {
      color: #ffffff;
  }
  .result-box p, .result-box ul, .result-box ol, .result-box li {
      color: #e0e0e0;
  }

  /* Audio container styling */
  .audio-container {
      background: #2d2d2d;
      padding: 20px;
      border-radius: 10px;
      margin-top: 30px;
      text-align: center;
      box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  }
  .audio-container h4 {
      color: #4fc3f7;
      margin-bottom: 15px;
      font-size: 1.3em;
  }
  .audio-container audio {
      width: 100%;
      border-radius: 10px;
      border: 1px solid #4fc3f7;
  }
  .audio-btn {
      background-color: #4fc3f7;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      font-size: 1.2em;
      cursor: pointer;
      margin-top: 10px;
  }
  .audio-btn:hover {
      background-color: #1976d2;
  }
</style>

<div class="header-container">
    <span class="title">⚡ MedAI Pro</span>
</div>
<div class="header-container">
    <img src="https://repository-images.githubusercontent.com/615510678/93880a8f-edb6-4ef2-88d1-abff2651702e" width="120" alt="Camel AI"/>
    <img src="https://www.ciscoinvestments.com/assets/logos/groq-logo.png" width="120" alt="Together"/>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# 5. Theme helper
# ---------------------------
def set_theme():
    """Additional theme settings (if needed)."""
    # Placeholder for any Python-based theme logic
    pass

set_theme()

# ---------------------------
# 6. Sidebar: File upload
# ---------------------------
with st.sidebar:
    st.subheader("📁 Upload Medical Report")
    uploaded = st.file_uploader(
        label="", type=["pdf"], label_visibility="collapsed"
    )

    if uploaded:
        # Store file bytes in session
        st.session_state.uploaded_file = uploaded
        st.session_state.file_bytes = uploaded.getbuffer()

        # Button to clear upload
        st.button("🗑️ Clear Uploaded File", on_click=st.session_state.clear_file)

        # PDF preview expander
        with st.expander("📄 Preview Report Pages", expanded=False):
            try:
                images = convert_from_bytes(
                    st.session_state.file_bytes, size=(300, None)
                )
                for i, img in enumerate(images, start=1):
                    st.image(img, caption=f"Page {i}", use_container_width=True)
                st.success(f"✅ Showing all {len(images)} pages.")
            except Exception as e:
                st.error(f"Could not preview PDF: {e}")

# ---------------------------
# 7. Utility functions
# ---------------------------
def clean_text(text: str) -> str:
    """Remove non-alphanumeric characters for TTS."""
    return re.sub(r"[^\w\s]", "", text)

def generate_audio(text: str) -> str:
    """
    Generate an MP3 from cleaned text via gTTS.
    Returns the path to the audio file.
    """
    cleaned = clean_text(text)
    audio_path = "temp_result_audio.mp3"
    tts = gTTS(text=cleaned, lang="en")
    tts.save(audio_path)
    return audio_path

def get_assistant() -> MedicalReportAssistant:
    """Instantiate and return the medical report assistant."""
    return MedicalReportAssistant()

# ---------------------------
# 8. Main interface: Tabs
# ---------------------------
tab1, tab2 = st.tabs(["Analyze Report", "ℹ️ About"])

with tab1:
    # User query input
    query = st.text_area(
        "Enter your query (or leave blank to auto-analyze):",
        height=120,
        placeholder="e.g. Explain my blood test results"
    )

    if st.button("🚀 Start Analysis", type="primary", use_container_width=True):
        if not st.session_state.uploaded_file:
            st.error("❌ Please upload a PDF medical report first.")
        else:
            with st.spinner("🧠 Analyzing report with AI..."):
                try:
                    # Write temp PDF file
                    temp_pdf = f"temp_{uuid.uuid4().hex}.pdf"
                    with open(temp_pdf, "wb") as f:
                        f.write(st.session_state.file_bytes)

                    # Analyze via assistant
                    assistant = get_assistant()
                    prompt = query.strip() or (
                        "Please analyze this medical report and explain "
                        "the findings in simple terms."
                    )
                    result = assistant.analyze_query(prompt, temp_pdf)

                    # Generate and display audio
                    audio_path = generate_audio(result)
                    st.markdown('<div class="audio-container">', unsafe_allow_html=True)
                    st.markdown(
                        '<h4>🔊 Listen to Doctor\'s AI Opinion:</h4>',
                        unsafe_allow_html=True
                    )
                    st.audio(audio_path)
                    st.markdown('</div>', unsafe_allow_html=True)

                    # Display text result
                    st.markdown("### 🩺 Doctor’s AI Opinion")
                    st.markdown(
                        f'<div class="result-box">{result}</div>',
                        unsafe_allow_html=True
                    )
                    st.success("✅ Analysis completed successfully!")

                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
                    st.error("Please try again with a different PDF file")
                finally:
                    # Clean up temp file
                    if os.path.exists(temp_pdf):
                        os.remove(temp_pdf)

with tab2:
    # About section
    st.markdown("""
    ## About MedAI Pro

    MedAI Pro leverages advanced AI to transform complex medical reports 
    into clear, actionable insights in seconds.

    **Key Capabilities**
    - Comprehensive PDF report interpretation
    - Natural language explanations
    - Integrated audio playback for auditory learners
    - Privacy-first design—no data is stored

    **How It Works**
    1. **Upload** your medical report (PDF)
    2. **Query** specific points or run a full analysis
    3. **Review** both text and audio summaries

    Built on the [CAMEL-AI](https://www.camel-ai.org/) framework & 
    [Groq Inference](https://groq.com/) and powered by secure, on-device 
    processing to ensure patient confidentiality.
    """)

# ---------------------------
# 9. Footer
# ---------------------------
st.markdown("---")
st.caption("© 2025 MedAI Pro | For educational and research use only")
