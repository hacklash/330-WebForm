from django import forms
from django.forms.widgets import RadioSelect
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard import FormWizard

CONTROLLERS = (('Arcade Stick','Arcade Stick'),
               ('Gamepad','Gamepad'),
               ('Keyboad','Keyboard'))

GATES = (('Circular', 'Circular'),
         ('Octagonal', 'Octagonal'),
         ('Square', 'Square'))

SCROLLING = (('Horizontal', 'Horizontal'),
             ('Vertical', 'Vertical'))

H_GAME = (('Gradius V', 'Gradius V'),
          ('Sexy Parodius', 'Sexy Parodius'),
          ('Border Down', 'Border Down'),
          ('Deathsmiles', 'Deathsmiles'),
          ('Your Choice: ', 'Other'))

DEVELOPER = (('Cave', 'Cave'),
             ('Treasure', 'Treasure'))

CAVE = (('Dodonpachi', 'Dodonpachi'),
        ('Ketsui kizuna jigoku tachi', 'Ketsui kizuna jigoku tachi'),
        ('Mushihimesama Futari 1.5', 'Mushihimesama Futari 1.5'),
        ('Your choice: ', 'Other'))

TREASURE = (('Radiant Silvergun', 'Radiant Silvergun'),
            ('Sin and Punishment', 'Sin and Punishment'),
            ('Ikaruga', 'Ikaruga'),
            ('Sin and Punishment: Star Successor', 'Sin and Punishment: Star Successor'),
            ('Your choice: ', 'Other'))

class SurveyWizard(FormWizard):
    def done(self, request, form_list):
        return render_to_response('results.html', {
            'form_data': [form.cleaned_data.iteritems() for form in form_list],
        })

class ControllerForm(forms.Form):
    controller = forms.ChoiceField(widget=RadioSelect, choices=CONTROLLERS)

class GateForm(forms.Form):
    gate = forms.ChoiceField(widget=RadioSelect, choices=GATES)

class ScrollingForm(forms.Form):
    scrolling = forms.ChoiceField(widget=RadioSelect, choices=SCROLLING)

class HGameForm(forms.Form):
    hgame = forms.ChoiceField(widget=RadioSelect, choices=H_GAME)

class VDeveloperForm(forms.Form):
    vdeveloper = forms.ChoiceField(widget=RadioSelect, choices=DEVELOPER)

class VCaveForm(forms.Form):
    vgame = forms.ChoiceField(widget=RadioSelect, choices=CAVE)

class VTreasureForm(forms.Form):
    vgame = forms.ChoiceField(widget=RadioSelect, choices=TREASURE)
