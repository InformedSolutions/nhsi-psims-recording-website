from django.shortcuts import render
from django.http import HttpResponseRedirect


def action(request):
    if request.method == 'GET':
        return render(request, 'action.html')
    else:
        action = request.POST.get('action')
        return HttpResponseRedirect('/record_type')
        #return render(request, 'action.html')


def record_type(request):
    if request.method == 'GET':
        return render(request, 'record_type.html')
    else:
        type = request.POST.get('record-type')
        return HttpResponseRedirect('/date_form')
        #return render(request, 'record_type.html')
