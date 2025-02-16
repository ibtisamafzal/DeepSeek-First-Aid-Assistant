import streamlit as st

def contact_page():
    """Contact page content and layout"""
    # Apply Poppins font across the app
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], * {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # Include Font Awesome CDN for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; text-align: center; color: gray;'>Need assistance or have feedback? We're here to help!</p>", unsafe_allow_html=True)

    # Emergency Notice
    st.markdown("""
    <div style='background-color: #f8d7da; padding: 20px; border-radius: 10px; margin-bottom: 30px;'>
        <h3 style='color: #721c24; font-size: 18px;'>⚠️ Emergency Notice</h3>
        <p style='color: #721c24;'>If you're experiencing a medical emergency, please contact emergency services immediately:</p>
        <ul style='color: #721c24;'>
            <li>Emergency Services: Call your local emergency number (e.g., 911 in the US)</li>
            <li>Poison Control: Contact your national poison control center</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Contact Form
    st.markdown("<h2 style='font-size: 30px;'>📬 Get in Touch</h2>", unsafe_allow_html=True)
    st.write("Have questions about our First-Aid Assistant? Fill out the form below:")

    cols = st.columns([2, 1])
    with cols[0]:
        contact_form = st.form(key='contact_form')
        name = contact_form.text_input("Your Name")
        email = contact_form.text_input("Your Email")
        category = contact_form.selectbox(
            "Inquiry Type",
            ["General Question", "Technical Support", "Feature Request", "Bug Report", "Other"]
        )
        message = contact_form.text_area("Your Message")
        submit_button = contact_form.form_submit_button("Send Message")
        
        if submit_button:
            if name and email and message:
                st.success("Thank you for reaching out! Our team will get back to you within 24 hours.")
            else:
                st.error("Please fill in all required fields.")

    with cols[1]:
        st.markdown("""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px;'>
            <h3 style='font-size: 20px;'>📞 Quick Contact</h3>
            <p><i class="fas fa-envelope"></i> Email: adnantariq966@gmail.com</p>
            <p><i class="fas fa-clock"></i> Response Time: Within 24 hours</p>
            <p><i class="fas fa-globe"></i> Available: 24/7 for emergency guidance</p>
        </div>
        """, unsafe_allow_html=True)

    # FAQ Section
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>❓ Frequently Asked Questions</h2>", unsafe_allow_html=True)
    
    faqs = {
        "Is this a replacement for emergency services?": 
            "No, our AI assistant is designed to provide first-aid guidance but is not a replacement for professional medical care. Always call emergency services in serious situations.",
        "How accurate is the first-aid guidance?": 
            "Our AI uses up-to-date medical information but should be used as a supplementary tool. Always follow official first-aid protocols and seek professional medical advice when needed.",
        "Can I use this internationally?": 
            "Yes, our service is available worldwide and provides location-specific emergency contact information when available.",
        "Is my medical information private?": 
            "Yes, we take privacy seriously. All interactions are confidential and we do not store personal medical information."
    }

    for question, answer in faqs.items():
        with st.expander(question):
            st.write(answer)

    # Team Availability
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>👥 Team Availability</h2>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    availability_info = [
        {
            "title": "Technical Support",
            "hours": "Monday - Friday: 9 AM - 5 PM",
            "icon": "fa-wrench"
        },
        {
            "title": "AI Assistant",
            "hours": "24/7 Availability",
            "icon": "fa-robot"
        },
        {
            "title": "Customer Service",
            "hours": "Monday - Sunday: 8 AM - 8 PM",
            "icon": "fa-headset"
        }
    ]

    for col, info in zip(cols, availability_info):
        with col:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center;'>
                <i class="fas {info['icon']}" style="font-size: 24px; color: #0077B5;"></i>
                <h3 style='font-size: 18px; margin: 10px 0;'>{info['title']}</h3>
                <p style='color: #6c757d;'>{info['hours']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Social Media Links
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>💬 Connect With Us</h2>", unsafe_allow_html=True)
    st.write("Follow us for the latest updates and first-aid tips:")

    social_media_links = {
        "GitHub": "https://github.com/ibtisamafzal/DeepSeek-First-Aid-Assistant",
        "LinkedIn": "https://www.linkedin.com/company/genai-innovators",
        "Website": "https://genai-innovators.netlify.app/"
    }

    for platform, link in social_media_links.items():
        st.markdown(f"""
        <a href='{link}' target='_blank' style='font-size: 20px; color: #0077B5; margin-right: 20px;'>
            <i class="fab fa-{platform.lower()}" style="font-size: 24px;"></i> {platform}
        </a>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center;">©2025 GenAI-Innovators. All Rights Reserved.<br>Providing AI-powered first-aid guidance with care ❤️</p>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    contact_page()
