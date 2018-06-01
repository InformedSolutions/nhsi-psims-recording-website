from django import forms

from govuk_forms.fields import SplitDateField
from govuk_forms.forms import GOVUKForm
from govuk_forms.widgets import InlineCheckboxSelectMultiple, InlineRadioSelect, \
    SeparatedCheckboxSelectMultiple, SeparatedRadioSelect

options = (('a', 'Alpha'), ('b', 'Beta'))
separated_options = (('a', 'Alpha'), ('b', 'Beta'), ('c', 'Gamma'), ('d', 'Delta'), ('e', 'Epsilon'))
grouped_options = (
    ('First', options),
    ('Second', (('c', 'Gamma'), ('d', 'Delta'))),
)

class IncidentDateForm(GOVUKForm):
    # customisations:
    auto_replace_widgets = True
    field_label_classes = 'heading-medium'

    reveal_conditionally = {
        'occur_today': {
            False: 'exact_date'
        },
        'exact_date': {
            True: 'full_date',
            False: 'hidden_at_first'
        }
    }

    occur_today = forms.ChoiceField(label='Did the incident occur today?', choices=((True, 'Yes'), (False, 'No')),
                                    widget=InlineRadioSelect)

    exact_date = forms.ChoiceField(label='Did the incident occur today?', choices=((True, 'I know the exact date'), (False, 'Im not sure')),
                                    widget=InlineRadioSelect)

    full_date = SplitDateField(label='', help_text='For example, 20 11 2017', required=False)

    hidden_at_first = forms.CharField(label='Hidden at first')