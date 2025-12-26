import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")

st.title("🐾 GroomerAI Pro")
st.write("Luxury marketing suite for busy pet salons.")

# --- SIDEBAR ---
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- MAIN LOGIC ---
if api_key:
    try:
        # Initialize using the STABLE library
        genai.configure(api_key=api_key)
        
        # We use 'gemini-1.5-flash' which is the most stable name for this library
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        pet_info = st.text_area(
            "What happened today?", 
            placeholder="Groomed a Golden Retriever named Max...",
            height=150
        )

        if st.button("Generate Marketing Bundle"):
            if not pet_info:
                st.warning("Please enter some pet details.")
            else:
                with st.spinner('Creating your content...'):
                    prompt = f"Act as a luxury pet spa marketing manager. Create a social media bundle for: {pet_info}. Include a headline, Instagram caption, and 10 hashtags."
                    
                    response = model.generate_content(prompt)
                    
                    st.divider()
                    st.success("Bundle Ready!")
                    st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
        st.info("COACH TIP: If you see 'User location not supported', it means you need to enable 'Pay-as-you-go' in AI Studio (it will still be $0).")
else:
    st.info("Enter your API Key in the sidebar to start.")
