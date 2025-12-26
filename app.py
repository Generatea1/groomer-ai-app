import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")
st.title("🐾 GroomerAI: Visual Marketing Suite")

api_key = st.sidebar.text_input("Enter your Gemini Pro API Key", type="password")

if api_key:
    try:
        # Initialize the new 2025 Client
        client = genai.Client(api_key=api_key)
        
        pet_info = st.text_area("Describe the dog and the result:", placeholder="A fluffy Golden Retriever after a blueberry spa...")

        if st.button("Generate Professional Asset"):
            with st.spinner('AI is painting your marketing image...'):
                
                # We use 'gemini-2.5-flash-image' which is optimized for this
                response = client.models.generate_content(
                    model='gemini-2.5-flash-image',
                    contents=f"Create a high-end, professional studio photograph for a pet grooming business of: {pet_info}. Soft lighting, clean background, luxury spa vibe.",
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE"]
                    )
                )

                # Process and display the image
                for part in response.parts:
                    if part.inline_data:
                        img = Image.open(BytesIO(part.inline_data.data))
                        st.image(img, caption="Custom Marketing Asset")
                        st.success("Image Generated! You can now send this to your client.")
                        
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Tip: Ensure you have enabled the 'Gemini Pro' or 'Imagen' API in your Google Cloud/AI Studio console.")
else:
    st.info("Enter your API Key to unlock image generation.")