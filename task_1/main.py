from model import Shoes
from controller import Controller
from view import View



if __name__ == "__main__":
    product_name = 'Кроссовки'
    sex = 'Мужские'
    color = 'серый'
    price = 2000
    producer = 'Adidas'
    size = 41
    qty = 35


    # Создание экземпляров классов
    model = Shoes(
        product_name=product_name,
        sex=sex,
        color=color,
        price=price,
        producer=producer,
        size=size,
        qty=qty
    )
    view = View()
    controller = Controller(model, view)

    # Добавление заданий
    controller.model.add_product(product_name, sex, color, price, producer, size, qty)

    # Загрузка данных из файла при запуске
    controller.load_product()

    controller.show_product()

    controller.save_product()