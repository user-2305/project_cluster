from django import forms

class RegionFilterForm(forms.Form):
    region = forms.CharField(label='Регион', max_length=255, required=False)
    district = forms.CharField(label='Округ', max_length=255, required=False)
    indicator = forms.CharField(label='Индикатор', max_length=255, required=False)
    amount = forms.IntegerField(label='Количество', required=False)
    year = forms.IntegerField(label='Год', required=False)

class EmploymentFilterForm(forms.Form):
    region = forms.CharField(label='Регион', max_length=255, required=False)
    district = forms.CharField(label='Округ', max_length=255, required=False)
    indicator = forms.CharField(label='Индикатор', max_length=255, required=False)
    min_percentage = forms.DecimalField(label='Количество(мин)', max_digits=4, decimal_places=1, required=False)
    max_percentage = forms.DecimalField(label='Количество(макс)', max_digits=4, decimal_places=1, required=False)
    year = forms.IntegerField(label='Год', required=False)

class АgricultureFilterForm(forms.Form):
    region = forms.CharField(label='Регион', max_length=255, required=False)
    district = forms.CharField(label='Округ', max_length=255, required=False)
    indicator = forms.CharField(label='Индикатор', max_length=255, required=False)
    min_percentage = forms.DecimalField(label='Количество(мин)', max_digits=5, decimal_places=1, required=False)
    max_percentage = forms.DecimalField(label='Количество(макс)', max_digits=5, decimal_places=1, required=False)
    year = forms.IntegerField(label='Год', required=False)
