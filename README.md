Initial commit - Email Extraction System

# Email Extraction System

## Overview

Email Extraction System is a Python-based project that extracts important information from Gmail emails using the IMAP protocol.

The system automatically retrieves and parses email data such as sender details, subject, date, greeting, body content, signature, and attachments.

## Features

* Sender Name Extraction
* Sender Email Extraction
* Subject Extraction
* Date Extraction
* Greeting Detection
* Email Body Extraction
* Signature Detection
* Attachment Detection
* JSON Output Generation

## Technologies Used

* Python
* IMAP
* Email Package
* JSON

## Sample Output

```json
{
  "sender_name": "Duolingo",
  "sender_email": "hello@duolingo.com",
  "subject": "Practice English Today?",
  "attachments": []
}
```

## Project Structure

```
Email-Extraction-System/
│
├── gmail extract.py
├── email data.json
└── README.md
```

## Future Improvements

* Email Classification
* CSV Export
* Database Storage
* Streamlit Web Interface

## Author

Pavani
