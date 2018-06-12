"""
Currently a dummy function that returns representative form data.
"""
def call_api(endpoint, data):
    # Once the API is plugged in use the endpoint and data to build the request

    # Return the response after checking for errors
    if dummy_elements['form_id'] == data:
        return dummy_elements
    elif date_elements['form_id'] == data:
        return date_elements


"""
Temporarily storing some forms which can be used for testing below.
These can be deleted once we start getting forms from the API
"""
dummy_elements = {
    "form_id": "icic87ejm20js",
    "title": "A test form with all control types",
    "elements": [
        {
            "type": "radio-inline",
            "id": "uisdiudiu",
            "label": {
                "question": "Was the patient under 1 month old?",
                "true": "Yes",
                "false": "No"
            },
            "guidance": "At the time of incident",
            "target": {
                "true": "98r8jd8de"
            },
            "novalidate": False,
            "required": True
        },
        {
            "type": "text",
            "id": "98r8jd8de",
            "label": "What was the patient's age?",
            "guidance": "Tell us roughly how old the patient was",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "8rf88f89f8d",
            "label": {
                "question": "Does the patient have a learning disability?",
                "true": "Yes",
                "false": "No"
            },
            "guidance": "Example guidance text",
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
            "label": "Describe the incident",
            "guidance": "Use this space to describe in your own words what happened. It is important that the information you provide is factual and not simply opinion.  Concentrate on the facts and describe the events in the sequence in which they occurred. Please do not include any patient confidential or person identifiable information, for example names or NHS numbers.",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "text",
            "id": "jskjf8f7",
            "label": "An example question that is dependent upon one higher up the form",
            "guidance": "",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "98f8ffdikk",
            "label": {
                "question": "Was this a Never Event?",
                "true": "Yes",
                "false": "No"
            },
            "guidance": "Never Events are serious incidents that are entirely preventable because guidance or safety recommendations providing strong systemic protective barriers are available at a national level, and should have been implemented by all healthcare providers.",
            "target": {
                "true": "uuuui4848"
            },
            "novalidate": False,
            "required": True
        },
        {
            "type": "radio-inline",
            "id": "uuuui4848",
            "label": {
                "question": "Do you know the patient's date of birth?",
                "true": "Yes",
                "false": "No"
            },
            "guidance": "",
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
            "label": "What is the patient's date of birth?",
            "guidance": "For example 18 7 2008",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "fieldset",
            "id": "9r0ejkjkw88",
            "label": "This is an example fieldset",
            "guidance": "Fieldsets are groups of questions that can be useful for related items, like address lines.  Normally there will only be one per page.",
            "istarget": False,
            "novalidate": True,
            "elements": [
                {
                    "type": "text",
                    "id": "98r8jd8rrdy",
                    "label": "Example text question within a fieldset",
                    "guidance": "It should look like any other text question",
                    "istarget": False,
                    "novalidate": False,
                    "required": True
                },
                {
                    "type": "text",
                    "id": "58r8jewwd8de",
                    "label": "Another example text question",
                    "guidance": "This question is optional",
                    "istarget": False,
                    "novalidate": False,
                    "required": False
                },
                {
                    "type": "checkbox",
                    "id": "98r8jd8rrde",
                    "label": "What is the patient's gender?",
                    "guidance": "",
                    "istarget": False,
                    "novalidate": False,
                    "options": [
                        {
                            "id": 1,
                            "label": "Female"
                        },
                        {
                            "id": 2,
                            "label": "Male"
                        },
                        {
                            "id": 3,
                            "label": "Non-binary"
                        },
                        {
                            "id": 4,
                            "label": "Unknown"
                        }
                    ],
                    "required": True
                },
            ]
        },
        {
            "type": "radio-stacked",
            "id": "8r8kkkkf9r",
            "label": "Please tick all presentations that apply:",
            "guidance": "Select all that apply",
            "istarget": False,
            "novalidate": False,
            "options": [
                {
                    "id": 1,
                    "label": "Additional autism",
                    "target": "fuuf8tt77t"
                },
                {
                    "id": 2,
                    "label": "Behaviour that challenges",
                    "target": "fuuf8tt77t"
                },
                {
                    "id": 3,
                    "label": "Significant physical difficulties",
                    "target": "fuuf8tt77t"
                },
                {
                    "id": 4,
                    "label": "Profound and Multiple Learning Disabilities (PMLD)",
                    "target": "jffrf8f7"
                },
                {
                    "id": 5,
                    "label": "Dementia",
                    "target": "fuuf8tt77t"
                }
            ],
                    "required": True
        },
        {
            "type": "text",
            "id": "jffrf8f7",
            "label": "Describe any additional or related information:",
            "guidance": "This is a simple text box",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "textarea",
            "id": "fuuf8tt77t",
            "label": "Describe any additional or related information:",
            "guidance": "This is an expandable text area",
            "istarget": True,
            "novalidate": False,
            "required": True
        },
        {
            "type": "date",
            "id": "8d8ikikd665",
            "label": "What was the patient's age?",
            "guidance": "Tell us roughly how old the patient was",
            "istarget": False,
            "novalidate": False,
            "required": True,
            "approx_date": True
        }
    ]
}

date_elements = {
    "form_id": "abc123",
    "title": "Date of incident",
    "next_form_id": "icic87ejm20js",
    "elements": [
        {
            "type": "radio-inline",
            "id": "f8f8kjdi44j",
            "label": {
                "question": "Did the incident occur today?",
                "true": "Yes",
                "false": "No"
            },
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
            "label": {
                "question": "Do you know the exact date of the incident?",
                "true": "Yes",
                "false": "No"
            },
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