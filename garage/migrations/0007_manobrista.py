# Generated by Django 3.1.2 on 2022-03-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0006_auto_20220329_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manobrista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estacionado', models.CharField(choices=[('E', 'Estacionado'), ('N', 'Nao estacionado')], max_length=1)),
                ('pagamento', models.CharField(choices=[('P', 'Pago'), ('D', 'Debito')], max_length=1)),
            ],
        ),
    ]