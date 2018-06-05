# A generic form-rendering function that renders the correct form based on the request method
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..validation import validate_form, question_visible


def render_form(request, elements, form_heading):
    if request.method == 'GET':

        build_paths(elements)

        # Get the blank form
        return render(request, 'form.html', {'elements': elements, 'form_heading': form_heading, 'submit_text': 'Submit'})
    else:
        # Validate the form
        collect_responses(request, elements)
        messages = validate_form(elements)
        if len(messages) > 0:
            for message in messages:
                for element in elements:
                    if element['type'] == 'fieldset':
                        for e in element['elements']:
                            if message['id'] == e['id']:
                                e['haserror'] = True
                                e['error_message'] = message['label']
                    if message['id'] == element['id']:
                        element['haserror'] = True
                        element['error_message'] = message['label']

            request.method = 'GET'
            build_paths(elements)
            return render(request, 'form.html',
                          {'elements': elements, 'form_heading': form_heading, 'submit_text': 'Submit', 'validation': messages})

        else:
            # For now, render a generic success page
            return render(request, 'success.html')

def build_paths(elements):
    for element in elements:

        # For fieldsets recurse through sub-elements to set the partial path
        if element['type'] == 'fieldset':
            for e in element['elements']:
                e['type'] = "./form-elements/" + e['type'] + ".html"

        # Set the correct file path for the partial that will render the element
        element['type'] = "./form-elements/" + element['type'] + ".html"

def collect_responses(request, elements):

    for element in elements:
        if element['type'] == 'fieldset':
            for e in element['elements']:
                e = collect_response(request, e)
        else:
            element = collect_response(request, element)

def collect_response(request, element):
    if element['type'] == 'date':
        day = request.POST.get(element['id'] + '-day')
        month = request.POST.get(element['id'] + '-month')
        year = request.POST.get(element['id'] + '-year')
        date = day + '-' + month + '-' + year
        element['response'] = date
        element['response_list'] = {"day": day, "month": month, "year": year}

    elif element['type'] == 'checkbox':
        responses = []
        for item in element['options']:
            choice_id = element['id'] + '-' + str(item['id'])
            choice = request.POST.get(choice_id)
            responses.append({"choice_id": choice_id, "choice": choice})
            if not choice == None:
                item['ticked'] = True
            else:
                item['ticked'] = False
        element['response'] = responses

    else:
        response = request.POST.get(element['id'])
        element['response'] = response

    return element