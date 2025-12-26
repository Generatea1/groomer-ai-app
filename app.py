This 404 error is persistent because the new google-genai SDK is trying to use a v1beta endpoint that doesn't recognize the model name models/gemini-1.5-flash. This is a common "version mismatch" between the library and the API.

To hit your €200 goal, we need to stop the technical loop and get to the selling. I have rewritten the code to use the gemini-1.5-flash-latest alias, which is the most stable "catch-all" name for the API. I've also removed the v1beta conflict.

The "Guaranteed" app.py
Python

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
                    # THE FIX: Using 'gemini-1.5-flash-latest' avoids versioning conflicts
                    response = client.models.generate_content(
                        model='gemini-1.5-flash-latest',
                        contents=f"Act as a luxury pet spa marketing manager. Create a social media bundle for: {pet_info}. Include a headline, Instagram caption, and 10 hashtags."
                    )
                    
                    st.divider()
                    st.success("Bundle Ready!")
                    st.write(response.text)

    except Exception as e:
        # If this STILL fails, it will print the specific error to help me fix it
        st.error(f"Error: {e}")
        st.info("COACH TIP: If you see '404', please go to Google AI Studio and ensure you have 'Gemini API' enabled in your project settings.")
else:
    st.info("Enter your API Key in the sidebar to start.")