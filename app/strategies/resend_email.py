import httpx

from app.core.settings import env_variables
from app.models.entities.template import Template
from app.models.requests.notification_request import ResendEmailNotificationRequest
from app.strategies.base import NotifierStrategy, render_template


class ResendEmailStrategy(NotifierStrategy[ResendEmailNotificationRequest]):
    def apply_template(
        self, request: ResendEmailNotificationRequest, template: Template
    ) -> ResendEmailNotificationRequest:
        return request.model_copy(
            update={
                "email_body": render_template(
                    template.body, template, request.template_variables
                ),
                "subject": render_template(
                    template.subject, template, request.template_variables
                ),
            }
        )

    async def send_notification(self, request: ResendEmailNotificationRequest) -> None:
        if request.subject is None or request.email_body is None:
            raise ValueError("email_body and subject are required to send an email")

        async with httpx.AsyncClient() as client:
            response = await client.post(
                env_variables.resend_api_url,
                headers={"Authorization": f"Bearer {request.resend_api_key}"},
                json={
                    "from": request.resend_from,
                    "to": [request.recipient_email],
                    "subject": request.subject,
                    "html": request.email_body,
                },
            )
            response.raise_for_status()
