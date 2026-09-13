from services.retrieval_service import retrieve_relevant_chunks


question = input("\nAsk a question: ")

retrieve_relevant_chunks(question)