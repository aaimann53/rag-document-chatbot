import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path, output_path):
    pdf_path = Path(pdf_path)
    output_path = Path(output_path)

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

    return all_text