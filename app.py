import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="Stealth Text Humanizer",
    page_icon="✍️",
    layout="centered"
)

# Custom Styling for clean UI
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; color: #1f2937; font-weight: 700; margin-bottom: 0.2rem; }
    .subtitle { font-size: 1rem; color: #4b5563; margin-bottom: 1.5rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">✍️ Stealth AI Humanizer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Bypass AI detectors with natural sentence restructuring and human-like flow.</p>', unsafe_allow_html=True)

# Sidebar for API Key & Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("Gemini API Key:", type="password", help="Apni free Google AI Studio API key yahan dalein.")
    st.markdown("---")
    st.markdown("### 💡 Tips for Best Results")
    st.markdown("- Ek baar mein 300-400 words ka text dalein.")
    st.markdown("- Output milne ke baad zaroorat ho toh minor tweaks karein.")

# Main Input Area
user_text = st.text_area(
    "Apna AI-generated text yahan paste karein:",
    height=220,
    placeholder="Yahan text paste karein..."
)

# Humanize Button Logic
if st.button("Humanize Text 🚀", type="primary", use_container_width=True):
    if not api_key_input:
        st.warning("⚠️ Kripya sidebar mein apni Gemini API Key darj karein!")
    elif not user_text.strip():
        st.warning("⚠️ Kripya text box mein kuch text likhein ya paste karein!")
    else:
        try:
            # Configure Gemini API safely
            genai.configure(api_key=api_key_input)
            
            # Using stable flash model for fast execution
            model = genai.GenerativeModel('gemini-pro')
            
            # Anti-AI Detection System Prompt
            system_prompt = """You are an expert human content writer and anti-AI detection specialist. Your task is to rewrite the provided text so that it completely bypasses all AI detectors (like GPTZero, Turnitin, Copyleaks) while keeping the original meaning intact. 
            
            Follow these strict rules while rewriting:
            1. Break Predictable Patterns: Vary sentence lengths drastically—mix very short sentences with longer, complex ones.
            2. Change Structure & Voice: Actively switch between active and passive voice. Rearrange clauses so the flow mimics natural human thinking.
            3. Use Human Nuance: Introduce natural conversational phrasing and remove robotic buzzwords like 'delve', 'testament', 'furthermore', 'in conclusion'.
            4. Maintain the Core Fact: Do not change the factual meaning of the original text, only change how it is expressed.
            
            Here is the text to humanize:
            """
            
            full_prompt = system_prompt + "\n" + user_text
            
            with st.spinner("🔄 Text ko humanize kiya ja raha hai..."):
                response = model.generate_content(full_prompt)
                
            if response and response.text:
                st.success("✨ Humanized Text Tayar Hai:")
                st.code(response.text, language="markdown")
            else:
                st.error("❌ AI se proper response nahi mila. Dobara koshish karein.")
                
        except Exception as e:
            st.error(f"❌ Error aa gaya: {str(e)}")
