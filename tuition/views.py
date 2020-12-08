from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView

# Create your views here.
from tuition.forms import TuitionPostForm
from tuition.models import TuitionPost, District, Area, Subject, Class, Medium
from django.db.models import Q, query


class TuitionPostCreateView(CreateView):
    model = TuitionPost
    form_class = TuitionPostForm
    template_name = 'tuition/TuitionPostCreate.html'
    success_url = '/'


class TuitionListView(ListView):
    model = TuitionPost
    template_name = 'tuition/TuitionPostList.html'
    ordering = ['-created_at']
    paginate_by = 2


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['districts'] = District.objects.all().order_by('name')
        context['areas'] = Area.objects.all().order_by('name')
        context['subjects'] = Subject.objects.all().order_by('name')
        context['classes'] = Class.objects.all().order_by('name')
        context['mediums'] = Medium.objects.all().order_by('name')
        return context


class TuitionDetailView(DetailView):
    model = TuitionPost
    template_name = 'tuition/TuitionPostDetail.html'


class Home(TemplateView):
    template_name = 'base.html'


def filter(request):
    if request.method == "POST":
        district = request.POST['district_i']
        area = request.POST['area_i']
        subject = request.POST['subject_i']
        class_other = request.POST['class_i']
        medium = request.POST['medium_i']

        if subject or class_other or area or district or medium:
            queryset = (Q(district__name__icontains=district)) | (Q(area__icontains=area)) | (
                Q(subjects__icontains=subject)) | (Q(class_other__icontains=class_other)) | (
                           Q(medium__icontains=medium))
            results = TuitionPost.objects.filter(queryset).distinct()
        else:
            results = []
        context = {'results': results}
    return render(request, 'tuition/filter.html', context)
