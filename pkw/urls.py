from django.urls import path
from . import views

app_name = 'pkw'
#
# urlpatterns = [
#     path('stat/kraj/', views.kraj, name='kraj'), # strona główna
#     path('stat/<wojewodztwo>/<int:okreg>/<gmina>/', views.gmina, name='gmina'),
#     path('stat/<wojewodztwo>/<int:okreg>/', views.okreg, name='okreg'),
#     path('stat/<wojewodztwo>/', views.woj, name='woj'),
# ]



urlpatterns = [
    path('', views.kraj, name='kraj'), # strona główna
    path('<wojewodztwo>/<int:okreg>/<gmina>/', views.gmina, name='gmina'),
    path('<wojewodztwo>/<int:okreg>/', views.okreg, name='okreg'),
    path('<wojewodztwo>/', views.woj, name='woj'),
]