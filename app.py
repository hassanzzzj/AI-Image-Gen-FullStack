import streamlit as st
import requests
import random
from io import BytesIO

# 1. Page Configuration (Always at the top)
st.set_page_config(page_title="Cheetah AI | Ultra-Fast Gen", page_icon="🎨", layout="centered")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("🎨 Cheetah AI Image Generator")
st.markdown("Enter your imagination below and let AI create a masterpiece for you. **No limits, no cost.**")

# 2. User Input Section
prompt = st.text_input("Describe your image:", placeholder="e.g. A futuristic city under a violet sky, cinematic lighting...")

def get_image_url(user_prompt):
    # Professional Prompt Engineering
    quality_tags = "8k resolution, highly detailed, professional photography, masterpiece, unreal engine 5, cinematic lighting"
    full_prompt = f"{user_prompt}, {quality_tags}"
    
    # Random seed for variety on every click
    seed = random.randint(0, 9999999)
    
    # Updated Pollinations URL with Flux Model for highest quality
    # We use .replace() to make the prompt URL-friendly
    encoded_prompt = requests.utils.quote(full_prompt)
    image_url = f"https://pollinations.ai/p/{encoded_prompt}?width=1024&height=1024&seed={seed}&model=flux"
    
    return image_url

# 3. Generation Logic
if st.button("Generate Magic ✨"):
    if not prompt:
        st.warning("⚠️ Please enter a prompt first!")
    else:
        with st.spinner("🚀  AI is crafting your image..."):
            try:
                target_url = get_image_url(prompt)
                response = requests.get(target_url)
                
                if response.status_code == 200:
                    # Displaying the image
                    st.image(response.content, caption=f"Generated: {prompt}", use_container_width=True)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download This Masterpiece",
                        data=response.content,
                        file_name=f"Hassan_ai_{random.randint(100,999)}.png",
                        mime="image/png"
                    )
                else:
                    st.error("❌ AI Server is busy. Please try again in a moment.")
            
            except Exception as e:
                st.error(f"⚠️ Connection Error: {str(e)}")

# 4. Footer
st.markdown("---")
st.caption("🚀 **Hassan's AI** | Powered by Flux Model via Pollinations.ai | 2026 Edition")