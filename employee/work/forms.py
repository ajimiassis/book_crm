from django import forms
from work.models import Emp,Book,Details,Students

class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()

#class BookForm(forms.Form):
#    title=forms.CharField()
#    author=forms.CharField()
#    publication_year=forms.CharField()
#    genre=forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        #fields=['title','author','publication_year','genre']

class DetailsForm(forms.ModelForm):
    class Meta:
        model=Details
        fields='__all__'

class StudentsForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'
