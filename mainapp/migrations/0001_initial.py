# Generated by Django 2.2.13 on 2020-08-14 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.CharField(max_length=11, verbose_name='регистрационный номер заказа')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=8, verbose_name='артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='цена')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='количество товара')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='mainapp.OrderHeader')),
            ],
            options={
                'verbose_name': 'товар в заказе',
                'verbose_name_plural': 'товары в заказе',
                'ordering': ('order',),
            },
        ),
    ]
