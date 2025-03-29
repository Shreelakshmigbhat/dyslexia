from flask import Flask, render_template, request
import os
import zipfile

app = Flask(__name__)

# Character mappings for Dyslexic Encoding (No Numbers)
char_to_dyslexic = {
    'A': 'Δ', 'B': 'β', 'C': 'Ͼ', 'D': 'ↁ', 'E': 'ε', 'F': 'Ϝ', 'G': 'Ϭ', 'H': 'н', 
    'I': 'ι', 'J': 'ʝ', 'K': 'κ', 'L': 'ʟ', 'M': 'м', 'N': 'и', 'O': 'σ', 'P': 'ρ', 
    'Q': 'φ', 'R': 'я', 'S': 'ѕ', 'T': 'т', 'U': 'υ', 'V': 'ν', 'W': 'ω', 'X': 'χ', 
    'Y': 'γ', 'Z': 'ƶ'
}
# Include lowercase mappings
char_to_dyslexic.update({k.lower(): v.lower() for k, v in char_to_dyslexic.items()})

# Reverse mapping (Dyslexic to English)
dyslexic_to_char = {v: k for k, v in char_to_dyslexic.items()}

def english_to_dyslexic(text):
    """ Convert English text to Dyslexic encoding """
    return "".join(char_to_dyslexic.get(char, char) for char in text)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        print(f"Received text: {text}")  # Debugging
        translated_text = english_to_dyslexic(text)
        print(f"Translated text: {translated_text}")  # Debugging

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)