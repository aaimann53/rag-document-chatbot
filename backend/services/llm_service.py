import os

from dotenv import load_dotenv
from google import genai


# -----------------------------
# Load environment variables
# -----------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is not set in the .env file"
    )


# -----------------------------
# Create Gemini client
# -----------------------------

client = genai.Client(api_key=api_key)


# -----------------------------
# Generate answer
# -----------------------------

def generate_answer(question, context):

    prompt = f"""
You are a helpful assistant answering questions about a Production House.

Use ONLY the information provided in the context below.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided document."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text