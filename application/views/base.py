from django.shortcuts import render
from application.services.validation import validate_form
from django.http import HttpResponseRedirect


'''
A generic form-rendering function that renders the correct form through the form.html template.
Elements are expected in a standardise JSON format and comprise individual fieldsets and questions for rendering.
The form heading is an optional parameter for a heading-large page title if required.
'''
def render_form(request, elements, form_heading, next_form_id):
    if request.method == 'GET':

        # Ensure all references to partial templates are correct relative paths
        build_paths(elements)

        # Get the blank form
        return render(request, 'form.html', {'elements': elements, 'form_heading': form_heading, 'submit_text': 'Submit', 'next_form_id': next_form_id})
    else:
        # Gather question responses from the body
        collect_responses(request, elements)

        # Validate the responses - if there are any problems the messages array will have objects
        messages = validate_form(elements)

        if len(messages) > 0:
            # For each message, flag an error and attach the message to the relevant question
            for message in messages:
                for element in elements:
                    # Iterate over sub-elements within fieldsets
                    if element['type'] == 'fieldset':
                        for e in element['elements']:
                            if message['id'] == e['id']:
                                e['haserror'] = True
                                e['error_message'] = message['label']
                    if message['id'] == element['id']:
                        element['haserror'] = True
                        element['error_message'] = message['label']

            # We want to GET the page as if it was the first time, the difference being we may have
            # validation messages and pre-populated values to render too
            request.method = 'GET'

            # Ensure all references to partial templates are correct relative paths
            build_paths(elements)

            # Render the page with the built-out elements and validation messages
            return render(request, 'form.html',
                          {'elements': elements, 'form_heading': form_heading, 'submit_text': 'Submit', 'validation': messages, 'next_form_id': next_form_id})

        else:
            # No validation errors - for now, render a generic success page
            # In future, persist data then request the next section using the id from elements
            if next_form_id != None:
                # Get the next form
                return HttpResponseRedirect('/form?next_form_id=' + next_form_id)
            else:
                return HttpResponseRedirect('/success')


'''
Iterates through the given elements and updates their 'type' property to be a relative path to the template html.
This ensures the JSON does not need to know about relative paths and can be independent of this UI.
'''
def build_paths(elements):
    for element in elements:

        # For fieldsets recurse through sub-elements to set the partial path
        if element['type'] == 'fieldset':
            for e in element['elements']:
                e['type'] = "./form-elements/" + e['type'] + ".html"

        # Set the correct file path for the partial template that will render the element
        # This includes fieldsets which have their own template
        element['type'] = "./form-elements/" + element['type'] + ".html"


'''
Iterates through the elements to collect and assign the responses from the POST data to each element.
'''
def collect_responses(request, elements):

    for element in elements:
        # Fieldsets do not have responses but contain sub-elements, iterate over them instead
        if element['type'] == 'fieldset':
            for e in element['elements']:
                collect_response(request, e)
        else:
            collect_response(request, element)


'''
Gets the POST data for a single element and attaches it to the 'response' property of the element.
Does any necessary formatting, e.g. for dates.
'''
def collect_response(request, element):
    if element['type'] == 'date':
        # Dates are comprised of two or three inputs - collect each depending on type
        day = request.POST.get(element['id'] + '-day')
        month = request.POST.get(element['id'] + '-month')
        year = request.POST.get(element['id'] + '-year')

        # Combine components to make a save-friendly date
        if 'approx_date' in element:
            if element['approx_date']:
                # There is no day in an approx-date
                date = month + '-' + year
            else:
                date = day + '-' + month + '-' + year
        else:
            date = day + '-' + month + '-' + year

        element['response'] = date

        # Also create a special property containing the individual components which supports re-rendering:
        # each component can be matched back to its input in the view
        element['response_list'] = {"day": day, "month": month, "year": year}

    elif element['type'] == 'checkbox':
        # Checkboxes can have multiple responses, collect and save them in a list
        responses = []
        for item in element['options']:
            choice_id = element['id'] + '-' + str(item['id'])
            choice = request.POST.get(choice_id)

            # Add the choice to the responses object which can be validated
            responses.append({"choice_id": choice_id, "choice": choice})

            # Also mark whether the choice was selected in order to support re-rendering on the form
            if not choice == None:
                item['ticked'] = True
            else:
                item['ticked'] = False

        element['response'] = responses

    else:
        # For all other input types simply get the response by question id
        response = request.POST.get(element['id'])
        element['response'] = response


def success(request):
    return render(request, 'success.html')
