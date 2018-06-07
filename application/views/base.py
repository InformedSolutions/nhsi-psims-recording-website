# A generic form-rendering function that renders the correct form based on the request method
from django.shortcuts import render
from ..validation import validate_form


'''
Renders the given elements through the form.html template.
Elements are expected in a standardise JSON format and comprise individual fieldsets and questions for rendering.
The form heading is an optional parameter for a heading-large page title if required.
'''
def render_form(request, elements, form_heading):
    if request.method == 'GET':

        # Ensure all references to partial templates are correct relative paths
        build_paths(elements)

        # Get the blank form
        return render(request, 'form.html', {'elements': elements, 'form_heading': form_heading, 'submit_text': 'Submit'})
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
                          {'elements': elements, 'form_heading': form_heading, 'submit_text': 'Submit', 'validation': messages})

        else:
            # No validation errors - for now, render a generic success page
            # In future, persist data
            return render(request, 'success.html')


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

"""
Temporarily storing some forms which can be used for testing below.
These can be deleted once we start getting forms from the API
"""
dummy_elements = {
    "title": "A test form with all control types",
    "elements": [
        {
            "type": "radio-inline",
            "id": "uisdiudiu",
            "label": "Do you like tacos?",
            "guidance": "Tell us whether you like tacos",
            "target": {
                "true": "98r8jd8de"
            },
            "novalidate": False,
            "required": True
        },
        {
            "type": "text",
            "id": "98r8jd8de",
            "label": "Describe your perfect taco",
            "guidance": "For example, corn tortilla with carne asada and fresh spring onion",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "8rf88f89f8d",
            "label": "What about baked beans?",
            "guidance": "We aren't being nosey, we just want to tailor your experience",
            "target": {
                "true": "fif8f99di",
                "false": "jskjf8f7"
            },
            "novalidate": False,
            "required": True
        },
        {
            "type": "textarea",
            "id": "fif8f99di",
            "label": "Describe your ultimate baked beans meal",
            "guidance": "Don't be afraid to elaborate on all the juicy details",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "text",
            "id": "jskjf8f7",
            "label": "Please describe in a few words why you don't like baked beans",
            "guidance": "You are a terrible person",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "98f8ffdikk",
            "label": "Do you know the muffin man?",
            "guidance": "The one who lives on Drury Lane",
            "target": {
                "true": "uuuui4848"
            },
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "uuuui4848",
            "label": "Do you think his muffins are any good?",
            "guidance": "Between you and me, I've got my doubts",
            "target": {
                "true": "487478jjjfju"
            },
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "date",
            "id": "487478jjjfju",
            "label": "When was the last time you ever had a good muffin from the muffin man?",
            "guidance": "I've never known the like",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "fieldset",
            "id": "9r0ejkjkw88",
            "label": "An example of a fieldset",
            "guidance": "Please answer the below questions to the best of your ability",
            "istarget": False,
            "novalidate": True,
            "elements": [
                {
                    "type": "text",
                    "id": "98r8jd8rrdy",
                    "label": "How many tacos do you think you could eat in one sitting?",
                    "guidance": "",
                    "istarget": False,
                    "novalidate": False,
                    "required": True
                },
                {
                    "type": "text",
                    "id": "58r8jewwd8de",
                    "label": "What about in a full day?",
                    "guidance": "I can probably eat 7 or 8 myself",
                    "istarget": False,
                    "novalidate": False,
                    "required": True
                },
                {
                    "type": "checkbox",
                    "id": "98r8jd8rrde",
                    "label": "What are the best kinds of beans?",
                    "guidance": "Choose all that apply",
                    "istarget": False,
                    "novalidate": False,
                    "options": [
                        {
                            "id": 1,
                            "label": "Baked beans"
                        },
                        {
                            "id": 2,
                            "label": "Coffee beans"
                        },
                        {
                            "id": 3,
                            "label": "Mexican Jumping beans"
                        },
                        {
                            "id": 4,
                            "label": "Jelly beans"
                        }
                    ],
                    "required": True
                },
            ]
        },
        {
            "type": "radio-stacked",
            "id": "8r8kkkkf9r",
            "label": "What is the best type of taco out there?",
            "guidance": "You've only got one shot at this, don't get it wrong",
            "istarget": False,
            "novalidate": False,
            "options": [
                {
                    "id": 1,
                    "label": "Carnitas",
                    "target": "fuuf8tt77t"
                },
                {
                    "id": 2,
                    "label": "Carne Asada",
                    "target": "fuuf8tt77t"
                },
                {
                    "id": 3,
                    "label": "Con queso y muchos frijoles",
                    "target": "fuuf8tt77t"
                },
                {
                    "id": 4,
                    "label": "Surprise flavour jamboree",
                    "target": "jffrf8f7"
                },
                {
                    "id": 5,
                    "label": "Black beans and grilled chicken",
                    "target": "fuuf8tt77t"
                }
            ],
                    "required": True
        },
        {
            "type": "text",
            "id": "jffrf8f7",
            "label": "That's correct.  Write a note of self-praise here",
            "guidance": "You've got great tase",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "textarea",
            "id": "fuuf8tt77t",
            "label": "That's incorrect.  Please explain yourself.",
            "guidance": "You are a terrible person",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "date",
            "id": "8d8ikikd665",
            "label": "In which month and year were you born?",
            "guidance": "I bet you'll find this pretty tricky",
            "istarget": False,
            "novalidate": False,
            "required": True,
            "approx_date": True
        }
    ]
}

date_elements = {
    "title": "Date of incident",
    "elements": [
        {
            "type": "radio-inline",
            "id": "f8f8kjdi44j",
            "label": "Did the incident occur today?",
            "guidance": "",
            "target": {
                "false": "75799ffff"
            },
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "75799ffff",
            "label": "Do you know the exact date of the incident?",
            "guidance": "",
            "target": {
                "true": "f8k3jn33di",
                "false": "yd65c6ll0"
            },
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "date",
            "id": "f8k3jn33di",
            "label": "",
            "guidance": "For example, 20 11 2017",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "date",
            "id": "yd65c6ll0",
            "label": "",
            "guidance": "If you're not sure, tell us roughly when you think it happened",
            "istarget": True,
            "novalidate": False,
            "required": True,
            "approx_date": True
        }
    ]
}