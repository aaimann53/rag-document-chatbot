from pathlib import Path
import re
import json


# --------------------------------------------------
# 1. Read extracted text
# --------------------------------------------------

text_file = Path("data/extracted_text.txt")

text = text_file.read_text(encoding="utf-8")


# --------------------------------------------------
# 2. Clean text
# --------------------------------------------------

# Remove standalone page numbers
text = re.sub(r'(?m)^\s*\d+\s*$', '', text)

# Remove excessive spaces
text = re.sub(r'[ \t]+', ' ', text)

# Remove excessive blank lines
text = re.sub(r'\n\s*\n+', '\n\n', text)

text = text.strip()


# --------------------------------------------------
# 3. Split into paragraphs
# --------------------------------------------------

paragraphs = text.split("\n\n")


# --------------------------------------------------
# 4. Split paragraphs into sentences
# --------------------------------------------------

sentences = []

for paragraph in paragraphs:

    paragraph = paragraph.strip()

    if not paragraph:
        continue

    parts = re.split(r'(?<=[.!?])\s+', paragraph)

    for part in parts:

        part = part.strip()

        if part:
            sentences.append(part)


# --------------------------------------------------
# 5. Create chunks
# --------------------------------------------------

chunk_size = 500

chunks = []

current_chunk = ""

for sentence in sentences:

    if len(current_chunk) + len(sentence) + 1 <= chunk_size:

        if current_chunk:
            current_chunk += " " + sentence
        else:
            current_chunk = sentence

    else:

        if current_chunk:
            chunks.append(current_chunk.strip())

        current_chunk = sentence


# Add final chunk
if current_chunk:
    chunks.append(current_chunk.strip())


# --------------------------------------------------
# 6. Add metadata
# --------------------------------------------------

documents = []

for i, chunk in enumerate(chunks):

    document = {
        "chunk_id": i + 1,
        "source": "Production House.pdf",
        "text": chunk
    }

    documents.append(document)


# --------------------------------------------------
# 7. Save chunks as JSON
# --------------------------------------------------

output_file = Path("data/chunks.json")

with open(output_file, "w", encoding="utf-8") as f:

    json.dump(documents, f, indent=4, ensure_ascii=False)


# --------------------------------------------------
# 8. Display chunks
# --------------------------------------------------

for document in documents:

    print("\n" + "=" * 60)

    print(f"CHUNK {document['chunk_id']}")

    print("=" * 60)

    print("Source:", document["source"])

    print("Text:", document["text"])

    print("Characters:", len(document["text"]))


print("\n" + "=" * 60)

print(f"TOTAL CHUNKS: {len(documents)}")

print(f"Saved to: {output_file}")

print("=" * 60)