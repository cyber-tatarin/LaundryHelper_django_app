from django.forms import ModelForm
from .models import Colors
from django import forms


class CreateThingForm(forms.Form):
    title = forms.CharField(max_length=100, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'id': "thing-title",
                                                          'aria-describedby': "titleHelp"}))

    color = forms.ChoiceField(widget=forms.RadioSelect())

    temperature = forms.IntegerField(required=True,
                                     widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'id': "thing-temp",
                                                                     'aria-describedby': "tempHelp"}))

    mass = forms.IntegerField(required=False,
                              widget=forms.NumberInput(attrs={'class': 'form-control',
                                                              'id': "thing-mass",
                                                              'aria-describedby': "massHelp"}),
                              initial=200)

    photo = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control',
                                                           'id': 'formFile'}))

    def __init__(self, colorChoices, *args, **kwargs):
        super(CreateThingForm, self).__init__(*args, **kwargs)
        self.fields['color'].choices = colorChoices


class CreateColorForm(ModelForm):
    class Meta:
        model = Colors
        fields = ['color', 'image']

        widgets = {
            'color': forms.TextInput(attrs={'class': 'form-control',
                                            'id': "color-title",
                                            'aria-describedby': "colorHelp"}),

            'image': forms.FileInput(attrs={'class': 'form-control',
                                            'id': 'formFile'})
        }
