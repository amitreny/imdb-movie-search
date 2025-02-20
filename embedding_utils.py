import pandas as pd
from sentence_transformers import SentenceTransformer
from pinecone_setup import get_pinecone_index

# Load Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Get Pinecone index
index = get_pinecone_index()

def generate_embedding(text):
    """Generate embeddings using Sentence Transformer"""
    return model.encode(text).tolist()

def upload_embeddings(csv_path="data\IMDB top 1000.csv"):
    """Load dataset, create embeddings, and upload to Pinecone"""
    df = pd.read_csv(csv_path)
    df = df[["Title", "Description"]].dropna()

    for i, row in df.iterrows():
        movie_text = f"{row['Title']}: {row['Description']}"
        embedding = generate_embedding(movie_text)
        index.upsert([(str(i), embedding, {"title": row['Title'], "description": row['Description']})])

    print("✅ Embeddings uploaded successfully.")

def search_similar_movies(query, top_k=5):
    """Search for similar movies in Pinecone, ensuring unique results"""
    query_embedding = generate_embedding(query)

    # Query Pinecone
    results = index.query(vector=query_embedding, top_k=top_k * 2, include_metadata=True)  # Request more results to filter duplicates
    
    unique_movies = {}
    
    for res in results["matches"]:
        title = res["metadata"]["title"]
        if title not in unique_movies:
            unique_movies[title] = res["metadata"]["description"]
        if len(unique_movies) == top_k:
            break  # Stop when we reach the desired unique results

    return list(unique_movies.items())  # Return unique (title, description) pairs


