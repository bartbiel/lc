from dotenv import load_dotenv
import os
load_dotenv()

# Access the API key
LANGCHAIN_API_KEY = os.getenv("API_LC")
DEEPSEEK_API_KEY=os.getenv("API_DS")
OPENAI_API_KEY=os.getenv("API_01")
OPENAI_API_KEYb=os.getenv("API_01b")

#Access source folder
PDF_PATH=os.getenv("PDF_PATH")


