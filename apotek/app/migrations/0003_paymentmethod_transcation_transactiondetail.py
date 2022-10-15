# Generated by Django 4.1.1 on 2022-10-15 12:21

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_is_active_productcategory_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transcation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_date', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('bayar', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('kemnbali', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.customer')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.paymentmethod')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('product_variant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.productvariant')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.transcation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
