# Generated by Django 4.0.6 on 2024-10-16 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled district', max_length=200, verbose_name='Название района')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled News', max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(default='', verbose_name='Текст')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='RegistrationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(default='Unknown FIO', max_length=200, verbose_name='ФИО')),
                ('work_2', models.CharField(default='Unknown work', max_length=200, verbose_name='Должность')),
                ('mail', models.EmailField(default='Unknown mail', max_length=254, verbose_name='Почта')),
                ('login', models.CharField(default='Unknown login', max_length=40, verbose_name='Логин')),
                ('password', models.CharField(default='123', max_length=18, verbose_name='Пароль')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='Принята')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Tos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown TOS', max_length=200, verbose_name='Имя')),
                ('addres', models.CharField(max_length=200, verbose_name='Адрес')),
                ('tos_chairperson', models.CharField(max_length=100, verbose_name='ФИО Представителя')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_image/', verbose_name='Фото')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tos.district', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Тос',
                'verbose_name_plural': 'Тосы',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_image/', verbose_name='Изображение')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tos.news')),
            ],
            options={
                'verbose_name': 'изображение новости',
                'verbose_name_plural': 'изображения новостей',
            },
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled doc', max_length=200, verbose_name='Имя')),
                ('pdf_document', models.FileField(blank=True, max_length=200, null=True, upload_to='pdfs/', verbose_name='PDF Документ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'документ',
                'verbose_name_plural': 'документы',
            },
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Compititons', max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(default='', verbose_name='Текст')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tos.doc', verbose_name='Утвержденный документ')),
            ],
            options={
                'verbose_name': 'конкурс',
                'verbose_name_plural': 'конкурсы',
            },
        ),
    ]
