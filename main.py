import pdfplumber
import re


def extract_text_from_pdf(pdf_path):
    """
    
    Extracts text from a PDF file.
    
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

text = extract_text_from_pdf("Resume.pdf")

def anonymize_pll(text, name_to_remove=None):
    
    #extract email
    text = re.sub(r'[\w\.-]+@[\w\.-]+', 'xxxxx@xxxx.com', text)
    
    #extract phone numbers
    text =  text = re.sub(r'(\+?\d{1,3})?[-.\s]?\(?\d{3,5}\)?[-.\s]?\d{3,5}[-.\s]?\d{3,5}', 'xx xxxx xxxx', text)
    
    #extract links
    text = re.sub(r'(linkedin|github)\.com[^\s]*', 'PROFILE_REDACTED', text, flags=re.I)
    
    if name_to_remove:
        text = text.replace(name_to_remove, 'John Doe')

    return text

def save_to_file(text, filename="anonymized_resume.txt"):
     with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
        
        
def main():
    
    pdf_path = "Resume.pdf"
    
    name_to_remove = "John Doe"
    
    text = extract_text_from_pdf(pdf_path)
    anonymized_text = anonymize_pll(text, name_to_remove)
    save_to_file(anonymized_text)
    
    print("✅ Anonymized resume saved to anonymized_resume.txt")

if __name__ == "__main__":
    main()