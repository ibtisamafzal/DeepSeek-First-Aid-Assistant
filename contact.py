import streamlit as st

def contact_page():
    st.title("📧 Contact Us")
    st.write("Have questions or feedback? Reach out to us!")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for contacting us! We'll get back to you soon.")