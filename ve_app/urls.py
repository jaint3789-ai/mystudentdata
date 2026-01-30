from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view),
    path('second/', views.second),
    path('html/', views.send_html_file),
    path('form/', views.send_form ),
    path('third/', views.home_view ),
    path('fourth/', views.rooms ),
    path('fifth/', views.myimage ),
    path('students/', views.student_data ),
] 