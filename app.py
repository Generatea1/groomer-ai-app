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
        # CHANGED: Using the more reliable 'latest' tag
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        # Input Section
        st.subheader("What happened in the salon today?")
        pet_info = st.text_area("Example: I groomed a Golden Retriever named Max. He was very muddy but now he's fluffy and smells like blueberries!")

        if st.button("Generate Marketing Bundle"):
            if pet_info:
                with st.spinner('Magic in progress...'):
                    prompt = f"""
                    You are a professional social media manager for a pet grooming salon.
                    Based on this: '{pet_info}', generate:
                    1. INSTAGRAM: A cute post with 10 hashtags.
                    2. FACEBOOK: A community-focused post.
                    3. GOOGLE BUSINESS: A professional update.
                    4. CLIENT SMS: A short 'Ready for pickup' text.
                    """
                    response = model.generate_content(prompt)
                    st.success("Bundle Ready!")
                    st.markdown(response.text)
            else:
                st.warning("Please enter some pet details first!")
                
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.info("Tip: Make sure your API key is correct and you have enabled the Gemini API in Google AI Studio.")
else:
    st.info("Please enter your License Key in the sidebar to start.")