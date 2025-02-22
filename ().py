# coding: utf-8
from users.models import CustomUser
user1 = CustomUser .objects.create_user(username='Alina', email='pastaeva98@mail.ru', password='Alina2208+/', phone_number='1234567890', user_country='Russia', user_photo=None)
print(CustomUser.objects.get(username='Alina').id)
