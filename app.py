import streamlit as st
import requests
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

if st.button("Generate Image ✨"):
    if not prompt:
        st.warning("Enter Prompt First!")
    else:
        with st.spinner("AI is doing a Magic..."):
            try:
                # Pollinations AI ki simple URL structure
                # Format: https://image.pollinations.ai/prompt/{prompt}?width={w}&height={h}&seed={s}
                encoded_prompt = prompt.replace(" ", "%20")
                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&seed={seed}&nologo=true"
                
                # Image fetch karna
                response = requests.get(image_url)
                
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