class View:
    @staticmethod
    def display_product(batch):
        if not batch:
            print("Нет такого товара.")
        else:
            for item in batch:
                print(f"Наименование товара: {item['product name']}")
                print(f"Тип товара: {item['sex']}")
                print(f"Цвет: {item['color']}")
                print(f"Производитель: {item['producer']}")
                print(f"Размер: {item['size']}")
                print(f"Количество на складе: {item['qty']}")