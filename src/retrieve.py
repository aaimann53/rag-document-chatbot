from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer


# -----------------------------
# ChromaDB location
# -----------------------------
db_path = "data/chroma_db"


# -----------------------------
# Load embedding model
# -----------------------------
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded!")


# -----------------------------
# Connect to ChromaDB
# -----------------------------
client = chromadb.PersistentClient(path=db_path)

collection = client.get_collection(
    name="production_house"
)


# -----------------------------
# User question
# -----------------------------
query = input("\nAsk a question: ")


# -----------------------------
# Convert question to embedding
# -----------------------------
query_embedding = model.encode(query).tolist()


# -----------------------------
# Search vector database
# -----------------------------
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


# -----------------------------
# Display retrieved chunks
# -----------------------------
print("\n" + "=" * 60)
print("RETRIEVED CHUNKS")
print("=" * 60)

for i, document in enumerate(results["documents"][0]):
    print(f"\nResult {i + 1}")
    print("-" * 60)
    print(document)

print("\n" + "=" * 60)