from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Carro
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class CadastroView(TemplateView):
    template_name = 'cadastro.html'

class ListaView(TemplateView):
    template_name = 'lista.html'

class CarCreate(CreateView):
    model = Carro
    fields = ['placa', 'fabricante','modelo','cor']
    template_name = 'cadastro.html'
    success_url = reverse_lazy('lista')

class CarUpdate(UpdateView):
    model = Carro
    fields = ['placa','parado']
    template_name = 'valet.html'
    success_url = reverse_lazy('lista')

class CarDelete(DeleteView):
    model = Carro
    template_name = 'cardelete.html'
    success_url = reverse_lazy('lista')

class CarList(ListView):
    model = Carro
    template_name = 'lista.html'


            ## Busca ##
    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            carro = Carro.objects.filter(placa__icontains=txt_nome)
        else:
            carro = Carro.objects.all()

        return carro