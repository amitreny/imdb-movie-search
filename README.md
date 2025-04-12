# 🎬 IMDb Movie Search App with Pinecone and Sentence Transformers

## 🚀 Overview
This is a **Streamlit-based** application that allows users to search for similar movies based on plot descriptions. It uses **`sentence-transformers/all-MiniLM-L6-v2`** to generate text embeddings and stores them in **Pinecone** for efficient similarity search.

## ✨ Features
- 🎥 **Search for similar movies** by entering a plot or description.
- 🔎 **Embeddings powered by `sentence-transformers/all-MiniLM-L6-v2`** (384-dimensional vectors).
- 🚀 **Fast similarity search** using **Pinecone** vector database.
- 📊 **User-friendly UI** built with **Streamlit**.
- 🛠️ **Efficient movie search** without duplicate results.

## 📚 Project Structure
```
imdb_search_app/
│── data/
│   ├── imdb_top_1000.csv  # IMDb dataset from Kaggle
│── app.py  # Streamlit UI
│── embedding_utils.py  # Generate and store embeddings
│── pinecone_setup.py  # Initialize and manage Pinecone index
│── requirements.txt  # Dependencies
│── .env  # API keys (ignored in Git)
│── .gitignore  # Prevents sensitive files from being uploaded
```

## 💪 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/amitreny/imdb-movie-search.git
cd imdb-movie-search
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
Create a `.env` file and add:
```env
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
PINECONE_INDEX_NAME=imdb-movies
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

## 🔢 How It Works
### 💾 Upload Movie Embeddings
- Extracts **titles & overviews** from the IMDb dataset.
- Generates **embeddings** using `sentence-transformers/all-MiniLM-L6-v2`.
- Stores embeddings in **Pinecone** for fast retrieval.

### 🔍 Search for Similar Movies
- Enter a **movie description** in the search bar.
- Retrieves **top 5 similar movies** using cosine similarity.
- Ensures **no duplicate results** in search results.

## 📜 Dataset
- **IMDb Top 1000 Movies Dataset** from Kaggle ([Download Here](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows?resource=download)).
- Contains **movie titles, overviews, and other metadata**.

## 🌟 Future Enhancements
✅ Add support for **multiple embedding models**.  
✅ Enable **real-time dataset updates** from IMDb API.  
✅ Improve **search ranking** with more metadata (e.g., genres, actors).  

## 💪 Contributing
Want to improve the project? Feel free to **fork**, open an **issue**, or submit a **pull request**!

## 📄 License
This project is licensed under the **MIT License**.
