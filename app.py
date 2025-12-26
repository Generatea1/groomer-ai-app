import streamlit as st
from google import genai
from PIL import Image
from io import BytesIO

# App Config
st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")
st.title("🐾 GroomerAI: Pro Visual Suite")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter your Gemini Pro API Key", type="password")

if api_key:
    try:
        # NEW 2025 SDK INITIALIZATION
        client = genai.Client(api_key=api_key)
        
        pet_info = st.text_area("What did you do today?", placeholder="Groomed a Golden Retriever named Max...")

        if st.button("Generate Pro Marketing Bundle"):
            with st.spinner('Generating high-end assets...'):
                
                # 1. GENERATE TEXT (Using Gemini 2.5 Flash)
                text_response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=f"Create a 100-word Instagram post for: {pet_info}"
                )
                
                # 2. GENERATE IMAGE (Using Imagen 3.0)
                image_prompt = f"Professional high-end pet spa photography of a {pet_info}. Fluffy, clean, studio lighting, 8k."
                image_response = client.models.generate_images(
                    model='imagen-3.0-generate-001', # The elite image model
                    prompt=image_prompt
                )

                # Display Results
                if image_response.generated_images:
                    img_data = image_response.generated_images[0].image.image_bytes
                    st.image(Image.open(BytesIO(img_data)), caption="AI-Generated Marketing Asset")
                
                st.success("Your Marketing Post:")
                st.write(text_response.text)
                
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter your Pro API Key to start generating images.")