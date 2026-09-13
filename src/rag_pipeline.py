from sentence_transformers import SentenceTransformer
import chromadb

from llm_service import generate_answer


# --------------------------------------------------
# 1. Load embedding model
# --------------------------------------------------

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded!")


# --------------------------------------------------
# 2. Connect to ChromaDB
# --------------------------------------------------

db_path = "data/chroma_db"

client = chromadb.PersistentClient(path=db_path)

collection = client.get_collection(
    name="production_house"
)

print("Connected to ChromaDB!")


# --------------------------------------------------
# 3. Ask the user a question
# --------------------------------------------------

question = input("\nAsk a question: ")


# --------------------------------------------------
# 4. Convert question into embedding
# --------------------------------------------------

query_embedding = model.encode(question).tolist()


# --------------------------------------------------
# 5. Retrieve relevant chunks
# --------------------------------------------------

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)


# --------------------------------------------------
# 6. Build context from retrieved chunks
# --------------------------------------------------

retrieved_documents = results["documents"][0]

context = "\n\n".join(retrieved_documents)


# --------------------------------------------------
# 7. Send context + question to Gemini
# --------------------------------------------------

answer = generate_answer(
    question,
    context
)


# --------------------------------------------------
# 8. Display final answer
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print(answer)

print("=" * 60)