from unittest.mock import Mock
from lab4.main import User

class EmailService:
    def send_email(self, user: User, message: str):
        print(f"Sending email to {user.email}: {message}")

def test_email_service_mock():
    service = EmailService()
    service.send_email = Mock()

    user = User("Alice", "alice@example.com")
    service.send_email(user, "Welcome!")
    service.send_email.assert_called_once_with(user, "Welcome!")
