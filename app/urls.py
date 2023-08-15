
from django.urls import path

from . import views
urlpatterns = [
    path('first_api/', views.FirstApiView.as_view(), name='first_api'),
    path('term/', views.TermApiView.as_view(), name='first_api'),
    path('course/', views.CourseApiView.as_view(), name='first_api'),
    ]