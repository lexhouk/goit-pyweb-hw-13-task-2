from smtplib import SMTP
from ssl import _create_unverified_context

from django.core.mail.backends.smtp import EmailBackend


class FpqEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        try:
            self.connection = SMTP(self.host, self.port, timeout=self.timeout)

            if self.use_tls:
                context = _create_unverified_context()
                self.connection.starttls(context=context)

            self.connection.login(self.username, self.password)
        except Exception:
            if not self.fail_silently:
                raise

            return False

        return True
