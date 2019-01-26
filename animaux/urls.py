from django.urls import path
from . import views

app_name = 'animaux'
urlpatterns = [
    path('',views.liste_animaux,name ='liste'),
    path('<int:animaux_id>/detail/',views.detail,name ='detail'),
    path('<int:animaux_id>/results/',views.results,name = 'results'),
    path('<int:animaux_id>/nourrir/',views.nourrir,name ='nourrir'),
    path('<int:animaux_id>/divertir/',views.divertir,name ='divertir'),
    path('<int:animaux_id>/coucher/',views.coucher,name ='coucher'),
    path('<int:animaux_id>/reveiller/',views.reveiller,name ='reveiller'),
]