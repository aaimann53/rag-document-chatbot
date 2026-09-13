from services.retrieval_service import retrieve_relevant_chunks
from services.llm_service import generate_answer


def run_rag():

    print("\n" + "=" * 60)
    print("PRODUCTION HOUSE RAG CHATBOT")
    print("=" * 60)

    question = input("\nAsk a question: ")

    # -----------------------------------------
    # 1. Retrieve relevant chunks
    # -----------------------------------------

    documents = retrieve_relevant_chunks(question)

    # -----------------------------------------
    # 2. Combine retrieved chunks into context
    # -----------------------------------------

    context = "\n\n".join(documents)

    # -----------------------------------------
    # 3. Generate answer using Gemini
    # -----------------------------------------

    answer = generate_answer(
        question,
        context
    )

    # -----------------------------------------
    # 4. Display final answer
    # -----------------------------------------

    print("\n" + "=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)

    print(answer)

    print("=" * 60)


if __name__ == "__main__":
    run_rag()