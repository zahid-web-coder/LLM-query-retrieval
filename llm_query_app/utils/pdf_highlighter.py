import fitz  # PyMuPDF
import io

def highlight_clauses_in_pdf(file, clauses):
    # Open the PDF from the uploaded file stream
    doc = fitz.open(stream=file.read(), filetype="pdf")

    for page in doc:
        for clause in clauses:
            # Clean clause (sometimes newline issues cause matching errors)
            clean_clause = clause.strip().replace("\n", " ").replace("  ", " ")

            # Try searching the text
            matches = page.search_for(clean_clause)

            for match in matches:
                page.add_highlight_annot(match)

    # Save to in-memory buffer
    output = io.BytesIO()
    doc.save(output, garbage=4, deflate=True)
    doc.close()
    output.seek(0)

    return output
