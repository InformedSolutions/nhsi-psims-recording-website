from .base import render_form
from application.services.api_helper import call_api
import copy

def form(request):

    # Get the id for this form from the request
    form_id = request.GET.get('next_form_id')

    # Use the id to call the API to get the form title and content
    # For now just using a dummy function in API helper
    form = call_api("/dummy/api", form_id)

    # Deepcopy used to prevent multiple changes to template paths on browser back/forward
    # Once getting these from the API this may not be necessary but should be tested
    elements = copy.deepcopy(form['elements'])
    title = copy.deepcopy(form['title'])
    if 'next_form_id' in form:
        next_form_id = copy.deepcopy(form['next_form_id'])
    else:
        next_form_id = None

    # Render the form
    return render_form(request, elements, title, next_form_id)
