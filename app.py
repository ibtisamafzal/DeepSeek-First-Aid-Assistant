import streamlit as st
import os
from dotenv import load_dotenv
import pycountry
from home import home_page
from about import about_page
from contact import contact_page

# Load environment variables
load_dotenv()

# UI Setup
st.set_page_config(page_title="DeepSeek First-Aid Assistant", page_icon="🚑", layout="wide")

# Sidebar Navigation
with st.sidebar:
    st.title("🌐 Navigation")
    page = st.radio("Go to", ["Home", "About", "Contact Us"])

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

# Load the selected page
if page == "Home":
    home_page(country_name)
elif page == "About":
    about_page()
elif page == "Contact Us":
    contact_page()