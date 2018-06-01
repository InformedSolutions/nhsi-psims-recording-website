from .base import render_form


def date_form(request):

    elements = [
        {
            "type": "radio-inline",
            "id": "uisdiudiu",
            "label": "Do you like tacos?",
            "guidance": "Tell us whether you like tacos",
            "target": {
                "true": "98r8jd8de"
            },
            "novalidate": False
        },
        {
            "type": "text",
            "id": "98r8jd8de",
            "label": "Describe your perfect taco",
            "guidance": "For example, corn tortilla with carne asada and fresh spring onion",
            "istarget": True,
            "novalidate": False

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
            "novalidate": False

        },
        {
            "type": "textarea",
            "id": "fif8f99di",
            "label": "Describe your ultimate baked beans meal",
            "guidance": "Don't be afraid to elaborate on all the juicy details",
            "istarget": True,
            "novalidate": False
        },
        {
            "type": "text",
            "id": "jskjf8f7",
            "label": "Please describe in a few words why you don't like baked beans",
            "guidance": "You are a terrible person",
            "istarget": True,
            "novalidate": False

        },
        {
            "type": "radio-inline",
            "id": "98f8ffdikk",
            "label": "Do you know the muffin man?",
            "guidance": "The one who lives on Drury Lane",
            "target": {
                "true": "uuuui4848"
            },
            "novalidate": False

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
            "novalidate": False

        },
        {
            "type": "date",
            "id": "487478jjjfju",
            "label": "When was the last time you ever had a good muffin from the muffin man?",
            "guidance": "I've never known the like",
            "istarget": True,
            "novalidate": False

        }
    ]

    return render_form(request, elements, "A terrific form for testing")
