'''
Helper functions for general re-user between tests
'''
def get_question(id, elements):
    for element in elements:
        if element['type'] == 'fieldset':
            for e in element['elements']:
                if e['id'] == id:
                    return e
        else:
            if element['id'] == id:
                return element


def set_property(property, value, elements, id):
    for element in elements:
        if element['type'] == 'fieldset':
            for e in element['elements']:
                if e['id'] == id:
                    e[property] = value
        else:
            if element['id'] == id:
                element[property] = value

'''
Test data for general re-user between tests
'''
test_elements = [
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