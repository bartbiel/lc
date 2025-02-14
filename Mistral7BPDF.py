from splitter import documentSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




# Set up Mistral 7B with LangChain
llm = Ollama(model="mistral:7b-instruct")

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

@app.post("/chat/")
def chat_with_pdf(query, persist_directory):
    split_docs = documentSplitter()
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    vector_db = Chroma.from_documents(split_docs, embedding=embedding_model, persist_directory=persist_directory)
    vector_db.persist()

    retriever = vector_db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

    split_docs = documentSplitter()
    
    while True:
        discussion = input(query)

        if discussion.lower() in ["exit", "quit"]:
            break
        response = qa_chain.invoke(discussion)
        return {"response": response}








