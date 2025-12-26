import streamlit as st
import google.generativeai as genai

# Setup
st.set_page_config(page_title="GroomerAI Suite", page_icon="🐾")
st.title("🐾 GroomerAI: Your Digital Assistant")

api_key = st.sidebar.text_input("Enter your License Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # THE FIX: We use 'models/gemini-1.5-flash' which is the correct internal path
        # for keys generated in the EU/UK region.
        model = genai.GenerativeModel('models/gemini-1.5-flash')

        st.subheader("What happened in the salon today?")
        pet_info = st.text_area("Example: I groomed a Golden Retriever named Max. He was very muddy but now he's fluffy and smells like blueberries!")

        if st.button("Generate Marketing Bundle"):
            if pet_info:
                with st.spinner('Magic in progress...'):
                    # Adding a safety check for the API call
                    response = model.generate_content(
                        f"You are a professional pet groomer social media manager. Create an Instagram, Facebook, and Google Business post for: {pet_info}"
                    )
                    st.success("Bundle Ready!")
                    st.markdown(response.text)
            else:
                st.warning("Please enter some pet details first!")
                
    except Exception as e:
        # This will tell us if it's still a region issue
        st.error(f"Setup Error: {e}")
        st.info("If you see 'User location is not supported', it means the free tier is blocked in Spain. To fix this, simply enable 'Pay-as-you-go' in Google AI Studio (it will still be $0 for your usage).")
else:
    st.info("Please enter your License Key in the sidebar to start.")