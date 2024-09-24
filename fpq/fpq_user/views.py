from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy

from fpq_core.views import FormView
from .forms import RegisterForm


class RegisterView(FormView):
    template_name = 'fpq_user/register.html'
    form_class = RegisterForm

    def _guest(self) -> bool:
        return False


class ResetPasswordView(PasswordResetView, SuccessMessageMixin):
    template_name = 'fpq_user/password_reset.html'
    email_template_name = 'fpq_user/password_reset_email.html'
    html_email_template_name = 'fpq_user/password_reset_email.html'
    success_url = reverse_lazy('fpq_user:password_reset_done')
    success_message = ('An email with instructions to reset your password has '
                       'been sent to %(email)s.')
    subject_template_name = 'fpq_user/password_reset_subject.txt'


@login_required
def signout(request: WSGIRequest) -> HttpResponsePermanentRedirect:
    logout(request)

    return redirect('fpq_core:index')
