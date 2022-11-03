from django.urls import path

from . import views                                                      # views modelin tanitmi

app_name = 'sorgu'                                                       # urllerin name vasitesi ile tespiti

urlpatterns = [

    # ex: /sorgu/
    path('', views.esas, name='esas'),                                   # esas sehife urlsi

    # ex: /sorgu/5/
    path('<int:niko_id>/', views.etrafli, name='etrafli'),              # etrafli sehifesi urlsi

    # ex: /sorgu/5/netice/
    path('<int:niko_id>/netice/', views.netice, name='netice'),         # netice sehifesi urlsi

    # ex: /sorgu/5/vote/
    path('<int:niko_id>/vote/', views.vote, name='vote'),               # sesverme sehifesi urlsi
]
