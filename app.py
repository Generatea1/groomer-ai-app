import streamlit as st
from google import genai

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")

st.title("🐾 GroomerAI Pro")
st.write("Luxury marketing suite for busy pet salons.")

# --- SIDEBAR ---
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- MAIN LOGIC ---
if api_key:
    try:
        # Initialize the Client
        client = genai.Client(api_key=api_key)
        
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
                    # THE FIX: We use 'gemini-1.5-flash' which is the global standard.
                    # If this fails, the fallback is 'gemini-1.5-flash-002'
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=f"Act as a luxury pet spa marketing manager. Create a social media bundle for: {pet_info}. Include a headline, Instagram caption, and 10 hashtags."
                    )
                    
                    st.divider()
                    st.success("Bundle Ready!")
                    st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
        st.info("COACH TIP: If the 404 persists, go to Google AI Studio, create a BRAND NEW API Key, and try that one. Sometimes old keys are locked to retired model versions.")
else:
    st.info("Enter your API Key in the sidebar to start.")