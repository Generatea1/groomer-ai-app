import streamlit as st
from google import genai

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GroomerAI Pro", 
    page_icon="🐾"
)

# --- CLEAN UI ---
st.title("🐾 GroomerAI Pro")
st.write("Luxury marketing for busy pet salons.")

# --- SIDEBAR ---
api_key = st.sidebar.text_input("Enter Gemini License Key", type="password")

# --- MAIN LOGIC ---
if api_key:
    try:
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
                    prompt = f"""
                    Act as a high-end luxury marketing manager for a pet spa. 
                    Based on: {pet_info}
                    Provide:
                    1. THE GOLDEN HOOK
                    2. LUXURY INSTAGRAM CAPTION
                    3. VISUAL PROMPT FOR AI IMAGES
                    4. 10 HASHTAGS
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=prompt
                    )
                    
                    st.divider()
                    st.success("Bundle Ready!")
                    st.write(response.text)

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Enter your API Key in the sidebar to start.")