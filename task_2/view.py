class View:
    @staticmethod
    def display_product(order):
        if not order:
            print("Нет такого блюда...")
        else:
            for item in order:
                print(f"Название блюда: {item['product name']}")
                print(f"Автор блюда: {item['author']}")
                print(f"Тип меню: {item['type menu']}")
                print(f"Описание: {item['description']}")
                print(f"Список ингредиентов: {item['ingredients']}")
                print(f"К какой кухне мира относится: {item['cuisine']}")
                print(f"Ссылка на ресурс: {item['link']}")