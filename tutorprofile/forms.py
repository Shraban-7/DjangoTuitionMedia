from django import forms

from tutorprofile.models import TutorInfo, PersonalInformation


class TutorInfoForm(forms.ModelForm):
    class Meta:
        model = TutorInfo
        exclude = ['user']
        widgets = {
            'prefer_subjects': forms.CheckboxSelectMultiple(attrs={'multiple': True})
        }


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = ['user']


class PersonalInfoUpdateForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = ['user']
