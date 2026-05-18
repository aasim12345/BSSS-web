from django import forms

from .models import teacher
from .models import assessment





class InputForm(forms.ModelForm):

    class Meta:

        model = teacher

        fields = ['Name', 'Area']
class InputForm2(forms.ModelForm):

    class Meta:

        model = assessment

        fields = ['Name', 'Topic', 'teacher']

