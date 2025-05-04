
# 🏥 MedAI Pro – AI-Powered Medical Report Analyzer

**MedAI Pro** is an AI-driven web application that allows users to upload medical reports in PDF format, ask health-related questions, and receive responses from a virtual medical expert powered by LLaMA 4 and CAMEL AI.

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

