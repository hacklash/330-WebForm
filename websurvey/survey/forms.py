from django import forms
from django.forms.widgets import RadioSelect
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard import FormWizard

CONTROLLERS = (('as', 'Arcade Stick'),
               ('gp', 'Gamepad'),
               ('kb', 'Keyboad'))

GATES = (('cir', 'Circular'),
         ('oct', 'Octagonal'),
         ('squ', 'Square'))

SCROLLING = (('hori', 'Horizontal'),
             ('vert', 'Vertical'))

DEVELOPER = (('cave', 'Cave'),
             ('trea', 'Treasure'))

class SurveyWizard(FormWizard):
    def done(self, request, form_list):
        return render_to_response('results.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

class ControllerForm(forms.Form):
    controller = forms.ChoiceField(widget=RadioSelect, choices=CONTROLLERS)

class GateForm(forms.Form):
    gate = forms.ChoiceField(widget=RadioSelect, choices=GATES)

class ScrollingForm(forms.Form):
    scrolling = forms.ChoiceField(widget=RadioSelect, choices=SCROLLING)

