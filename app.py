import streamlit as st
from google import genai

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GroomerAI Pro Suite", 
    page_icon="🐾", 
    layout="centered"
)

# --- STYLE ---
# FIX: Changed 'unsafe_content_safe' to 'unsafe_allow_html'
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        height: 3em; 
        background-color: #4CAF50; 
        color: white; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🐾 GroomerAI Pro: Content Suite")
st.subheader("Luxury marketing for high-end pet salons.")

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

        if st.button("✨ Generate Luxury Marketing Bundle"):
            if not pet_info:
                st.error("Please enter some details first!")
            else:
                with st.spinner('🎨 Creating your luxury assets...'):
                    
                    # Using 1.5-Flash for maximum speed and regional stability in Spain/UK
                    prompt = f"""
                    Act as a high-end luxury marketing manager for a celebrity pet spa. 
                    Based on this groom: {pet_info}
                    
                    Provide the following in a professional, clear format:
                    1. THE 'GOLDEN HOOK': A headline for the post.
                    2. LUXURY INSTAGRAM CAPTION: (Polished and elite).
                    3. THE 'VISUAL PROMPT': A description of exactly what photo the groomer should take or generate to match this post.
                    4. 10 HIGH-PERFORMANCE HASHTAGS.
                    """
                    
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=prompt
                    )
                    
                    st.divider()
                    st.success("✅ Your Content Bundle is Ready:")
                    st.markdown(response.text)
                    
                    st.info("💡 COACH TIP: Copy the text above and send it to your client. You are selling them the *time* they save by not having to think of what to write!")

    except Exception as e:
        st.error(f"Setup Error: {e}")
else:
    st.warning("🔑 Please enter your API Key in the sidebar to unlock the suite.")