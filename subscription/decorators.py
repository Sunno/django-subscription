from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings

SUBSCRIPTION_START_URL = getattr(settings, 'SUBSCRIPTION_START_URL', None)

def valid_helper(u):
    current = u.get_active_subscription()
    return current is not None and current.valid() and \
        not current.expired() and not current.cancelled

def subscription_required(function=None,
                          redirect_field_name=REDIRECT_FIELD_NAME,
                          subscription_url=SUBSCRIPTION_START_URL,
                          login_url=settings.LOGIN_URL):
    """Decorator for views that checks if the current user has
    *any* active subscription"""


    actual_decorator = user_passes_test(
        lambda u: (valid_helper(u) or u.is_coach or u.is_superuser),
        login_url=subscription_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def subscription_in(subscription_list, redirect_field_name=REDIRECT_FIELD_NAME,
                    login_url=None):
    return user_passes_test(
        lambda u: u.get_active_subscription() in subscription_list,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
