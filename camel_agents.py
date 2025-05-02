import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from camel.agents import ChatAgent
from camel.types import RoleType
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

class MedicalReportAssistant:
    def __init__(self):
        load_dotenv("api.env")
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("❌ GROQ_API_KEY missing in api.env")

        # Model for LLAMA 3, but no need to pass api_key here
        self.model = ModelFactory.create(
            model_platform=ModelPlatformType.GROQ,
            model_type="llama-3.1-8b-instant"  # LLAMA 3 model
        )

    def extract_text(self, pdf_input):
        try:
            if isinstance(pdf_input, bytes):
                doc = fitz.open(stream=pdf_input, filetype="pdf")
            else:
                doc = fitz.open(pdf_input)
            return "\n".join(page.get_text() for page in doc)
        except Exception as e:
            return f"⚠️ PDF Error: {str(e)}"

    def analyze_query(self, query, pdf_input=None):
        try:
            # Initialize ChatAgent for Doctor role
            doctor = ChatAgent(
                system_message=BaseMessage(
                    role_name="Doctor",
                    role_type=RoleType.ASSISTANT,
                    content="""You are a medical expert. Analyze reports and provide:
1. Key findings
2. Potential concerns
3. Recommendations""",
                    meta_dict={}  # Add additional meta information if needed
                ),
                model=self.model
            )

            input_content = f"Patient Query: {query}\n\n"
            if pdf_input:
                report_text = self.extract_text(pdf_input)
                input_content += f"Report Contents:\n{report_text[:5000]}"

            # Send query and report to Doctor agent
            response = doctor.step(BaseMessage(
                role_name="Patient",
                role_type=RoleType.USER,
                content=input_content,
                meta_dict={}  # Optional metadata
            ))

            return response.msg.content

        except Exception as e:
            return f"⚠️ Processing Error: {str(e)}"
