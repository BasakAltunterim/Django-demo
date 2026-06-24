from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('teslimler/',views.teslim_edilen_list,name='teslim_listesi')
]


