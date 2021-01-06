from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView

# Create your views here.
from tutorprofile.forms import TutorInfoForm, PersonalInfoForm, PersonalInfoUpdateForm
from tutorprofile.models import TutorInfo, PersonalInformation


# class TutorInfoCreate(CreateView):
#     model = PersonalInformation
#     form_class = PersonalInfoForm
#     template_name = 'profile/tutorInfoCreate.html'


@login_required
def TutorInfoCreate(request):
    if request.method == 'POST':
        u_form = PersonalInfoUpdateForm(request.POST, instance=request.user)
        p_form = PersonalInfoForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = PersonalInfoUpdateForm(instance=request.user)
        p_form = PersonalInfoForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile/tutorInfoCreate.html', context)


class TutorInfoView(ListView):
    model = TutorInfo
    form_class = TutorInfoForm
    template_name = 'profile/tutorInfoList.html'
