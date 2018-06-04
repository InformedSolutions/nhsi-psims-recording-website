def validate_form(request, elements):

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
            # special case for date
            if question['type'] == 'date':
                day = request.POST.get(question['id'] + '-day')
                month = request.POST.get(question['id'] + '-month')
                year = request.POST.get(question['id'] + '-year')
                date = day + '-' + month + '-' + year
                print(date)
                message = assess_condition(question, date)
                if not isinstance(message, bool):
                    messages.append(message)
            elif question['type'] == 'checkbox':
                responses = []
                for item in question['options']:
                    choice = request.POST.get(question['id'] + '-' + str(item['id']))
                    responses.append(choice)
                print(responses)
                message = assess_condition(question, responses)
                if not isinstance(message, bool):
                    messages.append(message)
            else:
                response = request.POST.get(question['id'])
                print(response)
                message = assess_condition(question, response)
                if not isinstance(message, bool):
                    messages.append(message)
        except:
            print("Response not found")
            messages.append(build_message("1", "#" + question['id'], "This question is required"))

    print(messages)

    return messages

def assess_condition(question, response):
    if question['required']:
        if response == '' or response == None:
            return build_message("1", "#" + question['id'], "This question is required")
        elif isinstance(response, list):
            if len(response) == 0:
                return build_message("2", "#" + question['id'], "Choose an option")
            else:
                empty = True
                for r in response:
                    if r != None:
                        empty = False
                if empty:
                    return build_message("2", "#" + question['id'], "Choose an option")
                else:
                    return True
        else:
            return True
    else:
        return True

def build_message(code, href, label):
    message = {}
    message['code'] = code
    message['href'] = href
    message['label'] = label
    return message