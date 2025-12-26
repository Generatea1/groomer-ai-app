import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="GroomerAI Suite", page_icon="??")
st.title("?? GroomerAI: Your Digital Assistant")

# Sidebar for API Key (Professional touch)
api_key = st.sidebar.text_input("Enter your License Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Input Section
    st.subheader("What happened in the salon today?")
    pet_info = st.text_area("Example: I groomed a Golden Retriever named Max. He was very muddy but now he's fluffy and smells like blueberries!")

    if st.button("Generate Marketing Bundle"):
        if pet_info:
            with st.spinner('Magic in progress...'):
                # The System Instruction
                prompt = f"""
                You are a professional social media manager for a high-end pet grooming salon.
                Based on this session: '{pet_info}', generate:
                1. INSTAGRAM: A cute post with 10 hashtags.
                2. FACEBOOK: A community-focused post.
                3. GOOGLE REVIEW REPLY: A template to thank the owner.
                4. CLIENT SMS: A short 'Ready for pickup' text.
                """
                response = model.generate_content(prompt)
                
                st.success("Bundle Ready!")
                st.markdown(response.text)
        else:
            st.warning("Please enter some pet details first!")
else:
    st.info("Please enter your License Key in the sidebar to start.")