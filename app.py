
import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾", layout="wide")
st.title("🐾 GroomerAI: 4K Content Studio")

api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Source Content")
        uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png', 'jpeg'])
        shop_name = st.text_input("Shop Name", "Luxury Paws")
        
    if st.button("🚀 Generate 4K Brand Bundle"):
        if uploaded_file:
            img_pil = Image.open(uploaded_file)
            
            with st.spinner('🎨 Nano Banana Pro is rendering (approx. 30-40 seconds)...'):
                try:
                    prompt = f"1. Write a luxury IG caption for {shop_name}. 2. Generate a 4K luxury spa image of this dog with a sign saying '{shop_name}'."

                    response = client.models.generate_content(
                        model="gemini-3-pro-image-preview", 
                        contents=[prompt, img_pil],
                        config=types.GenerateContentConfig(
                            response_modalities=["TEXT", "IMAGE"]
                        )
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        for part in response.parts:
                            if part.text:
                                st.markdown(part.text)
                            
                            if part.inline_data:
                                # SUCCESS: We found the image data!
                                raw_img = part.as_image()
                                
                                # FIX: Manually save to a byte buffer to bypass the 'format' error
                                buf = io.BytesIO()
                                # We explicitly tell PIL to save this as a PNG
                                raw_img.save(buf, format="PNG") 
                                byte_im = buf.getvalue()
                                
                                # Display using the stable byte data
                                st.image(byte_im, caption="✨ 4K Luxury Asset", use_container_width=True)
                                
                                # Add the Download Button
                                st.download_button(
                                    label="📥 Download 4K Asset",
                                    data=byte_im,
                                    file_name=f"{shop_name}_4K.png",
                                    mime="image/png"
                                )
                                
                    st.success("Bundle Created!")

                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("Check your Google Cloud Billing if you see 404/NOT_FOUND.")
        else:
            st.warning("Please upload a photo first.")
else:
    st.info("Enter your API key in the sidebar.")