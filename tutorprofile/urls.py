from django.urls import path
from .views import TutorInfoCreate

urlpatterns = [
    path('create/', TutorInfoCreate, name='create_tutor_info'),
    # path('list/', TuitionListView.as_view(), name='list'),
    # path('detail/<int:pk>/', TuitionDetailView.as_view(), name='detail'),
    # path('', Home.as_view(), name='home'),
    # path('filter/', filter, name='filter'),
    # path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
]