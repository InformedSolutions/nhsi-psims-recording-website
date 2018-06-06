'''
Validates a set of elements.
The elements object must already have the responses attached.
'''
def validate_form(elements):

    # Gather only elements which are questions in a single list
    questions = []

    for element in elements:
        # Find any sub-elements contained within fieldsets
        if element['type'] == 'fieldset':
            for e in element['elements']:
                questions.append(e)
        else:
            # Append elements to the list
            # This can be built out to exclude certain element types if required
            questions.append(element)

    # The messages list will collect all the validation errors that are identified
    messages = []

    # Iterate through each question and assess whether the conditions required to submit it are met
    for question in questions:
        try:
            message = assess_condition(question, elements)
            # If the response is a boolean it is not a validation error.  Only put errors into the messages list.
            if not isinstance(message, bool):
                messages.append(message)
        except:
            # In the unlikely event that a response could not be found for the question (even an unanswered
            # question should be on the POST body as 'None' or '') add a message to the list
            messages.append(build_message("1", "#" + question['id'], "This question is required", None))

    # Return the messages containing validation errors for rendering
    return messages


'''
Evaluates the conditions for a particular question to be valid.
This requires checks of:
    - the question's response, e.g. is it blank or None
    - the question's visibility - if it is not visible, do not validate (response would be blank which otherwise
      could trigger an error)
    - whether the question is required or not

This will also strip responses from questions which are not visible.  This can occur when a dependent question is
answered but then its trigger question is answered differently which hides the question but does not clear its data.
'''
def assess_condition(question, elements):
    if question['required']:
        if question_visible(question, elements):
            if question['type'] == 'date':
                # For dates the response will be DD-MM-YYYY, so check that each of these components is present
                if question['response'] == '--':
                    return build_message("1", question['id'], "This question is required", question['response'])
                else:
                    # For approx-dates only evaluate the month and year
                    if 'approx_date' in question:
                        if question['approx_date']:
                            components = [question['response_list']['month'], question['response_list']['year']]
                        else:
                            components = [question['response_list']['day'], question['response_list']['month'],
                                          question['response_list']['year']]
                    else:
                        components = [question['response_list']['day'], question['response_list']['month'], question['response_list']['year']]

                    incomplete_date = False
                    # Check each individual component - if any of them are blank the date is not complete
                    for component in components:
                        if component == '':
                            incomplete_date = True

                    if incomplete_date:
                        return build_message("3", question['id'], "Please supply a complete date", question['response'])
                    else:
                        # Date question has been answered fully
                        return True

            # General catch for empty responses
            elif question['response'] == '' or question['response'] == None:
                return build_message("1", question['id'], "This question is required", question['response'])

            # For lists, evaluate their members to ensure they have an item and it is not empty
            elif isinstance(question['response'], list):
                # List responses expect at least one value
                if len(question['response']) == 0:
                    return build_message("2", question['id'], "Choose an option", question['response'])
                else:
                    # At least one non-empty value is expected in list responses
                    empty = True
                    for r in question['response']:
                        if r['choice'] != None and r['choice'] != '':
                            # A single non-empty response is enough to make the response valid
                            empty = False
                    if empty:
                        return build_message("2", question['id'], "Choose an option", question['response'])
                    else:
                        # Non-empty list response, valid
                        return True
            else:
                # Question did not meet any error criteria
                return True

        else:
            # Question was hidden, prevent any response from being saved and do not validate
            strip_response(question)
            return True
    else:
        # Question was not required
        return True


'''
Helper for building a validation message.  This consists of:
    - id: the id of the question that this message pertains to
    - code: not currently being used but may be helpful in future
    - href: uses question id to build the link that the users can click to be taken to the question
    - label: the actual text of the error message for display to users
    - response: response to the question - this is not currently used but may be useful in future
'''
def build_message(code, id, label, response):
    message = {}
    message['id'] = id
    message['code'] = code
    message['href'] = "#" + id
    message['label'] = label
    message['response'] = response
    return message

'''
Evaluates whether a given question is visible on the page based on the answers to other questions.
All questions on the page must be iterated to find any that reference the question as a data target.
If this is the case, check whether the data target conditions are met, i.e. the response will trigger the question.
Returns True if the question is visible on the page or false if not.
'''
def question_visible(question, elements):
    if 'istarget' in question:
        if question['istarget']:
            for element in elements:
                # Stacked radios are a special case where each option can have its own target
                if element['type'] == 'radio-stacked':
                    target_found = False
                    condition_met = False
                    for option in element['options']:
                        if 'target' in option:
                            if option['target'] == question['id']:
                                # If the id is in a target then this radio is the trigger to the question
                                target_found = True
                                if 'response' in element:
                                    if element['response'] == option['label']:
                                        # The selected option triggers the target
                                        condition_met = True
                    if target_found:
                        # This radio is responsible for showing the question so we will return without iterating further elements
                        if condition_met:
                            # An option that triggers the question was selected, so question visible
                            return True
                        else:
                            # This radio triggers the question, but the selected value was not the right one
                            return False
                else:
                    # Find elements which have a data target
                    if 'target' in element:
                        # Iterate through the target's properties to see if it targets this question
                        for key, value in element['target'].items():
                            # If it does target this question, check whether the current response triggers the target
                            if value == question['id']:
                                if 'response' in element:
                                    if element['response'] == key:
                                        # If this is the case then the question should be visible
                                        return True
                                    else:
                                        # The response is not the one which will trigger the target question
                                        return False
                                else:
                                    # Trigger question has not been answered so the question is not visible
                                    return False

            # The question is not visible if any of the above if statements were not true
            return False
        else:
            # The question is not a target and should be visible
            return True
    else:
        # If the question is not marked as being a target then it is visible/not hidden
        return True


'''
Strips response data off a given question.
Useful for ensuring questions which are answered and then made non-visible do not get saved.
'''
def strip_response(question):
    question['response'] = None
