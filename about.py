import streamlit as st

def about_page():
    st.title("🌍 About Us")
    st.write("Learn more about the vision, mission, and team behind GenAI-Innovators. 🌍📰")

    st.header("🌟 Our Vision")
    st.write("At GenAI-Innovators, we aim to revolutionize the way AI-driven solutions are created and consumed. By leveraging cutting-edge Generative AI, we aspire to provide reliable, real-time, and personalized content that empowers individuals and organizations worldwide. We envision a world where technology enhances the accessibility and quality of information for everyone.")

    st.header("🚀 Our Mission")
    st.write("Our mission is simple: to deliver AI-powered solutions that make content creation faster, smarter, and more efficient. We believe in innovation, creativity, and the potential of AI to transform industries. Whether you're a developer, an organization, or just someone seeking personalized content, GenAI-Innovators is here to serve your needs with accuracy, diversity, and creativity.")

    st.header("Meet the Team")
    
    # Team Member 1
    st.subheader("Muhammad Khaqan Nasir")
    st.write("Pursuing a BSCS (5th semester) at COMSATS University, Sahiwal Campus, specializing in full-stack web development and generative AI. I focus on creating user-centric solutions using modern technologies to solve real-world problems.")
    st.write("Driven by a passion for innovation, I specialize in leveraging AI to design efficient, scalable systems and stay at the forefront of web development.")
    st.markdown("[GitHub](https://github.com/khaqan-nasir) | [LinkedIn](https://www.linkedin.com/in/khaqan-nasir/)")
    st.markdown("[Email](mailto:khaqannasir01@gmail.com)")

    # Team Member 2
    st.subheader("Adnan Tariq")
    st.write("A Generative AI enthusiast, currently pursuing a Bachelor's of Computer Science at COMSATS University Islamabad, Sahiwal Campus.")
    st.write("As a mentee in the prestigious **Code in Place** program ([Stanford](https://codeinplace.stanford.edu/cip4/certificate/tmt0m3)), I have gained invaluable insights into programming and innovation under the mentorship of experts.")
    st.write("I am also an **Oracle Certified Generative AI Professional** ([Certificate](https://catalog-education.oracle.com/ords/certview/sharebadge?id=9ABDF2C83D619C2D6FAF456FCF35F4B47DCE20E4A6317D111639205958FCF826)), showcasing my commitment to excelling in the tech industry.")
    st.markdown("[GitHub](https://github.com/adnan-tariq) | [LinkedIn](https://www.linkedin.com/in/adnan-tariq/)")
    st.markdown("[Email](mailto:adnantariq966@gmail.com)")

    # Team Member 3
    st.subheader("Muhammad Ibtisam Afzal")
    st.write("I'm a third-year Computer Science undergrad, passionate about AI research and development, focusing on creating innovative AI solutions using cutting-edge technologies.")
    st.write("With a keen interest in artificial intelligence, I actively participate in international hackathons. I enjoy exploring the intersection of AI and design, from crafting data-driven applications to deploying models on accessible platforms like Streamlit. My goal is to make AI more impactful and user-friendly for everyone.")
    st.markdown("[GitHub](https://github.com/ibtisiam-afzal) | [LinkedIn](https://www.linkedin.com/in/ibtisiam-afzal/)")
    st.markdown("[Email](mailto:chaudhryibtisam2003@gmail.com)")

    st.header("🛠️ Technology Stack")
    st.write("Our app uses cutting-edge Generative AI models combined with open-source tools to ensure high-quality performance. Below are some key technologies that power GenAI-Innovators:")
    st.write("- **Streamlit**: For building the user interface.")
    st.write("- **Natural Language Processing (NLP)**: For generating accurate and readable content.")
    st.write("- **Free APIs and Open-Source Models**: To make the app cost-efficient and widely accessible.")
    st.write("- **Python Libraries**: For seamless backend integration and feature enhancement.")

    st.header("💡 Why Choose Us?")
    st.write("- **Free and Accessible**: We use free resources to ensure accessibility for all users.")
    st.write("- **Real-Time Content**: Generate fresh, personalized content in seconds.")
    st.write("- **Innovative AI**: Powered by state-of-the-art generative AI.")
    st.write("- **User-Centric Design**: Intuitive and simple to use for anyone.")

    st.header("🚀 Are You Ready to Join Us on the Next Hackathon?")
    st.write("Let’s collaborate and create groundbreaking projects together. Be part of an exciting journey where innovative ideas transform into impactful realities that shape the future! 🚀")
    if st.button("Join Us"):
        st.write("Contact us to join our next hackathon!")

    st.markdown("---")
    st.write("Copyright @2024, [GenAI-Innovators](https://github.com/GenAI-Innovators) All Rights Reserved.")
    st.write("Crafted with ❤️")
