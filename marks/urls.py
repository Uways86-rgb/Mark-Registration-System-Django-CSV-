from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input-marks/', views.input_marks, name='input-marks'),
    path('view-marks/', views.view_marks, name='view-marks'),
    path('update-marks/', views.update_marks, name='update-marks'),
    path('show_one_record/', views.show_one_record, name='show_one_record'),
    path('delete-marks/', views.delete_marks, name='delete-marks'),
    path('visualisation/', views.visualisation, name='visualisation'),
    path('chart-data/', views.chart_data, name='chart-data'),
]