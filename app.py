import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# App Setup
st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")
st.title("🐾 GroomerAI Pro: Visual Suite")

api_key = st.sidebar.text_input("Enter your Gemini Pro API Key", type="password")

if api_key:
    try:
        # Initialize the new 2025 Client
        client = genai.Client(api_key=api_key)
        
        pet_info = st.text_area("What did you do today?", placeholder="Groomed a Golden Retriever named Max...")

        if st.button("Generate Pro Assets"):
            with st.spinner('Creating marketing materials...'):
                
                # 1. TEXT GENERATION
                text_resp = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=f"Write a luxury Instagram post for a pet groomer: {pet_info}"
                )
                
                # 2. IMAGE GENERATION (The 'Pro' Way)
                # Note: 'imagen-3.0-generate-001' is the current gold standard
                try:
                    img_resp = client.models.generate_images(
                        model='imagen-3.0-generate-001',
                        prompt=f"A professional studio photo of a {pet_info}, clean, fluffy, luxury pet spa background.",
                        config=types.GenerateImagesConfig(number_of_images=1)
                    )
                    
                    if img_resp.generated_images:
                        img_bytes = img_resp.generated_images[0].image.image_bytes
                        st.image(Image.open(BytesIO(img_bytes)), caption="AI Generated Asset")
                except Exception as img_err:
                    st.warning("Image generation is restricted in Spain on the free tier. Using Pro text instead.")

                st.success("Marketing Copy Ready:")
                st.write(text_resp.text)
                
    except Exception as e:
        st.error(f"Setup Error: {e}")
else:
    st.info("Please enter your API Key to unlock the Pro Suite.")