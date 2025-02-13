from fpdf import FPDF
from sentenceTransformer import Indexing
import unicodedata
import re

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "", 16)
        self.cell(200, 10, "Search Results", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
# Function to replace Unicode characters with ASCII equivalents
def clean_text(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

# Function to remove numbers
def remove_numbers(text):
    return re.sub(r'\d+', '', text)  # Removes all numbers


def createPDF(query_text):
    indexing= Indexing(query_text)
    
    try:
        documents = [clean_text(doc) for doc in indexing["documents"][0]]
        documents = [remove_numbers(doc) for doc in indexing["documents"][0]]
    except Exception as ex:
        print(ex)
    documents = [remove_numbers(doc) for doc in indexing["documents"][0]]
    documents=indexing["documents"][0]



    # Create PDF instance
    pdf = PDF()
    pdf.add_font("DejaVu", "", "./ttf/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", "", 12)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    #pdf.set_font("Arial", size=12)
    # Add Unicode font


    # Add content to the PDF
    pdf.cell(200, 10, f"Query: {query_text}", ln=True, align="L")
    pdf.ln(10)  # Add space

    for i, doc in enumerate(documents):
        pdf.multi_cell(0, 10, f"{i+1}. {doc}")
        pdf.ln(5)  # Add spacing between results

    # Save PDF file
    pdf_output_path = "search_results.pdf"

    pdf.output(pdf_output_path)