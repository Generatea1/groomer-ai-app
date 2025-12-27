import streamlit as st
from PIL import Image
import io

# Robust Import Logic
try:
    from google import genai
    from google.genai import types
except ImportError:
    st.error("The 'google-genai' library is missing. Please check your requirements.txt and reboot the app.")
    st.stop()

st.set_page_config(page_title="GroomerAI Studio", page_icon="🐾", layout="wide")

# Sidebar for License Key
api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Source Content")
        uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png', 'jpeg'])
        shop_name = st.text_input("Shop Name", "Luxury Paws")
        
    if st.button("Generate 4K Brand Bundle"):
        if uploaded_file:
            img_pil = Image.open(uploaded_file)
            
            with st.spinner('Generating Text & 4K Luxury Asset...'):
                try:
                    # 1. TEXT GENERATION (Marketing Bundle)
                    text_prompt = f"Write a luxury Instagram caption and a Google review reply for {shop_name} based on this photo."
                    text_res = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=[text_prompt, img_pil]
                    )

                    # 2. IMAGE GENERATION (Nano Banana Engine)
                    img_prompt = f"Hyper-realistic 4K luxury pet spa background for this dog. Include a marble floor and a gold sign that says '{shop_name}'."
                    img_res = client.models.generate_content(
                        model="gemini-2.0-flash-exp", # Using the latest 2025 multimodal model
                        contents=[img_prompt, img_pil]
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        st.markdown(text_res.text)
                        
                        # Displaying the Nano Banana result
                        # Note: In the new SDK, we check for image parts specifically
                        for part in img_res.parts:
                            if part.inline_data:
                                st.image(part.as_image(), caption="4K Luxury Asset")
                                
                    st.success("Bundle Created!")

                except Exception as e:
                    st.error(f"Error during generation: {e}")
        else:
            st.warning("Please upload a photo.")
else:
    st.info("Enter your API key in the sidebar.")