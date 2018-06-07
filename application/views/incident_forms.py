from .base import render_form, date_elements, dummy_elements
import copy

def form(request):

    # Get the id for this form from the request
    next_form_id = request.GET.get('next_form_id')

    # Use the id to get call the API to get the form title and content
    # For now just getting them from base.py - in future they will come from the API response
    # Deepcopy used to prevent multiple changes to template paths on browser back/forward -
    # Once getting these from the API this may not be necessary but should be tested
    elements = copy.deepcopy(date_elements['elements'])
    title = copy.deepcopy(date_elements['title'])

    # Render the form
    return render_form(request, elements, title)
