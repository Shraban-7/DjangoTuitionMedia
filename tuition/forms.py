from django.forms import ModelForm

from tuition.models import TuitionPost


class TuitionPostForm(ModelForm):
    class Meta:
        model = TuitionPost
        fields = ('fullname', 'country', 'class_other', 'medium', 'subjects', 'school_college',
                  'student_quantity', 'student_gender', 'detail_tuition', 'day_per_week', 'salary',
                  'desire_tutor_gender', 'preference_tuition_style', 'address', 'mobile', 'email',)
        # fields = '__all__'
        # exclude = ("sno", "available")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()
    #
    #     if 'country' in self.data:
    #         try:
    #             country_id = int(self.data.get('country'))
    #             self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
