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
        
        # We use the base model name; the SDK handles the versioning.
        model = genai.GenerativeModel('gemini-1.5-flash')

        st.subheader("What happened in the salon today?")
        pet_info = st.text_area("Example: I groomed a Golden Retriever named Max. He was very muddy but now he's fluffy and smells like blueberries!")

        if st.button("Generate Marketing Bundle"):
            if pet_info:
                with st.spinner('Magic in progress...'):
                    # Clearer instructions to ensure no 404 on the content call
                    response = model.generate_content(
                        f"Professional Pet Groomer Social Media Manager: Create a bundle for: {pet_info}"
                    )
                    st.success("Bundle Ready!")
                    st.markdown(response.text)
            else:
                st.warning("Please enter some pet details first!")
                
    except Exception as e:
        st.error(f"Setup Error: {e}")
        st.info("If you still see 'Location not supported', it is because you are in Spain using a Free Key. To bypass this instantly: Go to Google AI Studio and link a credit card to enable 'Pay-as-you-go'. You will still get thousands of requests for $0, but it unlocks the regional block.")
else:
    st.info("Please enter your License Key in the sidebar to start.")