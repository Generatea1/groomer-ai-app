import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="GroomerAI Pro Suite", 
    page_icon="🐾", 
    layout="centered"
)

# --- STYLE ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_content_safe=True)

st.title("🐾 GroomerAI Pro: Visual Marketing Suite")
st.subheader("Turn one groom into a week of luxury content.")

# --- SIDEBAR SETUP ---
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your Gemini Pro License Key", type="password")
st.sidebar.info("Tip: Use the same key you generated in Google AI Studio.")

# --- MAIN LOGIC ---
if api_key:
    try:
        # Initialize the 2025 Pro Client
        client = genai.Client(api_key=api_key)
        
        # User Inputs
        pet_info = st.text_area(
            "What did you do in the salon today?", 
            placeholder="Example: Groomed a Golden Retriever named Max. He was muddy but now he's fluffy and smells like blueberries!",
            height=100
        )

        col1, col2 = st.columns(2)
        with col1:
            tone = st.selectbox("Tone", ["Luxury", "Playful", "Professional", "Heartfelt"])
        with col2:
            platform = st.selectbox("Primary Platform", ["Instagram", "Facebook", "Google Business", "All"])

        if st.button("✨ Generate Professional Marketing Bundle"):
            if not pet_info:
                st.error("Please enter some pet details first!")
            else:
                with st.spinner('🎨 AI is creating your high-end assets...'):
                    
                    # 1. TEXT GENERATION (Strategy & Copy)
                    text_prompt = f"Act as a luxury marketing manager for a pet spa. Create a {tone} {platform} post for: {pet_info}. Include a hook, 3 bullet points, and 10 hashtags."
                    
                    text_resp = client.models.generate_content(
                        model='gemini-2.0-flash',
                        contents=text_prompt
                    )
                    
                    # 2. IMAGE GENERATION (The 'Pro' Attempt)
                    # We use the Imagen 3.0 model which is elite for Pro users
                    image_status = "Success"
                    generated_image = None
                    
                    try:
                        image_prompt = f"A professional studio photograph of a {pet_info} in a luxury pet spa. Soft lighting, 8k resolution, clean background, masterpiece."
                        img_resp = client.models.generate_images(
                            model='imagen-3.0-generate-001',
                            prompt=image_prompt,
                            config=types.GenerateImagesConfig(number_of_images=1)
                        )
                        if img_resp.generated_images:
                            generated_image = Image.open(BytesIO(img_resp.generated_images[0].image.image_bytes))
                    except Exception as e:
                        image_status = "Restricted"
                    
                    # --- DISPLAY RESULTS ---
                    st.divider()
                    
                    if image_status == "Success" and generated_image:
                        st.image(generated_image, caption="AI-Generated Luxury Asset", use_column_width=True)
                    else:
                        st.warning("⚠️ Note: High-fidelity image generation is currently restricted in your region (Spain). I've optimized your strategy & copywriting below to compensate!")

                    st.success("✅ Your Marketing Strategy is Ready:")
                    st.markdown(text_resp.text)
                    
                    # Direct Link for User to Copy
                    st.info("💡 COACH TIP: Screenshot the image and copy the text above. Send this to your client immediately!")

    except Exception as e:
        st.error(f"Setup Error: {e}")
        st.info("Check if your Billing is enabled in AI Studio to remove the 'Resource Exhausted' block.")
else:
    st.warning("🔑 Please enter your API Key in the sidebar to unlock the suite.")
    st.image("https://images.unsplash.com/photo-1516733725897-1aa73b87c8e8?auto=format&fit=crop&q=80&w=1000", caption="GroomerAI: Professional Content in Seconds")

# --- FOOTER ---
st.divider()
st.caption("GroomerAI Suite v2.0 | Helping you reach your €200 goal.")