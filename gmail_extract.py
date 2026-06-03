from email.header import decode_header
from email.utils import parseaddr
import imaplib
import email

def decode_email_header(header):
    if not header:
        return ""
    decoded_parts = decode_header(header)
    decoded_string = ""

    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            decoded_string += part.decode(encoding or "utf-8", errors="ignore")
        else:
            decoded_string += part
    return decoded_string

# Gmail Details
EMAIL = "pavanipavani3116@gmail.com"
PASSWORD = "xcdy hvcz jfvf wpxl"

# Connect Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)

print("Login Successful")

# Open Inbox
mail.select("inbox")

# Get all email ids
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()

print("Total Emails :", len(email_ids))

# Latest Email
latest_email_id = email_ids[-1]

status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

raw_email = msg_data[0][1]

msg = email.message_from_bytes(raw_email)

# Decode Subject
subject = msg["Subject"]

decoded_subject, encoding = decode_header(subject)[0]

if isinstance(decoded_subject, bytes):
    subject = decoded_subject.decode(
        encoding if encoding else "utf-8"
    )

# Extract Body
from bs4 import BeautifulSoup

body = ""

for part in msg.walk():

    content_type = part.get_content_type()

    if content_type == "text/html":

        html = part.get_payload(decode=True)

        if html:

            soup = BeautifulSoup(html, "html.parser")

            body = soup.get_text(separator="\n", strip=True)

            break

# Extract Attachments
attachments = []

for part in msg.walk():

    filename = part.get_filename()

    if filename:
        attachments.append(filename)

# Final Output
print("\n===== EXTRACTED EMAIL =====\n")

print("FROM:")
print(msg["From"])

print("\nTO:")
print(msg["To"])

print("\nSUBJECT:")
print(subject)

print("\nDATE:")
print(msg["Date"])

print("\nBODY:")
print(body[:1000])

#GREETING EXTRACTION
greeting = ""

for line in body.split("\n"):
    line = line.strip()
    if line.startswith("Hi"):
        greeting = line
        break
print("\nGREETING:")
print(greeting)

# SIGNATURE EXTRACTION
signature = ""
lines = body.split("\n")
for i, line in enumerate(lines):
    if line.strip() == "Shruthi":
        signature = "\n".join(lines[i:i+2])
        break

print("\nSIGNATURE:")
print(signature)

#CLEAN BODY
main_body = body
if "Shruthi" in body:
    main_body = body.split("Shruthi")[0]

main_body = main_body.replace("📅", "")
main_body = main_body.replace("💡", "")
main_body = main_body.replace("📄", "")
main_body = main_body.replace("💻", "")
main_body = main_body.replace("🧠", "")
main_body = main_body.replace("🎯", "")
main_body = main_body.replace("→", "")
main_body = main_body.replace("|", "")

# REMOVE SYMBOLS

main_body = main_body.replace("→", "")
main_body = main_body.replace("|", "")


#REMOVE FOOTER
main_body = main_body.replace("Unsubscribe", "")
main_body = main_body.replace("mx", "")
main_body = main_body.replace("crio\n.\ndo", "")

# REMOVE EMPTY LINES
lines = main_body.split("\n")

clean_lines = []

for line in lines:

    line = line.strip()

    if line != "":
        clean_lines.append(line)

main_body = "\n".join(clean_lines)


print("\nATTACHMENTS:")
print(attachments)

from email.utils import parseaddr
sender_name, sender_email = parseaddr(msg["From"])
sender_name = decode_email_header(sender_name)

# Store in Dictionary
email_data = {
    "sender_name": sender_name,
    "sender_email": sender_email,
    "to": msg["To"],
    "subject": subject,
    "date": msg["Date"],
    "greeting": greeting,
    "body": main_body,
    "signature": signature,
    "attachments": attachments
}

print("\nEMAIL DATA:")
print(email_data)

import json

with open("email_data.json", "w", encoding="utf-8") as file:
    json.dump(
    email_data,
    file,
    indent=4,
    ensure_ascii=False
)
