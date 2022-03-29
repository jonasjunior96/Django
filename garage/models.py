from django.db import models

# Create your models here.
## gerir pagamentos e estatus do carro ##
class Manobrista(models.Model):
    manobra = (
        ("E", "Estacionado"),
        ("N", "Nao estacionado"),
    )

    pago = (
        ("P", "Pago"),
        ("D", "Debito"),
    )
    estacionado = models.CharField(max_length=1, choices=manobra, blank=False, null=False)
    pagamento = models.CharField(max_length=1, choices=pago, blank=False, null=False)

    if pagamento==False and estacionado==True:
        saida = models.BooleanField(default=False)
    else:
        saida = models.BooleanField(default=True)


class Carro(models.Model):

    placa = models.CharField(max_length=8, unique=True)
    cor = models.CharField(max_length=15)
    fabricante = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    dataentrada = models.DateTimeField(auto_now_add=True)
    parado = models.BooleanField(default=False)
    date_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Placa: {} - Data Criaçao: {}".format(self.placa, self.dataentrada)
