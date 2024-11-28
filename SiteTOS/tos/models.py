from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image as PILImage
from django.conf import settings



class News(models.Model):
    title = models.CharField(max_length=200,default='Untitled News',verbose_name='Заголовок')
    text = models.TextField(default='',verbose_name='Текст')
    #image = models.ImageField(upload_to='news_image/', blank=True, null=True,verbose_name='Изображение')
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ['-pub_date']

class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_image/', verbose_name='Изображение')

    class Meta:
        verbose_name = "изображение новости"
        verbose_name_plural = "изображения новостей"

    def __str__(self):
        return f"Image for {self.news.title}"

class Competitions(models.Model):
    title = models.CharField(max_length=200,default='Untitled Compititons',verbose_name='Заголовок')
    text = models.TextField(default='',verbose_name='Текст')
    date = models.DateTimeField(default=timezone.now,verbose_name='Дата')
    document = models.ForeignKey('Doc',on_delete=models.SET_NULL,blank=True, null=True,verbose_name='Утвержденный документ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "конкурс"
        verbose_name_plural = "конкурсы"



class Doc(models.Model):
    name = models.CharField(max_length=200, default='Untitled doc', verbose_name='Имя')
    pdf_document = models.FileField(max_length=200, upload_to='pdfs/', verbose_name='PDF Документ', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"


class District(models.Model):
    name = models.CharField(max_length=200,default='Untitled district',verbose_name='Название района')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Tos(models.Model):
    name = models.CharField(max_length=200, default='Unknown TOS', verbose_name='Имя')
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Район')
    addres = models.CharField(max_length=200, verbose_name='Адрес')
    tos_chairperson = models.CharField(max_length=100, verbose_name='ФИО Представителя')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    image = models.ImageField(upload_to='news_image/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.image:
            img = PILImage.open(self.image)
            if img.size[0] > 150 or img.size[1] > 150:
                raise ValidationError("Фото может содержать разрешение только 150X150")

    class Meta:
        verbose_name = "Тос"
        verbose_name_plural = "Тосы"


class RegistrationRequest(models.Model):
    FIO = models.CharField(max_length=200, default='Unknown FIO', verbose_name='ФИО')
    work_2 = models.CharField(max_length=200, default='Unknown work', verbose_name='Должность')
    mail = models.EmailField(max_length=254, default='Unknown mail', verbose_name='Почта')
    login = models.CharField(max_length=40, verbose_name='Логин', default='Unknown login')
    password = models.CharField(max_length=18, verbose_name='Пароль', default='123')
    tos = models.ForeignKey(Tos, on_delete=models.CASCADE, verbose_name='Тос',null=True)
    is_accepted = models.BooleanField(default=False, verbose_name='Принята')

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "Заявка"

        verbose_name_plural = "Заявки"
