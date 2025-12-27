import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

# App Layout
st.set_page_config(page_title="GroomerAI Studio Pro", page_icon="🐾", layout="wide")
st.title("🐾 GroomerAI: 4K Content Studio")

# 1. Sidebar for API Authentication
api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    # Initialize the current 2025 SDK Client
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Source Content")
        uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png', 'jpeg'])
        shop_name = st.text_input("Grooming Shop Name", "Luxury Paws")
        
    if st.button("🚀 Generate 4K Brand Bundle"):
        if uploaded_file:
            img_pil = Image.open(uploaded_file)
            
            with st.spinner('🎨 Nano Banana Pro is rendering your 4K Assets...'):
                try:
                    # PROMPT: Unified request for Text + High-End Image
                    prompt = f"""
                    You are a luxury marketing expert for {shop_name}.
                    1. TEXT: Write a professional Instagram caption and Google review reply.
                    2. IMAGE: Generate a 4K photorealistic luxury image of this dog in 
                       a cinematic pet spa. Background must have marble walls, 
                       gold lighting, and a sign saying '{shop_name}'.
                    """

                    # Using the active 2025 Image Generation Model
                    # This replaces the retired 2.0 models to stop 404 errors.
                    response = client.models.generate_content(
                        model="gemini-3-pro-image-preview", 
                        contents=[prompt, img_pil],
                        config=types.GenerateContentConfig(
                            response_modalities=["TEXT", "IMAGE"] # Specifically triggers Nano Banana
                        )
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        
                        # Loop through interleaved parts (Text AND Image data)
                        for part in response.parts:
                            if part.text:
                                st.markdown(part.text)
                            
                            if part.inline_data:
                                generated_img = part.as_image()
                                st.image(generated_img, caption="✨ 4K Luxury Asset", use_container_width=True)
                                
                                # Download Button for the generated 4K image
                                buf = io.BytesIO()
                                generated_img.save(buf, format="PNG")
                                st.download_button(
                                    label="📥 Download 4K Asset",
                                    data=buf.getvalue(),
                                    file_name=f"{shop_name}_4K_Promo.png",
                                    mime="image/png"
                                )
                                
                    st.success("Bundle Created Successfully!")

                except Exception as e:
                    st.error(f"Media Error: {e}")
                    st.info("Ensure you are using a US-based API key if image generation is blocked in your region.")
        else:
            st.warning("Please upload a dog photo first.")
else:
    st.info("Enter your API key in the sidebar to unlock the studio.")