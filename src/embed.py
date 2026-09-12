from pathlib import Path
import json

from sentence_transformers import SentenceTransformer


# -----------------------------
# File paths
# -----------------------------
input_file = Path("data/chunks.json")
output_file = Path("data/embedded_chunks.json")


# -----------------------------
# Load chunks
# -----------------------------
with open(input_file, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks.")


# -----------------------------
# Load embedding model
# -----------------------------
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded!")


# -----------------------------
# Generate embeddings
# -----------------------------
for chunk in chunks:
    embedding = model.encode(chunk["text"])

    chunk["embedding"] = embedding.tolist()

    print(f"Embedded chunk {chunk['chunk_id']}")


# -----------------------------
# Save embedded chunks
# -----------------------------
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=4, ensure_ascii=False)


print("\nEmbedding completed successfully!")
print(f"Saved to: {output_file}")