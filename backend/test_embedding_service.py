from services.embedding_service import generate_embeddings


generate_embeddings(
    "data/chunks.json",
    "data/embedded_chunks.json"
)