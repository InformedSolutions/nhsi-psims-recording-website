from django.shortcuts import render


def account(request):
    return render(request, 'account.html')

def account_choice(request):
    choice = request.POST.get('account')
    print(choice)
    return render(request, 'account.html')
