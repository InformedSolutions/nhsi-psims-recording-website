from django.shortcuts import render
from django.http import HttpResponseRedirect


def authenticate(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        choice = request.POST.get('authentication')
        request.method = 'GET'

        if choice == 'email-login':
            return HttpResponseRedirect('/sign_in')

        elif choice == 'code-login':
            return HttpResponseRedirect('/request_code')

        elif choice == 'register':
            return HttpResponseRedirect('/register')

        else:
            # Redirect to the guidance page on anonymous login
            return HttpResponseRedirect('/account_guidance')


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html')
    else:
        return render(request, 'success.html')


def request_code(request):
    if request.method == 'GET':
        return render(request, 'request_code.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'login.html')


def request_password_reset(request):
    if request.method == 'GET':
        return render(request, 'request_password_reset.html')
    else:
        return HttpResponseRedirect('/reset_link_sent')


def reset_link_sent(request):
    return render(request, 'reset_link_sent.html')


def email_password_reset(request):
    # This is an example email that could be sent for a password reset
    if request.method == 'GET':
        return render(request, 'email_password_reset.html')
    else:
        return HttpResponseRedirect('/reset_password')


def reset_password(request):
    if request.method == 'GET':
        return render(request, 'reset_password.html')
    else:
        return render(request, 'success.html')