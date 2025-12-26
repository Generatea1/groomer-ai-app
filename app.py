import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")

st.title("🐾 GroomerAI Pro")
st.write("Luxury marketing suite for high-end pet salons.")

# --- SIDEBAR ---
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- MAIN LOGIC ---
if api_key:
    try:
        # Initialize
        genai.configure(api_key=api_key)
        
        # FIX: We use the explicit model string. 
        # In some regions, 'gemini-1.5-flash' works, in others 'models/gemini-1.5-flash'.
        # We will try the most universal one.
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        pet_info = st.text_area(
            "Describe the groom today:", 
            placeholder="Groomed a Golden Retriever named Max. He smells like blueberries!",
            height=150
        )

        if st.button("Generate Marketing Bundle"):
            if not pet_info:
                st.warning("Please enter details.")
            else:
                with st.spinner('AI is working...'):
                    # Force a simple prompt to test connection
                    response = model.generate_content(
                        f"Write a luxury Instagram post for a pet groomer about: {pet_info}"
                    )
                    
                    st.divider()
                    st.success("Bundle Ready!")
                    st.write(response.text)

    except Exception as e:
        # If the 404 persists, this will help us see if it's a naming issue
        st.error(f"Error: {e}")
        st.info("COACH TIP: If you still see a 404, try replacing 'gemini-1.5-flash' with 'gemini-1.5-flash-latest' in the code.")
else:
    st.info("Enter your API Key in the sidebar to start.")