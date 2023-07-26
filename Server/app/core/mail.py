import yagmail

from app.core.settings import settings

server = yagmail.SMTP(
    settings.MATHTRIX_EMAIL_ADDRESS,
    settings.MATHTRIX_EMAIL_PASSWORD,
    host="smtp.office365.com",
    port=587,
    smtp_starttls=True,
    smtp_ssl=False,
)


def send_email(
        target_email: list[str],
        subject: str,
        body: str,
        attachments: list[str] = [],
        cc: list[str] = [],
        bcc: list[str] = [],
):
    server.send(
        to=target_email,
        subject=subject,
        contents=body,
        attachments=[yagmail.inline(i) for i in attachments],
        cc=cc,
        bcc=bcc,
    )
