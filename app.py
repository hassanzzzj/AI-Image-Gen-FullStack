import streamlit as st
import requests
import random
from io import BytesIO

# Page Configuration
st.set_page_config(page_title="Free AI Image Gen", page_icon="🚀")

st.title("🚀 Unlimited Free AI Image Generator")
st.markdown("Enter your prompt and generate unlimited AI images for free.")

# User Input
prompt = st.text_input("Enter your prompt:", placeholder="A magical forest with neon mushrooms...")

# Styling options (Pollinations supports easy customization)
width = 1024
height = 1024
seed = 42 # Random seed for variety

def generate_image(prompt):
    # High quality keywords add karna
    enhanced_prompt = f"{prompt}, 8k, highly detailed, professional photography, cinematic lighting, masterpiece"
    
    # Random seed taake har baar naya result aaye
    seed = random.randint(0, 999999)
    
    # Pollinations AI URL with Flux model and 1024x1024 resolution
    image_url = f"https://pollinations.ai/p/{enhanced_prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&model=flux"
    
    return image_url
if st.button("Generate Image ✨"):
    if not prompt:
        st.warning("Enter Prompt First!")
    else:
        with st.spinner("AI is doing a Magic..."):
            try:
                # Pollinations AI ki simple URL structure
                # Format: https://image.pollinations.ai/prompt/{prompt}?width={w}&height={h}&seed={s}
                
                # Image fetch karna
                response = requests.get(generate_image(prompt))
                
                if response.status_code == 200:
                    # Image display karna
                    st.image(response.content, caption=f"Result for: {prompt}", width='stretch')
                    
                    # Download button
                    st.download_button(
                        label="Download Image",
                        data=response.content,
                        file_name="ai_image.png",
                        mime="image/png"
                    )
                else:
                    st.error("There was an error, try again.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.caption("Powered by Pollinations.ai | No Limits | No Credits")