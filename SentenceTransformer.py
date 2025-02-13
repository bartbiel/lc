from sentence_transformers import SentenceTransformer
from splitter import documentSplitter
import chromadb


def GenerateEmbeddings(embedding_model):

    # Extract raw text from the split chunks
    split_text=documentSplitter()
    split_text_content = [chunk.page_content for chunk in split_text]

    # Generate embeddings for each chunk
    embeddings = embedding_model.encode(split_text_content)

    # Print shape (num_chunks, embedding_dim)
    print(f"embeddings shape= {embeddings.shape}")
    return embeddings, split_text_content

def StoreEmbeddingsinChroma(embeddings, split_text_content):
     
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path="bo2_db")

    # Create a collection
    collection = client.get_or_create_collection("ai_documents")

    # Add text chunks and embeddings to ChromaDB
    for i, (text, embedding) in enumerate(zip(split_text_content, embeddings)):
        collection.add(ids=[str(i)], documents=[text], embeddings=[embedding.tolist()])
    return collection

def Indexing(query_text):
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings, split_text_content= GenerateEmbeddings(embedding_model)
    collection = StoreEmbeddingsinChroma(embeddings, split_text_content)
    

    # Convert the query into an embedding
    query_embedding = embedding_model.encode([query_text])[0]

    # Search for the top 2 most relevant results
    results = collection.query(query_embeddings=[query_embedding.tolist()], n_results=2)

    # Print the results
    #print(results["documents"])
    return results






