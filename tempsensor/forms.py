from django import forms

class TempForm(forms.Form):
    new_temp = forms.IntegerField(label = 'Temp_F', max_value='110')
