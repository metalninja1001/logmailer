import subprocess
import email, smtplib, ssl
import typer

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    subject = input(f"Please enter a subject: ")
    body = input(f"Please enter a short body: ")
    sender_email = input(f"Please enter the sending email address: ")
    receiver_email = input(f"Please enter the recipient email address: ")
    password = input(f"Please enter a password: ")
    port = input(f"Please enter a port: ")
    smtp_server = input(f"Please enter the smtp server address: ")
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    #message["Cc"] = md_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    with open('OUTPUT FILENAME', 'w') as f:
        subprocess.run(['tail', 'PATH TO LOGFILE'], stdout=f)
    filename = "OUTPUT FILENAME"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

if __name__ == "__main__":
    typer.run(main)
