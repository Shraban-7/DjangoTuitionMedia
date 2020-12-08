from django import forms

from tuition.models import TuitionPost


class TuitionPostForm(forms.ModelForm):
    class Meta:
        model = TuitionPost
        exclude = ['available']
