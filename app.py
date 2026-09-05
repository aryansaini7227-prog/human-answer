import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="Stealth Text Humanizer",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Stealth AI Humanizer")
st.write("Bypass AI detectors with natural sentence restructuring.")

# Sidebar for API Key
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("Gemini API Key:", type="password", help="Apni Google AI Studio API key yahan dalein.")

# Main Input Area
user_text = st.text_area("Apna AI-generated text yahan paste karein:", height=200, placeholder="Yahan text dalein...")

if st.button("Humanize Text 🚀", type="primary"):
    if not api_key_input:
        st.warning("⚠️ Kripya sidebar mein apni Gemini API Key darj karein!")
    elif not user_text.strip():
        st.warning("⚠️ Kripya text box mein kuch text likhein!")
    else:
        try:
            # Configure Gemini API
            genai.configure(api_key=api_key_input.strip())
            
            # Using the stable model name
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            system_prompt = """You are an expert human content writer and anti-AI detection specialist. Your task is to rewrite the provided text so that it completely bypasses all AI detectors while keeping the original meaning intact. 
            
            Follow these strict rules while rewriting:
            1. Break Predictable Patterns: Vary sentence lengths drastically.
            2. Change Structure & Voice: Switch between active and passive voice.
            3. Use Human Nuance: Introduce natural conversational phrasing and remove robotic buzzwords like 'delve', 'testament', 'furthermore'.
            4. Maintain the Core Fact: Do not change the factual meaning of the original text.
            
            Here is the text to humanize:
            """
            
            full_prompt = system_prompt + "\n" + user_text
            
            with st.spinner("🔄 Text ko humanize kiya ja raha hai..."):
                response = model.generate_content(full_prompt)
                
            if response and response.text:
                st.success("✨ Humanized Text Tayar Hai:")
                st.write(response.text)
            else:
                st.error("❌ Response generate nahi ho paya.")
                
        except Exception as e:
            st.error(f"❌ Error details: {str(e)}")
