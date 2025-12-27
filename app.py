import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import io

st.set_page_config(page_title="GroomerAI Studio", page_icon="🐾", layout="wide")
st.title("🐾 GroomerAI: 4K Content Studio")

# Sidebar for the License Key
api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    # Use the modern 2025 Client
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Input")
        uploaded_file = st.file_uploader("Upload a Grooming Photo", type=['jpg', 'png', 'jpeg'])
        business_name = st.text_input("Business Name", "Luxury Paws")
        
    if st.button("Generate Luxury Brand Bundle"):
        if uploaded_file:
            # Convert uploaded file to PIL Image for the SDK
            image_data = Image.open(uploaded_file)
            
            with st.spinner('Generating Text & 4K Image...'):
                try:
                    # 1. TEXT GENERATION (Marketing Bundle)
                    # Using Gemini 3 Flash for the text logic
                    text_prompt = f"Create a viral Instagram caption, a Facebook community post, and a Google review reply for {business_name} based on this grooming photo. Use emojis and pet-friendly tone."
                    text_response = client.models.generate_content(
                        model="gemini-3-flash",
                        contents=[text_prompt, image_data]
                    )

                    # 2. IMAGE GENERATION (Nano Banana)
                    # Using Gemini 3 Pro Image (Nano Banana Pro) for 4K quality
                    img_prompt = "Keep the dog in the photo identical but change the background to a hyper-realistic high-end marble pet spa with soft golden lighting and a sign that says '" + business_name + "'. 4K resolution, cinematic photography."
                    img_response = client.models.generate_content(
                        model="gemini-3-pro-image-preview", 
                        contents=[img_prompt, image_data],
                        config=types.GenerateContentConfig(
                            response_modalities=["IMAGE"]
                        )
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        # Display Text
                        st.markdown(text_response.text)
                        
                        # Display Image
                        for part in img_response.parts:
                            if part.inline_data:
                                st.image(part.as_image(), caption="New 4K Luxury Brand Asset")
                                
                    st.success("Bundle Created! You just saved the client 4 hours of work.")

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please upload a photo first.")
else:
    st.info("Enter your API key in the sidebar to start.")