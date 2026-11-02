from enum import StrEnum


class NotificationTypeEnum(StrEnum):
    EMAIL = "Email"
    BREVO_EMAIL = "BrevoEmail"
    RESEND_EMAIL = "ResendEmail"
    SMS = "SMS"
    WHATSAPP = "WhatsApp"
