import grants
import os
from pdfchecker import listOfValidatedPDFs
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = grants.LANGCHAIN_API_KEY

def documentSplitter():
    pdf_list=listOfValidatedPDFs(grants.PDF_PATH)
    docs=[]
    for pdf in pdf_list:
        try:
            loader=PyMuPDFLoader(pdf)
            docs.extend(loader.load())
            print(f"successfuly loaded {pdf}")
        except Exception as e:
            print(f"error during loading for {pdf}")
            print({e})
    print(f"\n Total pages loaded: {len(docs)}")

    # Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits




    


