### Costume Identification App
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()  # Load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(prompt, image_parts):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, image_parts[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Initialize our Streamlit app
st.set_page_config(page_title="Costume Identification App")

st.header("Costume Identification App")
input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Analyze the Image")

default_prompt = """
Carefully analyze the uploaded image featuring a costume. Begin by identifying the overall type of costume displayed, which may range from historical, cultural, fantasy, superhero, to everyday fashion. Note any distinctive styles or themes that are evident, such as Victorian, Renaissance, futuristic, or specific character inspiration.

Examine and describe the color scheme of the costume, focusing on primary and secondary colors, as well as any patterns or motifs present. Detail the materials used in the costume's construction, such as fabric types (cotton, polyester, silk, leather) and any other materials (metal, plastic, natural elements) that contribute to its appearance and texture.

Provide a comprehensive item description, including all components of the costume such as dresses, suits, accessories (hats, jewelry, weapons), footwear, and props. Highlight unique features or intricate details that stand out, such as embroidery, digital components, lighting, or special effects makeup.

Based on the visual information, offer insights into the possible contexts or occasions for which the costume might be suitable, such as theatrical performances, cosplay events, historical reenactments, or fashion exhibitions.

Conclude with suggestions for enhancements or adjustments that could improve the costume's authenticity, comfort, or visual impact. This might include recommendations for accessory additions, material substitutions, or modifications to the design.

Emphasize that this AI-generated analysis aims to provide a detailed description and constructive feedback on the costume's design and presentation. It should serve as a guide for creators, enthusiasts, and professionals in the costume-making and fashion communities to refine and celebrate their work.
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(default_prompt, image_data)
    st.subheader("The Response is")
    st.write(response)
