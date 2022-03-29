from django.urls import path
from .views import IndexView, CadastroView, ListaView, CarCreate, CarUpdate, CarDelete, CarList

urlpatterns = [

    # path('endereço/', IndexView.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='inicio'),
    path('cadastro/', CarCreate.as_view(), name='cadastro'),

    path('lista/', CarList.as_view(), name='lista'),

    path('estacionar/<int:pk>/', CarUpdate.as_view(), name='estacionar-ou-retirar'),

    path('cardelete/<int:pk>/', CarDelete.as_view(), name='deletar-carro'),



]