import yagmail
import pandas as pd
from jinja2 import Template

class EmailSender:
    def __init__(self, email: str, app_password: str, subject: str, html_template_path: str):
        self.email = email
        self.app_password = app_password
        self.subject = subject
        self.html_template_path = html_template_path
        self.yag = yagmail.SMTP(email, app_password)

    def render_html(self, name: str, trainee_id: int):
        try:
            with open(self.html_template_path, 'r') as file:
                html_template = file.read()
            
            template = Template(html_template)
            html_content = template.render(CANDIDATE_NAME=name, S_ID=trainee_id)
            
            print(html_content)  # Add this line to print the rendered HTML
            return html_content
        except Exception as e:
            print(f"Failed to render HTML. Error: {str(e)}")
            return ""

    def send_email(self, recipient: str, name: str, trainee_id: int):
        try:
            html_content = self.render_html(name, trainee_id)
            if html_content:  # Check if HTML content was rendered successfully
                self.yag.send(
                    to=recipient,
                    subject=self.subject,
                    contents=[html_content]
                )
                print(f"Email sent to {recipient}.")
            else:
                print(f"Failed to render HTML for {recipient}.")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {str(e)}")

    def send_emails_from_csv(self, csv_file: str):
        try:
            df = pd.read_csv(csv_file)
            if 'email' not in df.columns or 'name' not in df.columns:
                print("CSV file must contain 'email' and 'name' columns.")
                return

            for index, row in df.iterrows():
                self.send_email(row['email'], row['name'], index + 1)
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
    # Variables for login and email details
    EMAIL = 'nourbassuni1@gmail.com'
    APP_PASSWORD = 'lhrh xhpz luhe wawm'  # Use the App Password generated
    SUBJECT = 'Congratulations on Your Acceptance!'
    HTML_TEMPLATE_PATH = './temp.html'  # Path to your HTML template
    CSV_FILE = './email_list.csv'  # Ensure this file exists in the same directory as the script

    # Initialize EmailSender
    email_sender = EmailSender(EMAIL, APP_PASSWORD, SUBJECT, HTML_TEMPLATE_PATH)
    
    # Send emails to recipients from the CSV file
    email_sender.send_emails_from_csv(CSV_FILE)

if __name__ == "__main__":
    main()
