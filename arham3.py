import streamlit as st
import smtplib

# Function to send email
def send_email(subject, body):
    # SMTP configuration
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    receiver_email = 'recipient_email@example.com'
    password = 'your_email_password'
    
    # Create SMTP server connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)
    
    # Construct email message
    message = f"Subject: {subject}\n\n{body}"
    
    # Send email
    server.sendmail(sender_email, receiver_email, message)
    
    # Close SMTP server connection
    server.quit()

# Define Streamlit app
def main():
    st.title('Food Order Website')

    # Render the home page
    if st.button('Home'):
        st.write('Welcome to the Food Order Website!')

    # Render the order page
    if st.button('Order'):
        st.write('Place your order here:')
        # Process the order and send email
        send_email("New Food Order", "A new food order has been placed.")
        st.success('Your order has been placed successfully!')

# Run the Streamlit app
if __name__ == '__main__':
    main()


