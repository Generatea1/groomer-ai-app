import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="GroomerAI Pro Suite", page_icon="🐾")
st.title("🐾 GroomerAI: Visual Marketing Suite")

api_key = st.sidebar.text_input("Enter your API Key", type="password")

if api_key:
    try:
        client = genai.Client(api_key=api_key)
        
        pet_info = st.text_area("What happened in the salon?", placeholder="A Golden Retriever named Max...")

        if st.button("Generate Professional Assets"):
            with st.spinner('AI is generating your marketing suite...'):
                
                # THE BYPASS: Using the latest model and specific modality request
                response = client.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=f"Generate a professional, high-end studio photograph of a {pet_info} in a luxury pet spa. Include a 100-word Instagram caption below the image.",
                    config=types.GenerateContentConfig(
                        response_modalities=["IMAGE", "TEXT"]
                    )
                )

                # Display Logic
                for part in response.candidates[0].content.parts:
                    if part.inline_data:
                        img = Image.open(BytesIO(part.inline_data.data))
                        st.image(img, caption="AI-Generated Pro Asset")
                    if part.text:
                        st.success("Marketing Copy Ready:")
                        st.write(part.text)
                        
    except Exception as e:
        st.error(f"Setup Error: {e}")
else:
    st.info("Please enter your API Key to start.")