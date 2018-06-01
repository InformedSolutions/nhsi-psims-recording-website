# A generic form-rendering function that renders the correct form based on the request method
from django.shortcuts import render


def render_form(request, elements, form_heading):
    if request.method == 'GET':
        for element in elements:
            element['type'] = "./form-elements/" + element['type'] + ".html"

        # Get the blank form
        return render(request, 'form.html', {'elements': elements, 'form_heading': form_heading})
    else:
        # For now, render a generic success page
        return render(request, 'success.html')