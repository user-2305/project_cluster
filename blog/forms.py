from django import forms

class RegionFilterForm(forms.Form):
    region = forms.CharField(label='Регион', max_length=255, required=False)
    district = forms.CharField(label='Округ', max_length=255, required=False)