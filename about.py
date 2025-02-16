import streamlit as st
import os
import base64

def encode_image(image_path):
    """Encode image to base64 string"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return ""

def about_page():
    """About page content and layout"""
    # Apply Poppins font across the app
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], * {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # Add Font Awesome CDN for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>About Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; text-align: center; color: gray;'>Learn more about the vision, mission, and team behind DeepSeek First-Aid Assistant. 🚑</p>", unsafe_allow_html=True)

    # Section 1: Our Vision
    st.markdown("<h2 style='font-size: 30px;'>🌟 Our Vision</h2>", unsafe_allow_html=True)
    st.write("""
    At **DeepSeek First-Aid Assistant**, we aim to revolutionize emergency response and first-aid guidance. 
    By leveraging cutting-edge **AI technology**, we aspire to provide **reliable, immediate, and personalized first-aid information** that can help save lives worldwide. 
    We envision a world where everyone has access to instant, accurate first-aid guidance when they need it most.
    """)

    # Section 2: Our Mission
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>🚀 Our Mission</h2>", unsafe_allow_html=True)
    st.write("""
    Our mission is clear: to deliver **AI-powered first-aid guidance** that is fast, reliable, and easy to understand. 
    We believe in leveraging technology to enhance emergency response and first-aid knowledge. Whether you're a healthcare professional, 
    first responder, or someone seeking immediate first-aid guidance, **DeepSeek First-Aid Assistant** is here to help with 
    **accuracy, clarity, and reliability**.
    """)

    # Team Section
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>👥 Meet the Team</h2>", unsafe_allow_html=True)
    
    team_members = [
        {
            "name": "Muhammad Khaqan Nasir",
            "role": "AI & Backend Developer",
            "bio": "Specializes in AI integration and backend development, focusing on making first-aid information accessible through technology.",
            "github": "khaqan-nasir",
            "linkedin": "khaqan-nasir",
            "email": "khaqannasir01@gmail.com",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member01.jpg')
        },
        {
            "name": "Adnan Tariq",
            "role": "ML Engineer & API Specialist",
            "bio": "Expert in machine learning models and API integration, ensuring accurate and reliable first-aid guidance.",
            "github": "adnan-tariq",
            "linkedin": "adnan-tariq",
            "email": "adnantariq966@gmail.com",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member02.JPG')
        },
        {
            "name": "Muhammad Ibtisam Afzal",
            "role": "Frontend & UX Developer",
            "bio": "Focuses on creating intuitive user interfaces and ensuring a seamless experience for emergency guidance.",
            "github": "ibtisiam-afzal",
            "linkedin": "ibtisiam-afzal",
            "email": "chaudhryibtisam2003@gmail.com",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member03.JPG')
        }
    ]

    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            # Encode image to base64
            encoded_image = encode_image(member['image'])
            
            # HTML structure with background color and adjusted image height
            st.markdown(f"""
            <div style='background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center;'>
                <div style='background-color: #ffffff; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; justify-content: center; align-items: center;'>
                    <img src="data:image/jpeg;base64,{encoded_image}" alt="{member['name']}" style='width: 100%; height: 100%; object-fit: cover; border-radius: 50%;'>
                </div>
                <div style='font-size: 22px; font-weight: 600; color: #5F6366; margin-top: 10px;'>{member['name']}</div>
                <div style='font-size: 16px; color: #6c757d; margin: 10px 0;'>{member['role']}</div>
                <div style='font-size: 14px; color: #6c757d; margin: 10px 0; min-height: 60px;'>{member['bio']}</div>
                <div style='margin-top: 15px;'>
                    <a href='https://github.com/{member["github"]}' target='_blank' style='font-size: 20px; color: #000000; margin-right: 10px;'>
                        <i class="fab fa-github"></i>
                    </a>
                    <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' style='font-size: 20px; color: #0077B5; margin-right: 10px;'>
                        <i class="fab fa-linkedin"></i>
                    </a>
                    <a href='mailto:{member["email"]}' style='font-size: 20px; color: #EA4335;'>
                        <i class="fas fa-envelope"></i>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Section 4: Technology Stack
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>🛠️ Technology Stack</h2>", unsafe_allow_html=True)
    st.write("""
    Our application leverages cutting-edge technologies to provide reliable first-aid guidance:
    - **DeepSeek AI**: For accurate symptom analysis and response generation
    - **Streamlit**: For building an intuitive user interface
    - **Python**: For robust backend processing and API integration
    - **YouTube Data API**: For finding relevant first-aid tutorial videos
    """)

    # Section 5: Why Choose Us?
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px;'>💡 Why Choose Us?</h2>", unsafe_allow_html=True)
    cols = st.columns(4)
    
    features = [
        ("Instant Response", "Get immediate first-aid guidance when you need it"),
        ("AI-Powered Analysis", "Accurate symptom analysis and recommendations"),
        ("Video Tutorials", "Access to relevant first-aid demonstration videos"),
        ("Location Aware", "Emergency contact information for your region")
    ]
    
    for col, (title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; height: 150px; text-align: center;'>
                <h3 style='font-size: 18px; color: #1a1a1a; margin-bottom: 10px;'>{title}</h3>
                <p style='font-size: 14px; color: #6c757d;'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # Important Notice
    st.markdown("---")
    st.markdown("<h2 style='font-size: 30px; text-align: center;'>⚠️ Important Notice</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color: #fff3cd; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;'>
        <p style='color: #856404; font-size: 16px;'>
            While we strive to provide accurate first-aid guidance, this app is not a substitute for professional medical care.
            Always call emergency services in severe cases and follow the advice of healthcare professionals.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center;">© 2024 DeepSeek First-Aid Assistant. All Rights Reserved.<br>Crafted with ❤️ for emergency preparedness</p>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    about_page()
