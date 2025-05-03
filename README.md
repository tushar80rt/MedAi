
# 🏥 MedAI Pro – AI-Powered Medical Report Analyzer

**MedAI Pro** is an AI-driven web application that allows users to upload medical reports in PDF format, ask health-related questions, and receive responses from a virtual medical expert powered by LLaMA 4 and CAMEL AI.

---

## 🎥 Demo Screenshots

Here are some key UI snapshots of the application in action:

![Screenshot 1](screenshot_1.png) ![screenshot_1](https://github.com/user-attachments/assets/165b443f-0683-45ff-a675-26ab9d904f5d)

![Screenshot 2](screenshot_2.png)   ![screenshot_2](https://github.com/user-attachments/assets/6e9745a6-efd4-4fae-ba38-00d8501c3443)

![Screenshot 3](screenshot_3.png)    ![screenshot_3](https://github.com/user-attachments/assets/ea71355f-4af0-43fe-b909-76064076fb4f)


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

1. **Clone this repository**

camel-ai[all]    
PyMuPDF==1.23.9         
python-dotenv==1.0.1        
streamlit
gTTS==2.5.1  

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

