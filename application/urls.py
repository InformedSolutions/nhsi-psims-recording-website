from django.conf import settings
from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('simple_form', simple_form, name='simple_form'),
    path('long_form', long_form, name='long_form'),
    path('fieldset_form', fieldset_form, name='fieldset_form'),
    path('revealing_form', revealing_form, name='revealing_form'),
    path('account', account, name='account'),
    path('account_guidance', account_guidance, name='account_guidance'),
    path('action', action, name='action'),
    path('record_type', record_type, name='record_type'),
    path('form', form, name='form'),
    path('login', authenticate, name='login'),
    path('sign_in', sign_in, name='sign_in'),
    path('request_code', request_code, name='request_code'),
    path('register', register, name='register'),
    path('email_password_reset', email_password_reset, name='email_password_reset'),
    path('request_password_reset', request_password_reset, name='request_password_reset'),
    path('reset_link_sent', reset_link_sent, name='reset_link_sent'),
    path('reset_password', reset_password, name='reset_password')
]

# Django toolbar settings for development environments
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

