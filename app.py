import streamlit as st
from embedding_utils import upload_embeddings, search_similar_movies

st.title("🎬 IMDb Movie Search with Pinecone & Sentence Transformers")

option = st.sidebar.selectbox("Choose an option", ["Upload Data", "Search Movies"])

if option == "Upload Data":
    if st.button("Upload Embeddings to Pinecone"):
        upload_embeddings()
        st.success("✅ Embeddings uploaded successfully!")

elif option == "Search Movies":
    query = st.text_input("🔍 Enter a movie description or plot:")
    
    if st.button("Search"):
        if query:
            results = search_similar_movies(query)
            if results:
                for title, description in results:
                    st.write(f"🎥 **{title}**: {description}")
            else:
                st.warning("⚠️ No results found. Try another query.")
        else:
            st.warning("⚠️ Please enter a query.")
