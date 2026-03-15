import fitz
import sys

pdf_path = sys.argv[1]
try:
    doc = fitz.open(pdf_path)
    for page in doc:
        print(page.get_text())
except Exception as e:
    print(f"Error: {e}")
