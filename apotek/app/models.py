from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import UserManager, AbstractUser
import uuid
# Create your models here.


class BaseFieldModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    class Meta:
        abstract = True


class BaseEntryModel(BaseFieldModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseEntryModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True, default=None, blank=True)
    email = models.EmailField(unique=True, validators=[validate_email])
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        'self', related_name='user_createdby', null=True, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(
        'self', related_name='user_updatedby', null=True, on_delete=models.SET_NULL)


class Role(BaseFieldModel):
    name = models.CharField(max_length=50, unique=True)


class WorkerRole(BaseEntryModel):
    worker = models.ForeignKey(to='Worker', on_delete=models.CASCADE)
    role = models.ForeignKey(to=Role, on_delete=models.RESTRICT)
    created_by = models.ForeignKey('Worker', related_name="%(app_label)s_%(class)s_createdby",
                                   null=True, on_delete=models.SET_NULL, blank=True)
    updated_by = models.ForeignKey('Worker', related_name="%(app_label)s_%(class)s_updatedby",
                                   null=True, on_delete=models.SET_NULL, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['worker', 'role'], name='unique_worker_role')]


class Worker(AbstractUser):
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True, default=None, blank=True)
    roles = models.ManyToManyField(to=Role, through=WorkerRole,
                                   through_fields=('worker', 'role'), related_name='workers')

class Supplier(User):
    city = models.CharField(max_length=255)


class Sales(User):
    supplier = models.ForeignKey


class Customer(User):
    CHOICE = (
        (1, 'MALE'),
        (2, "FEMALE")
    )
    gender = models.IntegerField(choices=CHOICE)
    profession = models.CharField(max_length=255, null=True)
    birth_date = models.DateField()
    nik = models.CharField(max_length=255)


class Product(BaseEntryModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('ProductCategory', on_delete=models.RESTRICT)


class ProductCategory(BaseEntryModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)


class ProductVariant(BaseEntryModel):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    unit = models.ForeignKey('ProductUnit', on_delete=models.RESTRICT)


class ProductUnit(BaseEntryModel):
    name = models.CharField(max_length=255)


class ProductDetail(BaseEntryModel):
    exp_date = models.DateField(null=False)
    stock = models.IntegerField(null=True)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    ppn = models.IntegerField(null=True)
    dicount = models.IntegerField(null=True)
    barcode = models.CharField(null=True, max_length=255)
    final_price = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
