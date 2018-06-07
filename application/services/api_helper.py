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
                "question": "Do you like tacos?",
                "true": "Yes",
                "false": "No"
            },
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
            "label": {
                "question": "What about baked beans?",
                "true": "Yes",
                "false": "No"
            },
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
            "label": {
                "question": "Do you know the muffin man?",
                "true": "Yes",
                "false": "No"
            },
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
            "label": {
                "question": "Do you think his muffins are any good?",
                "true": "Yes",
                "false": "No"
            },
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