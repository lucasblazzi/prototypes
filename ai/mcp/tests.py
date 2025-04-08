import PyPDF2 as pdf2


gips_pdf_path = "C:/Users/User/Blazzi/Repositories/prototypes/ai/mcp/servers/files/2020_gips_standards_firms.pdf"


def read_pdf(query: str = "What is TWR?"):
    query = query.lower()

    if "twr" not in query:
        return f"This tool only supports TWR queries. Please try again."
    
    with open(gips_pdf_path, "rb") as file:
        reader = pdf2.PdfReader(file)
        content = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                content += page.extract_text() + "\n"
        
    return (f"Using context from {gips_pdf_path}:\n\n"
            f"Content:\n{content}\n\n"
            f"Query: {query}\n\n"
            f"Please answer the question based on the content above.")


print(read_pdf())