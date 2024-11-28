from django.shortcuts import render,redirect,get_object_or_404
from .models import Competitions,News,Doc
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Tos
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.conf import settings
from email.mime.text import MIMEText
import smtplib
import logging
from .models import RegistrationRequest


def gl(request):
    queryset = News.objects.prefetch_related('images').all()
    context = {'contests': queryset}
    return render(request, "index.html", context)

def doc(request):
    queryset = Doc.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        queryset = queryset.filter(name__icontains=search_query)

    sort_order = request.GET.get('sort', 'asc')
    if sort_order == 'desc':
        queryset = queryset.order_by('-name')
    else:
        queryset = queryset.order_by('name')

    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'contests': page_obj,
        'search_query': search_query,
        'sort_order': sort_order,
    }

    return render(request, "doc.html", context)

def tos(request):
    tos_by_district = {}
    tos_list = Tos.objects.select_related('district').all()
    for tos in tos_list:
        district_name = tos.district.name
        if district_name not in tos_by_district:
            tos_by_district[district_name] = []
        tos_by_district[district_name].append(tos)

    return render(request, 'tos.html', {'tos_by_district': tos_by_district})


def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, 'Неверный логин или пароль.')
            return render(request,"auth.html")

    return render(request, "auth.html")

def comp(request):
    queryset = Competitions.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        queryset = queryset.filter(title__icontains=search_query)

    sort_order = request.GET.get('sort', 'asc')
    if sort_order == 'desc':
        queryset = queryset.order_by('-title')
    else:
        queryset = queryset.order_by('title')

    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'contests': page_obj,
        'search_query': search_query,
        'sort_order': sort_order,
    }

    return render(request, "comp.html", context)

def news(request):
    #queryset = News.objects.all()
    #paginator = Paginator(queryset, 9)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #
    #for news_item in page_obj:
    #    news_item.first_image = news_item.images.first()
    #
    #context = {'contests': page_obj}
    #return render(request, "news.html", context)


    queryset = News.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        queryset = queryset.filter(title__icontains=search_query)

    sort_order = request.GET.get('sort', 'asc')
    if sort_order == 'desc':
        queryset = queryset.order_by('-title')
    else:
        queryset = queryset.order_by('title')

    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for news_item in page_obj:
        news_item.first_image = news_item.images.first()

    context = {
        'contests': page_obj,
        'search_query': search_query,
        'sort_order': sort_order,
    }

    return render(request, "news.html", context)

def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    images = news_item.images.all()  # Retrieve all related images

    context = {
        'news_item': news_item,
        'images': images,
    }
    return render(request, 'news_detail.html', context)

def registration(request):
    tos_list = Tos.objects.all()  # Fetch all TOS instances

    if request.method == 'POST':
        username = request.POST['username']
        position = request.POST['position']
        tos = request.POST['tos']
        mail = request.POST['mail']
        login = request.POST['login']
        password = request.POST['password']

        #tos_instance = Tos.objects.get(id=int(tos_id))
        tos_instance = Tos.objects.get(name=tos)  # Assuming you're using Django ORM
        #request.tos = tos_instance

        # Create new registration request with selected TOS
        new_request = RegistrationRequest(
            FIO=username,
            work_2=position,
            mail=mail,
            login=login,
            password=password,
            tos = tos_instance
        )

        new_request.save()  # Save the new record

        message_content = f"""
        Новая заявка на регистрацию:

        ФИО: {username}
        Должность: {position}
        Тос: {position}
        Email: {mail}
        Логин: {login}
        Пароль: {password}
        """

        try:
            send_mail(
                subject='Заявка на регистрацию нового пользователя',
                message=message_content,
                from_email='vatagin.01@mail.ru',
                recipient_list=[mail],
                fail_silently=False,
            )

            messages.success(request, 'Регистрация прошла успешно! Проверьте вашу почту.')
            return redirect('auth')

        except Exception as e:
            logging.error(f"Ошибка при отправке письма или сохранении в БД: {e}")
            messages.error(request, f'Произошла ошибка при отправке сообщения или сохранении данных: {str(e)}')

        return redirect('home')

    return render(request, "Registration.html", {'tos_list': tos_list})
    #return render(request, "Registration.html")