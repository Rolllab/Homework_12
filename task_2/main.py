from model import Menu
from controller import Controller
from view import View



if __name__ == "__main__":
    product_name = 'Борщ'
    author = 'Волков Дмитрий'
    type_menu = 'первое'
    description = 'очень вкусное первое'
    ingredients = ['Вода', 'мясо', 'картофель', 'свекла', 'морковь', 'лук', 'капуста']
    cuisine = 'Русская'
    link = 'https://mysite.myhost'


    # Создание экземпляров классов
    model = Menu(
        product_name=product_name,
        author=author,
        type_menu=type_menu,
        description=description,
        ingredients=ingredients,
        cuisine=cuisine,
        link=link
    )
    view = View()
    controller = Controller(model, view)

    # Добавление заданий
    controller.model.add_product(product_name, author, type_menu, description, ingredients, cuisine, link)

    # Загрузка данных из файла при запуске
    controller.load_product()

    controller.show_product()

    controller.save_product()

    controller.model.order_completed()