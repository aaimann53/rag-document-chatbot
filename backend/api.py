from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.retrieval_service import retrieve_relevant_chunks
from backend.services.llm_service import generate_answer

# -----------------------------------------
# Create FastAPI application
# -----------------------------------------

app = FastAPI(
    title="Production House RAG API",
    description="API for asking questions about the Production House document",
    version="1.0.0"
)


# -----------------------------------------
# Request model
# -----------------------------------------

class QuestionRequest(BaseModel):
    question: str


# -----------------------------------------
# Health check
# -----------------------------------------

@app.get("/")
def root():
    return {
        "message": "Production House RAG API is running"
    }


# -----------------------------------------
# Ask question
# -----------------------------------------

@app.post("/ask")
def ask_question(request: QuestionRequest):

    # Retrieve relevant chunks
    documents = retrieve_relevant_chunks(
        request.question
    )

    # Combine chunks into context
    context = "\n\n".join(documents)

    # Generate answer
    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer
    }