import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

# Setup the page layout
st.set_page_config(page_title="GroomerAI Studio", page_icon="🐾", layout="wide")
st.title("🐾 GroomerAI: 4K Content Studio")

# 1. SIDEBAR: Authentication
api_key = st.sidebar.text_input("Enter your License Key", type="password")

if api_key:
    # Initialize the 2025 SDK Client
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Source Content")
        uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png', 'jpeg'])
        shop_name = st.text_input("Grooming Shop Name", "Luxury Paws")
        
    if st.button("🚀 Generate 4K Brand Bundle"):
        if uploaded_file:
            # Convert uploaded file for processing
            img_pil = Image.open(uploaded_file)
            
            with st.spinner('AI is crafting your 4K media and text...'):
                try:
                    # THE UNIFIED PROMPT: We ask for text AND an image in one go
                    # This tells the model to use Nano Banana for the visual part
                    prompt = f"""
                    You are a luxury marketing agent for '{shop_name}'. 
                    1. Provide a high-end Instagram caption and a Google review reply.
                    2. Then, generate an image (Nano Banana) showing this exact dog 
                       in a 4K cinematic luxury spa with a marble floor and a sign 
                       that says '{shop_name}'.
                    """
                    
                    # Generate content with 'IMAGE' and 'TEXT' modalities enabled
                    response = client.models.generate_content(
                        model="gemini-2.5-flash-image", # The Nano Banana engine
                        contents=[prompt, img_pil],
                        config=types.GenerateContentConfig(
                            response_modalities=["TEXT", "IMAGE"]
                        )
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        
                        # Loop through response parts to find text and image data
                        for part in response.parts:
                            # Handle Text (Captions/Replies)
                            if part.text:
                                st.markdown(part.text)
                            
                            # Handle Image (Nano Banana 4K Asset)
                            if part.inline_data:
                                generated_img = part.as_image()
                                st.image(generated_img, caption="✨ 4K Luxury Asset", use_container_width=True)
                                
                                # Add a Download Button for the 4K image
                                buf = io.BytesIO()
                                generated_img.save(buf, format="PNG")
                                st.download_button(
                                    label="📥 Download 4K Asset",
                                    data=buf.getvalue(),
                                    file_name=f"{shop_name}_4K_Promo.png",
                                    mime="image/png"
                                )
                                
                    st.success("Bundle Created! Ready to send to your client.")

                except Exception as e:
                    st.error(f"Generation Error: {e}")
                    st.info("Tip: Ensure 'Nano Banana' features are enabled in your AI Studio settings.")
        else:
            st.warning("Please upload a photo to start the transformation.")
else:
    st.info("Enter your API key in the sidebar to unlock the studio.")