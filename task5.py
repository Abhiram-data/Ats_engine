import fitz  # PyMuPDF
import re
import os

class ResumeEngine:
    def __init__(self):
        # Normalize: Standardize bullet points [cite: 9]
        self.bullet_pattern = re.compile(r'[\u2022\u00b7\u25cf\u25cb\u25aa\u25ab\u2013]')

    def clean_text(self, text):
        """Cleans noise, normalizes bullets and capitalization [cite: 7, 8]"""
        # Remove standalone markers like '+1', '+2' found in the PDF [cite: 7]
        text = re.sub(r'\+\d+', '', text)
        
        # Replace various bullets with a standard '-' [cite: 9]
        text = self.bullet_pattern.sub('-', text)
        
        # Normalize: Spacing and line breaks [cite: 7]
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n+', '\n', text)
        
        return text.strip()

    def read_pdf(self, file_path):
        """Extracts text reliably while handling complex layouts [cite: 6, 12]"""
        doc = fitz.open(file_path)
        full_text = ""
        for page in doc:
            # 'blocks' handles columns and different layouts [cite: 12]
            blocks = page.get_text("blocks")
            for b in blocks:
                full_text += b[4] + "\n"
        return full_text

    def process_resume(self, file_path):
        """Main engine to convert resume into clean AI input [cite: 2, 3]"""
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."

        raw_text = self.read_pdf(file_path)
        return self.clean_text(raw_text)

# --- Automated Test Run  ---
if __name__ == "__main__":
    engine = ResumeEngine()
    
    # Path to your specific file
    my_file = r"C:\Dev\ress.pdf" 
    
    # Deliverable: Cleaned resume output 
    cleaned_data = engine.process_resume(my_file)
    
    # Store extracted text in structured files [cite: 13]
    with open("cleaned_output.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_data)
        
    # Test result log 
    print("Success: Extraction complete. Results in cleaned_output.txt")