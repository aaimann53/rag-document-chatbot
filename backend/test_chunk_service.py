from services.chunk_service import create_chunks


create_chunks(
    "data/extracted_text.txt",
    "data/chunks.json"
)