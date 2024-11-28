from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import RegistrationRequest
from django.core.mail import send_mail
import logging


@receiver(post_save, sender=RegistrationRequest)
def create_user_from_registration(sender, instance, created, **kwargs):
    if instance.is_accepted:  # Ensure this is a new instance being created
        # Check if a user with the same username or email already exists
        if User.objects.filter(username=instance.login).exists():
            logging.warning(f"User with username '{instance.login}' or email '{instance.mail}' already exists. User not created.")
            return  # Exit the function to prevent user creation

        # Create a new user with data from RegistrationRequest
        user = User.objects.create_user(
            username=instance.login,
            email=instance.mail,
            password=instance.password,
            first_name=instance.FIO.split()[0],  # Assume first part of FIO is the first name
            last_name=' '.join(instance.FIO.split()[1:])  # Remaining parts as last name
        )

        # Add user to 'Редактор' group
        editor_group, _ = Group.objects.get_or_create(name='Редактор')
        user.groups.add(editor_group)

        # Optionally set additional attributes for the user
        user.is_staff = True  # Allow access to the admin panel
        user.save()

        message_content = f"""
        Ваши данные:

        ФИО: {instance.FIO}
        Должность: {instance.work_2}
        Место работы: {instance.work_2}
        Email: {instance.mail}
        Логин: {instance.login}
        Пароль: {instance.password}
        """

        try:
            send_mail(
                subject='Вашу заявку на регистрацию одобрили',
                message=message_content,
                from_email='vatagin.01@mail.ru',
                recipient_list=[instance.mail],
                fail_silently=False,
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке письма или сохранении в БД: {e}")