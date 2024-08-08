

from django import forms

from students.models import College


class StudentForm(forms.Form):
    rollNo = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'rollNo', 'class':'rollNoClass'}))
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=50)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':"className"}))
    college = forms.ModelChoiceField(queryset=College.objects.all(),
                                      empty_label="Select college",
                                      to_field_name='id',)
    
    
