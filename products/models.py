import string
from django.db import models
import random
import math
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Device(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'device'
        verbose_name_plural = 'devices'

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='device_image', blank=True, default='device_image/iphone-xsmax.png')
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Type, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_list_by_type', args=[self.slug])


class Model(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    system = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'model'
        verbose_name_plural = 'models'

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    system = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'storage'
        verbose_name_plural = 'storages'

    def __str__(self):
        return self.name


class Memory(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    system = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'memory'
        verbose_name_plural = 'memories'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    system = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'color'
        verbose_name_plural = 'colors'

    def __str__(self):
        return self.name


# Verification Code
def MakeCode():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))


conditions = (
    ('Mint', 'Mint'),
    ('Good', 'Good'),
    ('Fair', 'Fair'),
    ('New', 'New'),
)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    system = models.ForeignKey(Type, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, blank=True)
    edition = (
        ('Duos', 'Dual Sim/Duos'),
        ('Standard', 'Standard'),
    )
    status = (
        ('Active', '1'),
        ('Pending', '2'),
    )

    edition = models.CharField(max_length=10, choices=edition)
    condition = models.CharField(max_length=10, choices=conditions)
    status = models.CharField(max_length=10, choices=status, default='Pending')
    serial = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    express_shipping = models.BooleanField(default=False)
    shipping_location = models.CharField(max_length=10)
    damage_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(7000)])
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=10, default=MakeCode, db_index=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('code',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.code)
        super(Product, self).save(*args, **kwargs)

    @property
    def date(self):
        return self.created.strftime('%B %d, %Y')
    '''
    def fee_get(self):
        price = self.price
        self.fee = math.ceil(price / 100) * 5
        return self.fee
    fee_get = property(fee_get)

    def total_price(self):
        price = self.price
        fee = self.fee
        self.total = price + fee
        return self.total

    total_price = property(total_price)
    '''

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # SENDER
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment	by	{}	on	{}'.format(self.user.email, self.product)


def get_image_filename(instance, filename):
    device = instance.product.device
    slug = slugify(device)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='get_image_filename', verbose_name='Image')

    def __str__(self):
        return 'Image for  {}'.format(self.product.code)
