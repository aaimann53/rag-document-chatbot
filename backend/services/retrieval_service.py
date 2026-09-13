import chromadb
from sentence_transformers import SentenceTransformer


def retrieve_relevant_chunks(
    question,
    db_path="data/chroma_db",
    collection_name="production_house",
    top_k=3
):

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
        name=collection_name
    )

    # -----------------------------
    # Convert question to embedding
    # -----------------------------

    query_embedding = model.encode(question).tolist()

    # -----------------------------
    # Search vector database
    # -----------------------------

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    # -----------------------------
    # Get retrieved chunks
    # -----------------------------

    documents = results["documents"][0]

    print("\n" + "=" * 60)
    print("RETRIEVED CHUNKS")
    print("=" * 60)

    for i, document in enumerate(documents):

        print(f"\nResult {i + 1}")
        print("-" * 60)
        print(document)

    print("\n" + "=" * 60)

    return documents