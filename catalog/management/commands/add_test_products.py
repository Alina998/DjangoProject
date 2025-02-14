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
        Product.objects.create(name='iPhone 13', description='Смартфон Apple iPhone 13 оснащен 6.1-дюймовым дисплеем OLED – энергоэффективным и контрастным даже при ярком солнечном свете.'
                                                             'А прочный корпус надежно защищен от воды и пыли.', category=electronics, price=699.99)
        Product.objects.create(name='Футболка', description='Предоставляем вашему вниманию стильную и удобную футболку оверсайз!'
                                                            'Эта вещь станет незаменимым аксессуаром для тех, кто ценит комфорт и следит за трендами.', category=clothing, price=19.99)
        Product.objects.create(name='Худи',
                               description='Оверсайз худи, которое вы искали! Толстовка свободного силуэта, с увеличенной проймой, шириной рукавов и спущенной плечевой линией.'
                                           'Базовая и универсальная толстовка с капюшоном выполнена из мягкого хлопка, приятна к телу и точно станет самой любимой.',
                               category=clothing, price=19.99)

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены.'))
