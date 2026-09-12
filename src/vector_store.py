from pathlib import Path
import json
import chromadb


# -----------------------------
# File paths
# -----------------------------
input_file = Path("data/embedded_chunks.json")
db_path = "data/chroma_db"


# -----------------------------
# Load embedded chunks
# -----------------------------
with open(input_file, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} embedded chunks.")


# -----------------------------
# Create ChromaDB client
# -----------------------------
client = chromadb.PersistentClient(path=db_path)


# -----------------------------
# Create collection
# -----------------------------
collection = client.get_or_create_collection(
    name="production_house"
)


# -----------------------------
# Add chunks to database
# -----------------------------
ids = []
documents = []
embeddings = []
metadatas = []

for chunk in chunks:
    ids.append(str(chunk["chunk_id"]))
    documents.append(chunk["text"])
    embeddings.append(chunk["embedding"])
    metadatas.append({
        "source": chunk["source"]
    })


collection.add(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)


# -----------------------------
# Verify database
# -----------------------------
print("\nVector database created successfully!")
print("Collection:", collection.name)
print("Number of documents:", collection.count())
print("Database location:", db_path)