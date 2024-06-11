from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name= 'parent', blank=True , null=True, on_delete= models.CASCADE)
    title = models.CharField(verbose_name = 'name', max_length=50)
    description = models.TextField(verbose_name= 'description', blank=True)
    avatar = models.ImageField(blank=True, upload_to='categories/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'
        # verbose_name = 'category'
    
    def __str__(self) -> str:
        return self.title





class Product(models.Model):
    title = models.CharField(verbose_name = 'title', max_length=50)
    description = models.TextField(verbose_name= 'description', blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, verbose_name='categories', blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class File(models.Model):
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    title = models.CharField(verbose_name = 'title', max_length=50)
    file = models.FileField(verbose_name= 'file', upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'

