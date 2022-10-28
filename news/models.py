from django.db import models


class News(models.Model):
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
    
    title = models.CharField(max_length=50, verbose_name='заголовок')
    content = models.TextField(verbose_name='контент')
    image = models.ImageField(verbose_name='изображение', upload_to='news_images/')
    date = models.DateTimeField(verbose_name='дата добавление', auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'
    
# Create your models here.
