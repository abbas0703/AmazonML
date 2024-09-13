import pytesseract

# Assuming Tesseract is configured as per earlier instructions
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Download pytesseract from the link https://github.com/UB-Mannheim/tesseract/wiki
# Function to extract entity value using OCR
def extract_entity_value(image_path, entity_type):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    
    # Use regex based on entity_type
    if entity_type == 'weight':
        pattern = r'(\d+(\.\d+)?\s?(gram|kg|kilogram|g))'
    elif entity_type == 'volume':
        pattern = r'(\d+(\.\d+)?\s?(ml|l|litre))'
    elif entity_type == 'dimensions': 
        pattern = r'(\d+(\.\d+)?\s?(centimetre|meter|inch|cm|m|mm))'
    elif entity_type ==  'voltage':
        pattern = r'(\d+(\.\d+)?\s?(volt|v))',
    elif entity_type ==  'wattage': 
        pattern = r'(\d+(\.\d+)?\s?(watt|w))'
    else:
        pattern = r'.*'  # Catch-all pattern
    
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return ""
