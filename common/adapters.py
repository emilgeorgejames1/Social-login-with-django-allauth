from allauth.account import app_settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.signals import pre_social_login
from allauth.utils import get_user_model

from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import redirect

User = get_user_model()


class CustomLoginAccountAdapter(DefaultAccountAdapter):
    '''
    Overrides allauth.account.adapter.DefaultAccountAdapter.ajax_response to avoid changing
    the HTTP status_code to 400
    '''

    def get_login_redirect_url(self, request):
        """
        """
        if request.user.is_authenticated:
            return settings.LOGIN_REDIRECT_URL.format(
                id=request.user.id)
        else:
            return "/"


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    '''
    Overrides allauth.socialaccount.adapter.DefaultSocialAccountAdapter.pre_social_login to
    perform some actions right after successful login
    '''

    def pre_social_login(self, request, sociallogin):
        pass


@receiver(pre_social_login)
def link_social_account_to_user(sender, request, sociallogin, **kwargs):
    """
    :param sender:
    :param request:
    :param sociallogin:
    :param kwargs:
    :return:
    """
    email_address = sociallogin.account.extra_data['email']
    users = User.objects.filter(email=email_address)
    if users:
        perform_login(request, users[0], email_verification=app_settings.EMAIL_VERIFICATION)
        raise ImmediateHttpResponse(redirect(settings.LOGIN_REDIRECT_URL.format(id=request.user.id)))
