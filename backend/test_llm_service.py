from services.llm_service import generate_answer


question = "What is a production house?"

context = """
A production house is a company or creative organization that produces
different types of media and entertainment content. It manages the process
of turning an idea or script into a finished production, such as films,
dramas, commercials, music videos, documentaries, and digital content.
"""


answer = generate_answer(
    question,
    context
)


print("\n" + "=" * 60)
print("LLM ANSWER")
print("=" * 60)

print(answer)

print("=" * 60)