import streamlit as st
from google import genai
from google.genai import types
from PIL import Image

st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾", layout="wide")
st.title("🐾 GroomerAI: 4K Brand Transformation")

# License Key in Sidebar
api_key = st.sidebar.text_input("Enter License Key", type="password")

if api_key:
    # Initializing the 2025 SDK Client
    client = genai.Client(api_key=api_key)
    
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("1. Source Content")
        uploaded_file = st.file_uploader("Upload Grooming Photo", type=['jpg', 'png', 'jpeg'])
        shop_name = st.text_input("Shop Name", "Luxury Paws")
        
    if st.button("Generate 4K Brand Bundle"):
        if uploaded_file:
            img = Image.open(uploaded_file)
            
            with st.spinner('Generating Text & Nano Banana Image...'):
                try:
                    # 1. GENERATE MARKETING TEXT
                    text_prompt = f"Write a high-end Instagram caption and Google Review reply for {shop_name} based on this dog grooming photo."
                    text_res = client.models.generate_content(
                        model="gemini-3-flash", # Latest text model
                        contents=[text_prompt, img]
                    )

                    # 2. GENERATE 4K IMAGE (Nano Banana)
                    img_prompt = f"Transform this dog into a luxury 4K portrait in a marble pet spa with a sign that says '{shop_name}'."
                    img_res = client.models.generate_content(
                        model="gemini-2.5-flash-image", # Nano Banana
                        contents=[img_prompt, img]
                    )

                    with col2:
                        st.subheader("2. Your Results")
                        st.markdown(text_res.text)
                        
                        # Displaying the Nano Banana result
                        for part in img_res.parts:
                            if part.inline_data:
                                st.image(part.as_image(), caption="New 4K Luxury Asset")
                                
                    st.success("Bundle Complete!")

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please upload a photo.")
else:
    st.info("Please enter your API key in the sidebar.")