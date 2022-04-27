import django


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('membro/<int:membro_id>', views.membro, name='membro'),
    path('cria/membro', views.cria_membro, name='cria_membro'),
    path('bandos', views.bandos, name='bandos'),
    path('cria/bando', views.cria_bando, name='cria_bando'),
    path('bando/<int:bando_id>', views.bando, name='bando'),
    path('akumas', views.akumas, name='akumas'),
    path('cria/akuma', views.cria_akuma, name='cria_akuma'),
    path('akuma/<int:akuma_id>', views.akuma, name='akuma'),
    path('membro/<int:membro_id>/delete', views.deleta_membro, name='deleta_membro'),
    path('akuma/<int:akuma_id>/delete', views.deleta_akuma, name='deleta_akuma'),
    path('bando/<int:bando_id>/delete', views.deleta_bando, name='deleta_bando'),
    path('edita/membro/<int:membro_id>', views.edita_membro, name='edita_membro'),
    path('edita/bando/<int:bando_id>', views.edita_bando, name='edita_bando'),
    path('edita/akuma/<int:akuma_id>', views.edita_akuma, name='edita_akuma')
]
