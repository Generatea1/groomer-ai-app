import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="GroomerAI Studio", page_icon="✂️", layout="wide")
st.title("✂️ GroomerAI: 4K Brand Transformation")

# User enters their own API Key or you hardcode yours for the demo
api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Source Content")
        ig_url = st.text_input("Paste Instagram Image URL here")
        # In a real app, you'd use a scraper, but for the demo, they can upload the photo
        uploaded_file = st.file_uploader("Or Upload the Grooming Photo", type=['jpg', 'png'])

    if st.button("Generate Luxury 4K Bundle"):
        if uploaded_file:
            with st.spinner('Generating 4K Luxury Portrait...'):
                # IMAGE GENERATION (Nano Banana)
                img_response = client.models.generate_content(
                    model="gemini-2.5-flash-image",
                    contents=["Transform this dog into a 4K luxury cinematic portrait in a marble salon, soft gold lighting, professional photography style.", uploaded_file]
                )
                # Display Image
                for part in img_response.parts:
                    if part.inline_data:
                        st.image(part.as_image(), caption="New 4K Luxury Asset")

            with st.spinner('Creating Veo Video Ad...'):
                # VIDEO GENERATION (Veo)
                video_op = client.models.generate_videos(
                    model="veo-3.1-fast-generate-preview",
                    prompt="A cinematic slow-motion pan of the dog in a luxury salon. Soft lighting, high-end commercial feel.",
                    config=types.GenerateVideosConfig(number_of_videos=1)
                )
                st.info("Video is processing... (This takes 1-2 minutes)")
                # (In production, you would poll the operation status here)
        else:
            st.error("Please provide an image first!")
else:
    st.info("Enter your key to unlock Nano Banana & Veo features.")