import yagmail
import pandas as pd
from jinja2 import Template
import time
import os

class EmailSender:
    def __init__(self, email: str, app_password: str, subject: str, html_template_path: str):
        self.email = email
        self.app_password = app_password
        self.subject = subject
        self.html_template_path = html_template_path
        self.yag = yagmail.SMTP(email, app_password)

    def render_html(self, name: str):
        try:
            with open(self.html_template_path, 'r') as file:
                html_template = file.read()
            
            time.sleep(0.2)
            template = Template(html_template)
            html_content = template.render(CANDIDATE_NAME=name)
            
            return html_content
        except Exception as e:
            print(f"Failed to render HTML. Error: {str(e)}")
            return ""

    def send_email(self, recipient: str, name: str, cert: str):
        try:
            html_content = self.render_html(name)
            if html_content:  # Check if HTML was rendered successfully
                attachments = []
                
                cert_path = f'./certs/{cert}'
                if os.path.exists(cert_path):
                    attachments.append(cert_path)
                    sleep(1)
                else:
                    print(f"Certificate file {cert_path} not found for {name}. Skipping attachment.")
                
                self.yag.send(
                    to=recipient,
                    subject=self.subject,
                    contents=[html_content],
                    attachments=attachments if attachments else None
                )
                print(f"Email sent to {recipient} with certificate: {cert if attachments else 'No certificate attached'}")
            else:
                print(f"Failed to render HTML for {recipient}.")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {str(e)}")

    def send_emails_from_csv(self, csv_file: str):
        try:
            df = pd.read_csv(csv_file)
            if 'email' not in df.columns or 'name' not in df.columns or 'cert' not in df.columns:
                print("CSV file must contain 'email', 'name', and 'cert' columns.")
                return

            counter = 0  
            for _, row in df.iterrows():
                self.send_email(row['email'], row['name'], row['cert'])
                counter += 1

                if counter % 20 == 0:
                    print("Reached 20 emails. Sleeping for 3 minutes to avoid Gmail blocking...")
                    time.sleep(180)  

                time.sleep(0.5)  
        except Exception as e:
            print(f"Failed to read CSV file. Error: {str(e)}")

def main():
    print ("""   ___       ____                _                         
  / _ \     |  _ \              (_)                        
 | | | |_  _| |_) | __ _ ___ ___ _  ___  _   _ _ __  _   _ 
 | | | \ \/ /  _ < / _` / __/ __| |/ _ \| | | | '_ \| | | |
 | |_| |>  <| |_) | (_| \__ \__ \ | (_) | |_| | | | | |_| |
  \___//_/\_\____/ \__,_|___/___/_|\___/ \__,_|_| |_|\__, |
                                                      __/ |
                                                     |___/ 
 """)
    print ("                Created BY 0xBassiouny         ")
    
    EMAIL = ''
    APP_PASSWORD = ''  # Use the App Password generated
    SUBJECT = 'Congratulations on Your Acceptance!'
    HTML_TEMPLATE_PATH = './temp.html'  # Path to your HTML template
    CSV_FILE = './email_list.csv'  # Ensure this file exists in the same directory as the script

    email_sender = EmailSender(EMAIL, APP_PASSWORD, SUBJECT, HTML_TEMPLATE_PATH)
    
    email_sender.send_emails_from_csv(CSV_FILE)

if __name__ == "__main__":
    main()
