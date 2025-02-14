# Домашнее задание № 22 *"Знакомство с Django"*
## Задание 1. Настройка проекта
Создайте новую директорию для проекта и настройте виртуальное окружение.
Инициализируйте новый проект Django внутри этой директории.
Не забудьте про добавление файла *.gitignore* и правила ведения разработки по GitFlow. Создайте ветки *main*, 
*develop* и отдельные ветки для решения домашек. Также не забудьте оформить файл README с описанием проекта.

## Задание 2. Создание и настройка приложения
Создайте новое приложение под названием *catalog* в вашем проекте.
Зарегистрируйте приложение в настройках проекта.
Настройте маршрутизацию для нового приложения, добавив соответствующие URL-адреса.

## Задание 3. Создание шаблонов
Подготовьте два HTML-шаблона: для домашней страницы и для страницы с контактной информацией.
Для стилизации страниц используйте Bootstrap.
Вы можете взять за основу следующие шаблоны:
- [*home.html*](https://drive.google.com/file/d/1YzTf1Rbo4nG7HA267jPnOLiNND8ucHGd/view)
- [*contacts.html*](https://drive.google.com/file/d/1cThfPHMr7srYY9Opk1MK2-AuBnA9T2qq/view).

## Задание 4. Реализация контроллеров
Создайте контроллер для отображения домашней страницы.
Создайте контроллер для отображения страницы с контактной информацией.
Настройте маршрутизацию для этих контроллеров.

## * Дополнительное задание
Реализуйте форму обратной связи на странице контактов.
Настройте обработку данных формы в контроллере, чтобы отображать сообщение об успешной отправке данных.

# Домашнее задание №23 Работа с ORM в Django
## Задание 1
1. Подключите СУБД PostgreSQL для работы в проекте.
2. Создайте базу данных в ручном режиме. Внесите изменения в настройки подключения в файле settings.py.

## Задание 2
В приложении каталога создайте модели Product и Category и опишите для них базовые настройки.
Описание моделей:
1. Product:
- наименование,
- описание,
- изображение,
- категория,
- цена за покупку,
- дата создания,
- дата последнего изменения.
2. Category:
- наименование,
- описание.

## Задание 3
Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:
- создайте миграции для новых моделей;
- примените миграции.

## Задание 4
1. Создайте суперпользователя.
2. Зарегистрируйте модели Product и Category в админке.
3. Настройте отображение для моделей:
- Для Category выведите id и name в списке.
- Для Product выведите id, name, price и category в списке.
- Настройте фильтрацию продуктов по категории. Настройте поиск по полям name и description.

## Задание 5
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры.
1. Войдите в Django shell.
2. Создайте несколько категорий и продуктов.
3. Выполните следующие запросы:
- Получите все категории.
- Получите все продукты.
- Найдите все продукты в определенной категории.
- Обновите цену для определенного продукта.
- Удалите продукт.

## Задание 6
Сформируйте фикстуры для моделей Category и Product.

## Задание 7
1. Создайте кастомную команду для добавления тестовых продуктов.
2. В команде удалите все существующие данные из базы перед добавлением новых продуктов.

# Домашнее задание №24 Шаблонизация
## Задание 1
Создайте новый контроллер и шаблон для отображения страницы с подробной информацией о товаре.
На этой странице должна быть показана вся информация о товаре.

## Задание 2
Добавьте в шаблон главной страницы код для отображения списка товаров с помощью цикла.
Чтобы карточки товаров выглядели одинаково, обрежьте отображаемое описание до первых 100 символов.

## Задание 3
Из-за увеличения количества шаблонов возникает много повторяющегося кода.
Выделите общий (базовый) шаблон, который будет включать общие элементы страницы, такие как шапка, подвал и стили.
Также создайте подшаблон для главного меню, который можно будет включать в другие шаблоны.

## * Дополнительное задание
Реализуйте страницу с формой, которая позволит пользователю добавлять новые товары.
Обработайте ввод данных и сохраните новый товар в базу данных.
Добавьте функциональность для постраничного вывода списка товаров на главной странице.
Убедитесь, что пользователи могут легко переходить между страницами списка товаров.

# Домашнее задание №25 FBV и CBV
## Задание 1
Переведите имеющиеся в проекте контроллеры с FBV на CBV.

## Задание 2
Создайте новое приложение для блога и добавьте его в файл settings.py.
Создайте новую модель блоговой записи со следующими полями:
- заголовок,
- содержимое,
- превью (изображение),
- дата создания,
- признак публикации (булевое поле),
- количество просмотров.
Для работы с блогом реализуйте полный CRUD для новой модели, используя CBV.

## Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:
1. Увеличение счетчика просмотров: при открытии отдельной статьи увеличивать счетчик просмотров.
2. Фильтрация опубликованных статей: выводить в список статей только те, которые имеют положительный признак публикации.
3. Перенаправление после редактирования: после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.


# Домашнее задание 26.1 Формы
## Задание 1
Реализуйте механизм **CRUD** для модели продуктов, используя модуль *django.forms*. 
При этом необходимо обезопасить сайт от спама и не разрешать присваивать продуктам названия и добавлять в описание слова, 
которые включены в список запрещенных слов.
Реализуйте валидацию формы, чтобы проверять отсутствие этих слов (в любом регистре) в данных полях.
Запрещенные слова, которые нельзя использовать в названиях и описаниях продуктов:
- казино,
- криптовалюта,
- крипта,
- биржа,
- дешево,
- бесплатно,
- обман,
- полиция,
- радар.

## Задание 2
Добавьте кастомную валидацию для поля *price* в форме создания и редактирования продуктов.
Валидация должна проверять, что цена продукта не может быть отрицательной. Реализуйте это с использованием метода 
*clean_price* в форме. Если цена введена неправильно, отобразите соответствующее сообщение пользователю.

## Задание 3
Добавьте стилизацию форм для продуктов, используя метод *__init__*. Убедитесь, что формы соответствуют общей стилистике платформы.

## * Дополнительное задание
Реализуйте механизм, при котором пользователи могут загружать изображения продуктов.
Добавьте валидацию для поля загрузки изображения, чтобы проверить формат и размер загружаемого файла.
Убедитесь, что загружаемые файлы имеют формат *JPEG* или *PNG* и не превышают размер 5 МБ.


# Домашнее задание 27 Аутентификация в веб-приложениях
## Задание 1
1. Создайте новое приложение для работы с пользователями в вашем проекте Django.
2. Определите модель пользователя с использованием AbstractUser, задав электронную почту как поле для авторизации.
3. Добавьте дополнительные поля в модель пользователя:
- аватар (изображение),
- номер телефона,
- страна.

## Задание 2
В сервисе реализуйте функцию аутентификации, а именно:
1. Регистрация пользователя:
- Создайте форму для регистрации пользователя с полями электронной почты и пароля.
- Добавьте логику регистрации в представлении, позволяя пользователю создать учетную запись.
- Реализуйте отправку приветственного письма пользователю после регистрации.
2. Авторизация пользователя:
- Настройте форму и представление для авторизации пользователя по электронной почте и паролю.

## Задание 3
Закройте доступ к страницам, связанным с управлением продуктами, для анонимных пользователей.
Убедитесь, что только авторизованные пользователи могут просматривать, создавать, изменять и удалять продукты.
Общедоступной должна остаться только страница просмотра списка товаров.