from django.shortcuts import render
from django.http import HttpResponseRedirect


def account(request):
    if request.method == 'GET':
        return render(request, 'account.html')
    else:
        choice = request.POST.get('account')
        request.method = 'GET'
        # Evaluate form here

        # If form is ok do redirect
        return HttpResponseRedirect('/account_guidance')

        # Otherwise return render with the request, can pass vars
        #return render(request, 'account.html')


def account_guidance(request):
    if request.method == 'GET':
        return render(request, 'account_guidance.html')
    else:
        return HttpResponseRedirect('/action')
        #return render(request, 'account_guidance.html')
