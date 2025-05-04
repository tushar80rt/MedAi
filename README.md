
# 🏥 MedAI Pro – AI-Powered Medical Report Analyzer

🩺 Imagine this...
You're a doctor, student, or just someone trying to understand a lab report.
You open a 50-page PDF filled with blood work, medical terms, and charts.

You have one question:

“Is the patient’s WBC count normal?”

But you're stuck scanning through paragraphs.

"Imagine asking a question and receiving the answer in just seconds—delivered seamlessly in both text and audio formats. Instant, accurate, and fully interactive!"

🔥 Meet Med-AI
Med-AI is a blazing-fast PDF Q&A assistant for medical documents.

Built with:

💬 LLaMA 4 (Meta’s powerful open LLM)

⚡ Groq API (ultra-low latency inference)

🧠 Camel AI agents (smart prompting strategy)

🖥 Streamlit UI (sleek chat + PDF preview)

Whether you're analyzing reports or learning medicine — Med-AI gives you answers, not headaches.

---

## 🎥 Demo Screenshots

Here are some key UI snapshots of the application in action:

![Screenshot 1](screenshot_1.png) <img width="845" alt="topview" src="https://github.com/user-attachments/assets/d070eaa0-e999-43af-82d9-70f3435dd391" />

![Screenshot 2](screenshot_2.png)   <img width="846" alt="secondview" src="https://github.com/user-attachments/assets/5f27ae1f-4d1f-4080-9145-17cda831ce52" />

![Screenshot 3](screenshot_3.png)   <img width="842" alt="thirdview" src="https://github.com/user-attachments/assets/ed5ac83f-c511-4281-ab92-a2af6ec15795" />



---

## 🚀 Features

- 🧾 Upload and analyze medical reports (PDF)
- 🤖 AI-powered answers using LLaMA 4 + Groq API
- 🧠 CAMEL AI framework for role-based agent simulation
- 🎙 Converts response text into audio (Text-to-Speech)
- ⚡ Fast and interactive Streamlit-based UI

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **AI Agent:** CAMEL AI
- **LLM Backend:** LLaMA 4 via Groq API
- **PDF Processing:** PyMuPDF
- **Env Management:** python-dotenv

---

## 📦 Installation

camel-ai[all]  

PyMuPDF==1.23.9   

python-dotenv==1.0.1 

streamlit

gTTS==2.5.1 

groq

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your Groq API key**

Create a `.env` file or edit `api.env`:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

4. **Run the application**

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. User uploads a medical PDF report.
2. App extracts report content using PyMuPDF.
3. Initializes a CAMEL AI agent with "Doctor" role.
4. User enters a question; LLaMA 4 (via Groq) generates an answer.
5. Answer is shown on screen and converted to audio.

---

## 📄 License & Author

Developed by **Tushar Singh**  
🔗 *For educational and demo purposes only.*

---

