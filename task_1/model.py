class Shoes:
    def __init__(self, product_name: str, sex: str, color: str, price: float, producer: str, size: float, qty: int):
        self.product_name = product_name  # Наименование товара
        self.sex = sex                    # Мужская или женская обувь
        self.color = color                # Цвет
        self.price = price                # Цена
        self.producer = producer          # Производитель
        self.size = size                  # Размер
        self._purchased_quantity = qty    # qty- партия товара на складе, приобретенное количество (quantity) товара
        self.allocations = []  # Распределение товара в партии (заказ покупателя (возврат товара) или закупка товара)

    def add_product(self, product_name, sex, color, price, producer, size, qty):
        """Добавляет данные о товаре в список для отображения."""
        batch = {
            "product name": product_name,
            "sex": sex,
            "color": color,
            "price": price,
            "producer": producer,
            "size": size,
            "qty": qty
        }
        self.allocations.append(batch)
        print('Данные о товаре добавлены')

