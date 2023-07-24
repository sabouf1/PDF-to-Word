from pdf2docx import Converter

def pdf_to_word(pdf_file, word_file):
    # Convert PDF to Word using pdf2docx
    cv = Converter(pdf_file)
    cv.convert(word_file)
    cv.close()
    print(f"Conversion complete. Output saved to {word_file}")

if __name__ == "__main__":
    pdf_file_path = "input.pdf"  # Replace with the path to your input PDF file
    word_file_path = "output.docx"  # Replace with the desired output Word file name

    pdf_to_word(pdf_file_path, word_file_path)
