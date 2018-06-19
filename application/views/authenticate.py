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
        return HttpResponseRedirect('/success')


def request_code(request):
    if request.method == 'GET':
        return render(request, 'request_code.html')
    else:
        return HttpResponseRedirect('/login_code_sent')


def login_code_sent(request):
    if request.method == 'GET':
        return render(request, 'login_code_sent.html')
    else:
        code = request.POST.get('code')
        if code == '676897':
            return HttpResponseRedirect('/success')
        else:
            request.method = 'GET'
            return render(request, 'login_code_sent.html', {'haserror': True, 'error_message': 'Invalid code'})


def email_login_code(request):
    return render(request, 'email_login_code.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        return HttpResponseRedirect('/activation_code_sent')


def activation_code_sent(request):
    if request.method == 'GET':
        return render(request, 'activation_code_sent.html')
    else:
        code = request.POST.get('code')
        if code == '11G7243FR9T0':
            return HttpResponseRedirect('/create_password')
        else:
            request.method = 'GET'
            return render(request, 'activation_code_sent.html', {'haserror': True, 'error_message': 'Invalid code'})


def email_activation_code(request):
    return render(request, 'email_activation_code.html')


def create_password(request):
    if request.method == 'GET':
        return render(request, 'create_password.html')
    else:
        return HttpResponseRedirect('/login')


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
        return HttpResponseRedirect('/success')