import smtplib
from email.message import EmailMessage
from config import (
    SENDER_EMAIL,
    RECIPIENT_EMAIL,
    APP_PASSWORD
)


def send_email(new_internships):

    if len(new_internships) == 0:

        print(
            "No new internships found."
        )

        return

    body = "New Internships Found\n\n"

    for internship in new_internships:

        body += (
            f"Company: {internship['company']}\n"
        )

        body += (
            f"Role: {internship['role']}\n"
        )

        body += (
            f"Location: {internship['location']}\n"
        )

        body += (
            f"Link: {internship['link']}\n"
        )

        body += (
            "\n----------------\n\n"
        )

    msg = EmailMessage()

    msg["Subject"] = (
        "New Internship Alert"
    )

    msg["From"] = SENDER_EMAIL

    msg["To"] = RECIPIENT_EMAIL

    msg.set_content(body)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            SENDER_EMAIL,
            APP_PASSWORD
        )

        smtp.send_message(msg)

    print(
        "Email sent successfully!"
    )
