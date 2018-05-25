from django.shortcuts import render


def account(request):
    if request.method == 'GET':
        return render(request, 'account.html')
    else:
        choice = request.POST.get('account')
        return render(request, 'account_guidance.html')
