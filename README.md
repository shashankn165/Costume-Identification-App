# Costume Identification App

The Costume Identification App leverages the Google Gemini Vision Pro API to analyze images of costumes. This app provides detailed descriptions of the costume's type, material, color scheme, and possible contexts for use, along with suggestions for enhancements. It is aimed at costume creators, enthusiasts, and professionals to refine and celebrate their work.

## Features
- Analyze costume images to identify type, material, and color scheme.
- Detailed descriptions and constructive feedback.
- Suitable for theatrical performances, cosplay events, historical reenactments, and fashion exhibitions.

## Setup

### Requirements

- Python 3.7+
- Streamlit
- Google Generative AI google.generativeai
- python-dotenv
- dotenv
- Pillow

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Costume-Identification-App.git
    cd Costume-Identification-App
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    ```bash
    cp .env.example .env
    ```

5. Add your Google API key to the `.env` file.

### Usage

Run the Streamlit app:
```bash
streamlit run app.py

