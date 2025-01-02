from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты'

    def handle(self, *args, **kwargs):
        # Удалите все существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        electronics = Category.objects.create(name='Электроника', description='Различная электроника')
        clothing = Category.objects.create(name='Одежда', description='Модная одежда')

        # Создание продуктов
        Product.objects.create(name='Смартфон', description='Современный смартфон', category=electronics, price=699.99)
        Product.objects.create(name='Футболка', description='Удобная футболка', category=clothing, price=19.99)

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены.'))
