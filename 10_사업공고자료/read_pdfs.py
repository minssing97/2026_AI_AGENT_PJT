import sys
try:
    import fitz # PyMuPDF
except ImportError:
    import os
    os.system("python -m pip install pymupdf")
    import fitz
import os

out_path = sys.argv[1]
pdf_dir = sys.argv[2]

pdfs = [
    "붙임 1. 2026년 AI AGENT 융합 확산 지원사업 신규과제 모집 공고문.pdf",
    "붙임 2. 2026년 AI AGENT 융합 확산 지원사업 공모안내서.pdf",
    "붙임 3. 2026년 AI AGENT 융합·확산 지원 사업 수행계획서 양식.pdf",
    "붙임 4. 2026년 AI AGENT 융합·확산 지원 사업 제출서류.pdf"
]

with open(out_path, 'w', encoding='utf-8') as f:
    for pdf in pdfs:
        full_path = os.path.join(pdf_dir, pdf)
        f.write(f"\n\n{'='*50}\nFILENAME: {pdf}\n{'='*50}\n")
        try:
            doc = fitz.open(full_path)
            for page in doc:
                f.write(page.get_text())
        except Exception as e:
            f.write(f"Error reading {pdf}: {e}\n")
