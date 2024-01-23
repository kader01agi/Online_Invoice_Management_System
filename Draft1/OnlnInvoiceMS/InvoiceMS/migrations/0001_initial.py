# Generated by Django 5.0.1 on 2024-01-22 19:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientUserID', models.CharField(max_length=50, unique=True)),
                ('ClientName', models.CharField(max_length=100)),
                ('ClientEmail', models.EmailField(max_length=254)),
                ('ClientPhone', models.CharField(max_length=20)),
                ('ClientAddress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PaymentStatus', models.CharField(max_length=20)),
                ('DueDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=100)),
                ('ItemBrand', models.CharField(max_length=50)),
                ('ItemDescription', models.TextField()),
                ('ItemUnitPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ItemQuantity_in_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalesmanName', models.CharField(max_length=100)),
                ('SalesmanEmail', models.EmailField(max_length=254)),
                ('SalesmanPhone', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('InvoiceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.invoice')),
                ('ItemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.client')),
                ('ItemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.item')),
                ('SalesmanID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.salesman')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='OrderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.order'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentDate', models.DateField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('PaymentMethod', models.CharField(max_length=50)),
                ('InvoiceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceMS.invoice')),
            ],
        ),
    ]
