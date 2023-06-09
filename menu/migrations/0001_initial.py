# Generated by Django 4.2.1 on 2023-05-30 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('Site_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255, verbose_name='Dish name')),
                ('serving_size', models.CharField(choices=[('L', 'Large'), ('S', 'Small'), ('M', 'Medium'), ('F', 'Full'), ('H', 'Half')], default='L', max_length=255)),
                ('food_price', models.IntegerField(verbose_name='Dish price')),
                ('final_output_price', models.IntegerField(blank=True, null=True, verbose_name='Dish Output price')),
                ('food_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Foodorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_owner', models.CharField(default='', max_length=255)),
                ('i_d', models.IntegerField()),
                ('name', models.TextField(max_length=255, verbose_name='Order item name')),
                ('price', models.IntegerField(verbose_name='Order item price')),
                ('quantity', models.IntegerField(default=0, verbose_name='Order item quantity')),
                ('cart_used', models.ManyToManyField(to='menu.cart')),
            ],
        ),
    ]
