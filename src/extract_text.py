import pymupdf
from pathlib import Path


pdf_path = Path("data/documents/Production House.pdf")

output_path = Path("data/extracted_text.txt")


doc = pymupdf.open(pdf_path)


all_text = ""


for page_number, page in enumerate(doc):

    text = page.get_text()

    print(f"\n--- Page {page_number + 1} ---")
    print(text)

    all_text += text + "\n"


output_path.write_text(all_text, encoding="utf-8")


print("\nText extraction completed!")
print(f"Saved to: {output_path}")