from typing import Dict
def simple_token_count(text: str) -> int:
    return len(text.split())

def textextractor_dummy(file_path: str) -> Dict:
    # placeholder: returns the file contents as one big string
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return {'text': f.read(), 'pages': 1}
