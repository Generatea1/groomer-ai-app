import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="GroomerAI Pro", page_icon="🐾")

st.title("🐾 GroomerAI Pro")
st.write("Professional Marketing Suite for Pet Salons.")

# --- SIDEBAR ---
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# --- MAIN LOGIC ---
if api_key:
    try:
        # Step 1: Configure
        genai.configure(api_key=api_key)
        
        # Step 2: Initialize Model 
        # Using the standard production name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        pet_info = st.text_area(
            "What happened in the salon?", 
            placeholder="Groomed a Golden Retriever named Max...",
            height=150
        )

        if st.button("Generate Marketing Bundle"):
            if not pet_info:
                st.warning("Please enter some details.")
            else:
                with st.spinner('AI is generating your content...'):
                    # Step 3: Explicit call to the model
                    response = model.generate_content(
                        contents=f"Act as a luxury pet groomer's marketing assistant. Create a professional Instagram caption and 10 hashtags for: {pet_info}",
                        # Adding safety and configuration to bypass 'v1beta' issues
                        generation_config=genai.types.GenerationConfig(
                            candidate_count=1,
                            max_output_tokens=500,
                            temperature=0.7,
                        )
                    )
                    
                    st.divider()
                    st.success("✅ Content Ready!")
                    st.write(response.text)

    except Exception as e:
        # This will tell us if it's a regional block or a name block
        st.error(f"Error: {e}")
        st.info("COACH TIP: If the 404 persists, change the model line to: model = genai.GenerativeModel('gemini-1.5-flash-latest')")
else:
    st.info("Enter your API Key in the sidebar to start.")