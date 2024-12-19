from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['-id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nomi')
    description = models.TextField(default="Avtor ma'lumot qoshmadi:)", verbose_name='Tavsifi')
    price = models.IntegerField(default=0, verbose_name='Narxi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yuklangan vaqti')
    published = models.BooleanField(default=True, verbose_name='Qoshilganligi',
                                    help_text='Agar bu yerda - "False" bolsa bu gul sotuvda korinmaydi, Agar "True" bolsa korinadi')
    views = models.IntegerField(default=0, verbose_name='Korishlar soni')
    quantity = models.IntegerField(verbose_name='Miqdori')
    photo = models.ImageField(upload_to='post/photos', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriyasi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'
        ordering = ['-id']

