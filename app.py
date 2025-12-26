import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="GroomerAI Suite", page_icon="🐾")
st.title("🐾 GroomerAI: Your Digital Assistant")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter your License Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # THE FIX: Updated to the 2.5 Flash-Lite model which is more accessible in EU
        model = genai.GenerativeModel('gemini-2.5-flash-lite')

        st.subheader("What happened in the salon today?")
        pet_info = st.text_area("Example: I groomed a Golden Retriever named Max. He was very muddy but now he's fluffy and smells like blueberries!")

        if st.button("Generate Marketing Bundle"):
            if pet_info:
                with st.spinner('Magic in progress...'):
                    response = model.generate_content(
                        f"Professional Pet Groomer Social Media Manager: Create a bundle for: {pet_info}"
                    )
                    st.success("Bundle Ready!")
                    st.markdown(response.text)
            else:
                st.warning("Please enter some pet details first!")
                
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("COACH TIP: If you still see '404', go to Google AI Studio and search for 'gemini-2.5-flash-lite' in the model dropdown to ensure your key has access.")
else:
    st.info("Please enter your License Key in the sidebar to start.")