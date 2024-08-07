# Email Sender Script

## Overview

Send personalized HTML emails using `yagmail`, `pandas`, and `jinja2`. This script reads recipient details from a CSV file and sends custom emails based on an HTML template.

## Features

- Dynamic HTML content with Jinja2.
- Bulk email sending from a CSV file.
- Simple error handling.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/0xbassiouny1337/Email_sender.git
    cd Email_sender
    ```

2. **Set Up Virtual Environment (Optional):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip3 install -r requirements.txt
    ```

## Configuration

1. **Obtain Gmail App Password:**

    - Go to [Google Account Security](https://myaccount.google.com/security).
    - Ensure 2-Step Verification is enabled.
    - Under "App passwords," select "Generate app password."
    - Copy the generated password for use in your script.

2. **Update Script Settings:**

    Edit `email_sender.py`:

    ```python
    EMAIL = 'your-email@gmail.com'
    APP_PASSWORD = 'your-app-password'
    SUBJECT = 'Your Subject Here'
    HTML_TEMPLATE_PATH = './path-to-your-template.html'
    CSV_FILE = './path-to-your-csv-file.csv'
    ```

## Usage

1. **Prepare CSV File:**

    Ensure `email_list.csv` contains columns `email` and `name`.

    ```csv
    email,name
    recipient1@example.com,Name1
    recipient2@example.com,Name2
    ```

2. **Prepare HTML Template:**

    Create `temp.html` with Jinja2 placeholders.

    ```html
    <html>
    <body>
        <p>Dear {{ CANDIDATE_NAME }},</p>
        <p>Your trainee ID is {{ S_ID }}.</p>
    </body>
    </html>
    ```

3. **Run the Script:**

    ```bash
    python3 email_sender.py
    ```

## Requirements

- `yagmail`
- `pandas`
- `jinja2`

Listed in `requirements.txt`.

## License

MIT License - see the [LICENSE](LICENSE) file for details.
