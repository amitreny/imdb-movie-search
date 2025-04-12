import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "imdb-movies")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-east-1-gcp")

pc = Pinecone(api_key=PINECONE_API_KEY)

# Check if index exists; if not, create it
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=384,  # MiniLM-L6-v2 produces 384-dimensional vectors
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Connect to the index
index = pc.Index(PINECONE_INDEX_NAME)

def get_pinecone_index():
    """Return the initialized Pinecone index"""
    return index
