import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

st.set_page_config(page_title="GroomerAI Pro 2026", layout="wide")
st.title("🐾 GroomerAI: 4K Content Studio")

api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    # 2025 SDK Client initialization
    client = genai.Client(api_key=api_key)
    
    uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png'])
    shop_name = st.text_input("Shop Name", "Luxury Paws")
        
    if st.button("🚀 Generate 4K Brand Bundle"):
        if uploaded_file:
            img_pil = Image.open(uploaded_file)
            with st.spinner('🎨 Nano Banana Pro is rendering...'):
                try:
                    # UPDATED 2025 PROMPT & MODEL
                    # Use 'gemini-3-pro-image-preview' for 4K Nano Banana Pro
                    response = client.models.generate_content(
                        model="gemini-3-pro-image-preview", 
                        contents=[f"4K luxury marketing image for {shop_name}", img_pil],
                        config=types.GenerateContentConfig(
                            response_modalities=["TEXT", "IMAGE"],
                            image_config=types.ImageConfig(image_size="4K")
                        )
                    )

                    for part in response.parts:
                        if part.text: st.markdown(part.text)
                        if part.inline_data:
                            st.image(part.as_image(), caption="✨ 4K Asset")
                except Exception as e:
                    st.error(f"Media Error: {e}")
                    st.info("Ensure Billing is enabled in Google Cloud Console.")
else:
    st.info("Enter your API key in the sidebar.")