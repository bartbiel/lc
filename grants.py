from dotenv import load_dotenv
import os
load_dotenv()

# Access the API key
LANGCHAIN_API_KEY = os.getenv("API_LC")


#Access source folder
PDF_PATH=os.getenv("PDF_PATH")
PDF_PERSIST=os.getenv("PDF_PERSIST")



