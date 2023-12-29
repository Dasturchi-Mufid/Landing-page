# https://bootstraptema.ru/_sf/56/5680.html

from django.db import models

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    icon = models.ImageField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    steps = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'

class Testimonial(models.Model):
    author = models.IntegerField()# Bu yerga hozircha author id si yozilib turadi. Keyinchalik foreignkey orqali ulaymiz
    text = models.TextField()

    def __str__(self):
        return f"{self.author} - {self.text}"
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sharh'
        verbose_name_plural = 'Sharhlar'

class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Obuna'
        verbose_name_plural = 'Obunalar'
    
