def validate_form(elements):

    questions = []

    for element in elements:
        if element['type'] == 'fieldset':
            for e in element['elements']:
                questions.append(e)
        else:
            questions.append(element)

    messages = []

    for question in questions:
        try:
            message = assess_condition(question, question['response'], elements)
            if not isinstance(message, bool):
                messages.append(message)
        except:
            print("Response not found")
            messages.append(build_message("1", "#" + question['id'], "This question is required", None))

    print(messages)

    return messages


def assess_condition(question, response, elements):
    if question['required']:
        if question_visible(question, elements):
            if question['type'] == 'date':
                if question['response'] == '--':
                    return build_message("1", question['id'], "This question is required", response)
                else:
                    components = [question['response_list']['day'], question['response_list']['month'], question['response_list']['year']]
                    incomplete_date = False
                    for component in components:
                        if component == '':
                            incomplete_date = True

                    if incomplete_date:
                        return build_message("3", question['id'], "Please supply a complete date", response)
                    else:
                        # Date question has been answered fully
                        return True

            elif response == '' or response == None:
                # Empty response
                return build_message("1", question['id'], "This question is required", response)

            elif isinstance(response, list):
                # List responses expect at least one value
                if len(response) == 0:
                    return build_message("2", question['id'], "Choose an option", response)
                else:
                    # At least one non-empty value is expected in list responses
                    empty = True
                    for r in response:
                        if r['choice'] != None and r['choice'] != '':
                            empty = False
                    if empty:
                        return build_message("2", question['id'], "Choose an option", response)
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


def build_message(code, id, label, response):
    message = {}
    message['id'] = id
    message['code'] = code
    message['href'] = "#" + id
    message['label'] = label
    message['response'] = response
    return message

# Returns True if the question is visible on the page or false if not
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


# Strips response data off a given question
def strip_response(question):
    question['response'] = None