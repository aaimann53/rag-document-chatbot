from services.vector_store import create_vector_store


create_vector_store(
    "data/embedded_chunks.json",
    "data/chroma_db",
    "production_house"
)