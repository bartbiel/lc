
import os
import grants
import PyPDF2
'''
create a list of useful pdf files from the source
no pdfs from scan included
'''

def listOfValidatedPDFs(directory):
    result=[]
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Get all PDF files in the directory
    pdf_files = [file for file in os.listdir(directory) if file.lower().endswith('.pdf')]

    if not pdf_files:
        print(f"No PDF files found in '{directory}'.")
        return

    # Process each PDF file
    for pdf_file in pdf_files:
        #print(f"================{pdf_file}==============")
        file_path = os.path.join(directory, pdf_file)
        

        try:
            # Open and read the PDF file
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                #print(f"file={pdf_file} length={len(reader.pages)}")
                # Check if the PDF has at least one page
                if len(reader.pages) > 0:
                    #first_page = reader.pages[0]
                    result.append(file_path)
                    #print(f"length of first page is {len(first_page)}")
                    #print(first_page.extract_text())
                else:
                    print(f"'{pdf_file}' has no pages.")
        except PyPDF2.PdfReadError:
            print(f"Error: '{pdf_file}' is not a valid PDF or is corrupted.")
        except PermissionError:
            print(f"Error: Permission denied to read '{pdf_file}'.")
        except Exception as e:
            print(f"An unexpected error occurred while processing '{pdf_file}': {e}")
    return result

directory_path = grants.PDF_PATH
result = listOfValidatedPDFs(directory_path)

