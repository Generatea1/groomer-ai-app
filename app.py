import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾", layout="wide")
st.title("🐾 GroomerAI: 4K Content Studio")

api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    # Initialize with the standard v1 API for maximum compatibility
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Source Content")
        uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png', 'jpeg'])
        shop_name = st.text_input("Shop Name", "Luxury Paws")
        
    if st.button("🚀 Generate 4K Brand Bundle"):
        if uploaded_file:
            img_pil = Image.open(uploaded_file)
            
            with st.spinner('🎨 Nano Banana is rendering your 4K Assets...'):
                try:
                    # Using a simpler, highly direct prompt to ensure image triggering
                    prompt = f"""
                    Generate a marketing bundle for {shop_name}.
                    1. Write a professional Instagram caption and Google review reply.
                    2. Generate a high-quality 4K photo showing this dog in a 
                       luxury pet spa with a sign that says '{shop_name}'.
                    """

                    # Switching to the more stable 2.0 Flash model
                    response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=[prompt, img_pil],
                        config=types.GenerateContentConfig(
                            response_modalities=["TEXT", "IMAGE"]
                        )
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        
                        # New: Check if we got any parts back at all
                        if not response.parts:
                            st.warning("The AI processed the request but didn't return media. Trying a text-only fallback.")
                        
                        for part in response.parts:
                            if part.text:
                                st.markdown(part.text)
                            
                            # This is the "Media Catch" for Nano Banana
                            if part.inline_data:
                                generated_img = part.as_image()
                                st.image(generated_img, caption="✨ 4K Luxury Asset", use_container_width=True)
                                
                                # Download Logic
                                buf = io.BytesIO()
                                generated_img.save(buf, format="PNG")
                                st.download_button(
                                    label="📥 Download 4K Asset",
                                    data=buf.getvalue(),
                                    file_name=f"{shop_name}_4K.png",
                                    mime="image/png"
                                )
                                
                    st.success("Bundle Created!")

                except Exception as e:
                    st.error(f"Media Error: {e}")
                    st.info("Try refreshing your API key in AI Studio if the error persists.")
        else:
            st.warning("Please upload a photo first.")
else:
    st.info("Enter your API key to start.")