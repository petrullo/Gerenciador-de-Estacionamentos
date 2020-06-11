from django.conf.urls import url, include
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movemensalistas,
)

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^movrotativos/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^mensalistas/$', lista_mensalistas, name='core_lista_mensalistas'),
    url(r'^movemensalistas/$', lista_movemensalistas, name='core_lista_movemensalistas'),
]
