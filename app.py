import streamlit as st
from google import genai

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GroomerAI Pro Suite", 
    page_icon="🐾", 
    layout="centered"
)

# --- STYLE ---
# FIXED: Changed 'unsafe_content_safe' to 'unsafe_allow_html'
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐾 GroomerAI Pro: Content Suite")
st.subheader("High-end marketing for busy pet salons.")

# --- SIDEBAR SETUP ---
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your Gemini License Key", type="password")

# --- MAIN LOGIC ---
if api_key:
    try:
        # Initialize the 2025 Client
        client = genai.Client(api_key=api_key)
        
        pet_info = st.text_area(
            "What happened in the salon today?", 
            placeholder="Groomed a Golden Retriever named Max. He was muddy but now he's fluffy!",
            height=100
        )

        if st.button("✨ Generate Marketing Bundle"):
            if not pet_info:
                st.error("Please enter some details first!")
            else:
                with st.spinner('🎨 Creating your luxury assets...'):
                    
                    # Optimized prompt for Spain/UK regional stability
                    prompt = f"""
                    Act as a luxury marketing manager for a pet spa. 
                    Based on this groom: {pet_info}
                    Provide:
                    1. A LUXURY INSTAGRAM CAPTION.
                    2. AN ENGAGING FACEBOOK POST.
                    3. A 'VISUAL AI PROMPT' (A description the user can use to generate a matching image).
                    4. 10 HIGH-PERFORMANCE HASHTAGS.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=prompt
                    )
                    
                    st.divider()
                    st.success("✅ Your Content Bundle is Ready:")
                    st.markdown(response.text)
                    
                    st.info("💡 COACH TIP: Copy the 'Visual AI Prompt' above and use it in a free image generator to show your client the full potential!")

    except Exception as e:
        st.error(f"Setup Error: {e}")
else:
    st.warning("🔑 Please enter your API Key in the sidebar to unlock the suite.")