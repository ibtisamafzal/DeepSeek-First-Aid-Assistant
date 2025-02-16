import streamlit as st
import os
from dotenv import load_dotenv
import pycountry
from utils.api_utils import initialize_huggingface_client
from utils.emergency_utils import get_emergency_numbers
from utils.youtube_utils import get_youtube_video

# Load environment variables
load_dotenv()

# Initialize Hugging Face client
client = initialize_huggingface_client()

# UI Setup
st.set_page_config(page_title="DeepSeek First Aid Assistant", page_icon="🚑", layout="wide")

# Sidebar
with st.sidebar:
    st.title("ℹ️ About the App")
    st.write("This AI-powered assistant provides first-aid guidance based on symptoms you describe.")
    st.write("- Uses AI to analyze conditions\n- Suggests first aid actions\n- Finds relevant YouTube tutorials")
    st.write("⚠️ Always call emergency services for severe cases.")
    country_input = st.text_input("🌍 Enter Your Country (Optional):")
    country_name = None
    if country_input:
        country = pycountry.countries.get(name=country_input.title())
        if country:
            country_name = country.name
        else:
            st.warning("Could not recognize the country. Please check spelling.")

st.title("🚑 DeepSeek First Aid Assistant")

# User Input
condition = st.text_area("Describe the medical condition or symptoms:")

if st.button("Get First Aid") and condition:
    try:
        st.subheader("🆘 Analysis & First Aid Recommendations")
        prompt = f"""
        Analyze the following medical condition or symptoms and provide:
        - **Possible medical condition**
        - **Severity level**: Mild, Moderate, or Severe
        - **Immediate first-aid steps** (clear, structured bullet points)
        - **What NOT to do** (critical mistakes to avoid)
        - **When to seek medical help**
        
        Symptoms: {condition}
        """
        
        with st.spinner("Analyzing symptoms and generating recommendations..."):
            response = client.text_generation(
                prompt=prompt,
                max_new_tokens=300,
                temperature=0.3,
                top_p=0.9
            )
        
        # Display structured first aid recommendations with enhanced visuals
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
            font-weight: bold;
        }
        .medium-font {
            font-size:16px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<p class="big-font">✅ First Aid Steps:</p>', unsafe_allow_html=True)
        # Split the response into lines and display each line as a bullet point
        steps = response.split("\n")
        for step in steps:
            if step.strip():  # Ensure the line is not empty
                st.markdown(f"- {step.strip()}")

        # Show YouTube Video
        st.subheader("📹 Instructional Video")
        video_url = get_youtube_video(condition)
        if video_url:
            st.video(video_url)
        else:
            st.write("No relevant video found.")

        # Emergency Contact Information
        st.subheader("☎️ Emergency Contacts")
        if country_name:
            emergency_info = get_emergency_numbers(country_name)
            for service, number in emergency_info.items():
                st.write(f"- **{service}**: {number}")
        else:
            st.write("🌍 Enter your country in the sidebar to get local emergency numbers.")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("If this is a life-threatening emergency, please call emergency services immediately.")

# Important Disclaimers
st.markdown("---")
st.markdown("""
⚠️ **IMPORTANT DISCLAIMERS:**
- This is an AI-assisted tool and should not replace professional medical help
- In case of a serious emergency, call your country's emergency services
- Follow official first aid guidelines from authorized sources
- When in doubt, seek professional medical assistance
""")

# Add a clear emergency call button
if country_name and "Emergency Services" in get_emergency_numbers(country_name):
    emergency_number = get_emergency_numbers(country_name)["Emergency Services"]
    if st.button(f"🚨 CALL {emergency_number} NOW", use_container_width=True):
        st.error(f"Please exit this app and dial {emergency_number} immediately on your phone!")

# Add a link to the GitHub repository
st.markdown("---")
st.markdown("[GitHub Repository](https://github.com)")