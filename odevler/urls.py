from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('teslimler/', views.teslim_edilen_list, name='teslim_listesi'),
    path('giris/', views.student_user, name='giris'),
    path('cikis/', views.kullanici_cikis, name='cikis'),
    path('api/studentlar/', views.api_students, name='api_studentlar'),
    path('api/examlar/', views.api_exams, name='api_examlar'),
    path('api/teslimler/', views.api_deadlines, name='api_teslimler'),
]


