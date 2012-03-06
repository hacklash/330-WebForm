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
          ('Your choice: ', 'Other'))

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


class ControllerForm(forms.Form):
    controller = forms.ChoiceField(widget=RadioSelect, choices=CONTROLLERS, label='Favorite Controller?')

class GateForm(forms.Form):
    gate = forms.ChoiceField(widget=RadioSelect, choices=GATES, label='Favorite arcade stick gate?')

class ScrollingForm(forms.Form):
    scrolling = forms.ChoiceField(widget=RadioSelect, choices=SCROLLING, label='Do you like vertical or horizontal scrollers better?')

class HGameForm(forms.Form):
    game = forms.ChoiceField(widget=RadioSelect, choices=H_GAME, label='What is your favorite horizontal scroller?')
    other = forms.CharField(required=False, label='Other:')
    def clean(self):
        cleaned_data = self.cleaned_data
        game = cleaned_data.get("game")
        other = cleaned_data.get("other")
        if game:
            if "Your choice:" in game and len(other) == 0:
                raise forms.ValidationError("If you choose Other, you must type in your choice.")
        return cleaned_data

class VDeveloperForm(forms.Form):
    vdeveloper = forms.ChoiceField(widget=RadioSelect, choices=DEVELOPER, label='Whose vertical scrolling games do you prefer?')

class VCaveForm(forms.Form):
    game = forms.ChoiceField(widget=RadioSelect, choices=CAVE, label='What is your favorite game made by Cave?')
    other = forms.CharField(required=False, label='Other:')

    def clean(self):
        cleaned_data = self.cleaned_data
        game = cleaned_data.get("game")
        other = cleaned_data.get("other")
        if game:
            if "Your choice:" in game and len(other) == 0:
                raise forms.ValidationError("If you choose Other, you must type in your choice.")
        return cleaned_data

class VTreasureForm(forms.Form):
    game = forms.ChoiceField(widget=RadioSelect, choices=TREASURE, label='What is your favorite game made by Treasure?')
    other = forms.CharField(required=False, label='Other:')

    def clean(self):
        cleaned_data = self.cleaned_data
        game = cleaned_data.get("game")
        other = cleaned_data.get("other")
        if game:
            if "Your choice:" in game and len(other) == 0:
                raise forms.ValidationError("If you choose Other, you must type in your choice.")
        return cleaned_data


FORMS = [ControllerForm, GateForm, ScrollingForm, HGameForm, VDeveloperForm,
         VCaveForm, VTreasureForm]

class SurveyWizard(FormWizard):
    def done(self, request, form_list):
        return render_to_response('results.html', {
            'form_data': [form.cleaned_data.iteritems() for form in form_list],
        })
    def process_step(self, request, form, step):
        if hasattr(form, 'cleaned_data'):
            self.form_list = self.form_list[0:step+1]
            if form.cleaned_data.get('controller', None) is not None:
                self.form_list.extend(FORMS[1:])
                if form.cleaned_data['controller'] != 'Arcade Stick':
                    self.form_list.pop(step+1)
            if form.cleaned_data.get('gate', None) is not None:
                self.form_list.extend(FORMS[2:])
            if form.cleaned_data.get('scrolling', None) is not None:
                self.form_list.extend(FORMS[3:])
                if form.cleaned_data['scrolling'] == 'Horizontal':
                    self.form_list.pop(step+2)
                    self.form_list.pop(step+2)
                    self.form_list.pop(step+2)
                else:
                    self.form_list.pop(step+1)
            if form.cleaned_data.get('vdeveloper', None) is not None:
                self.form_list.extend(FORMS[5:])
                if form.cleaned_data['vdeveloper'] == 'Cave':
                    self.form_list.pop(step+2)
                else:
                    self.form_list.pop(step+1)
