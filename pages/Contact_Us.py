import smtplib
import streamlit as st
import ssl
import os


def send_email(sender_email, receiver_email, subject, message, username, password, host, port):
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # Login to the SMTP server
        server.login(username, password)

        # Construct the email message
        email_message = f"""Subject: {subject}\n\n
                                 From:{sender_email} \n
                                {message} """

        # Send the email
        server.sendmail(sender_email, receiver_email, email_message)


# Streamlit web form
st.title("Contact Me 📩")

# Email inputs
sender_email = st.text_input("Your Email")
subject = st.text_input("Subject")
message = st.text_area("Message")

# SMTP server configuration
host = "smtp.gmail.com"
port = 465
# Receiver email address
receiver_email = "mohammahhammadansari07@gmail.com"

# Password and username
# password = os.getenv("PASSWORD")
password="irvbbvusozrzonus"
username = "mohammadhammadansari07@gmail.com"

if st.button("Send Email"):
    # Call the send_email function with the provided inputs
    send_email(sender_email, receiver_email, subject, message, username, password, host, port)
    st.success("Email sent successfully 🎉")
