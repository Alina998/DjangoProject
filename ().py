# coding: utf-8
from catalog.models import Category

category1 = Category.objects.create(name="Электроника", description="Различная электроника")
category2 = Category.objects.create(name="Одежда",description="Модная одежда")
