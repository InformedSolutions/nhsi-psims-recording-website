from django.shortcuts import render
from django.http import HttpResponseRedirect


def action(request):
    if request.method == 'GET':
        return render(request, 'action.html')
    else:
        # Collect posted data
        action = request.POST.get('action')

        # Render next page
        return HttpResponseRedirect('/record_type')


def record_type(request):
    if request.method == 'GET':
        return render(request, 'record_type.html')
    else:
        # Collect posted data
        type = request.POST.get('record-type')

        # Get next form id from the data here and use in redirect
        next_form_id = "abc123"

        # Render next page
        return HttpResponseRedirect('/form?next_form_id=' + next_form_id)
