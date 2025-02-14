import os
import grants
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = grants.LANGCHAIN_API_KEY
from MiniLLMPDF import createPDFMiniLM
from Mistral7BPDF import chat_with_pdf


prompt="Chat BB - welcome -> "
#with llm="all-MiniLM-L6-v2"
#createPDFMiniLM(query)

persist_directory = "./db/eng_db"
chat_with_pdf(prompt, persist_directory)
print("=========done============")




