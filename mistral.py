from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Assuming you have these imports and the required classes/functions defined elsewhere
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from splitter import documentSplitter  # Assuming this function is defined elsewhere
from fastapi.middleware.cors import CORSMiddleware
import os
persistDir=os.getenv("PDF_PERSIST")

app = FastAPI()

def cors():
    origins = [
        "http://localhost:3000",  # React development server
    ]

    # Add CORS middleware to the app
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # Specify which origins are allowed
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allow all headers
    )    
cors()

# Define the request body schema for validation
class QueryRequest(BaseModel):
    query: str
    persist_directory: Optional[str] = persistDir  

# Initialize the vector database and retriever once, not every time a request is made
def initialize_vector_db(persist_directory: str):
    split_docs = documentSplitter()  # Assuming this splits your document into chunks
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    vector_db = Chroma.from_documents(split_docs, embedding=embedding_model, persist_directory=persist_directory)
    vector_db.persist()  # Persisting the database
    retriever = vector_db.as_retriever()
    return retriever

# Make sure to define or load your language model `llm` here
llm = Ollama(model="mistral:7b-instruct")

# Load and initialize the vector database once on app startup
retriever = initialize_vector_db(persistDir)

@app.post("/mistralchat/")
def chat_with_pdf(request: QueryRequest):
    # Using the request body query value
    query = request.query
    persist_directory = request.persist_directory
    
    # Initialize the QA chain with the retriever and the LLM
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    
    # Get the response based on the user's query
    response = qa_chain.invoke(query)  # This will retrieve and answer the question
    
    return {"query": query, "result": response}
