import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="GroomerAI Visual Suite", page_icon="🐾")
st.title("🐾 GroomerAI: Visual Marketing Suite")

api_key = st.sidebar.text_input("Enter your License Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Using the new Imagen model for image generation
        image_model = genai.GenerativeModel('imagen-3.0-generate-preview')
        text_model = genai.GenerativeModel('gemini-2.5-flash-lite')

        pet_info = st.text_area("What did you do today?", placeholder="Groomed a Golden Retriever named Max...")

        if st.button("Generate Full Visual Bundle"):
            with st.spinner('Generating professional assets...'):
                # 1. Generate the Marketing Copy
                text_response = text_model.generate_content(f"Create a 100-word Instagram post for: {pet_info}")
                
                # 2. Generate a Professional Marketing Image
                image_prompt = f"A professional, high-quality studio photograph of a {pet_info}. The dog looks clean, fluffy, and happy in a luxury pet spa setting. Soft lighting, 8k resolution."
                image_response = image_model.generate_images(prompt=image_prompt)
                
                # Display Results
                st.image(image_response.images[0], caption="AI-Generated Marketing Image")
                st.success("Your Marketing Post:")
                st.write(text_response.text)
                
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Enter your License Key to unlock Visual Generation.")