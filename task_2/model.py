class Menu:
    def __init__(self, product_name: str, author: str, type_menu: str, description: str, ingredients: list, cuisine: str, link: str):
        self.product_name = product_name  # Название блюда
        self.author = author              # Автор блюда
        self.type_menu = type_menu        # Тип меню (первое, второе, десерт или др.)
        self.description = description    # Текстовое описание блюда
        self.ingredients = ingredients    # Список ингредиентов
        self.cuisine = cuisine            # К какой кухне мира относится это блюдо (Итальянская, Русская и т.д.)
        self.link = link                  # Ссылка на ресурс
        self.order = []                   # Заказ клиента

    def order_progress(self):
        print(f'Ваш заказ - {self.product_name} - взяли в работу...')
        print('-' * 50)

    def order_completed(self):
        print('-' * 50)
        print(f'Ваш заказ - {self.product_name} - выполнен...')

    def add_product(self, product_name, author, type_menu, description, ingredients, cuisine, qty):
        """Добавляет данные о заказе в список для отображения."""
        menu = {
            "product name": product_name,
            "author": author,
            "type menu": type_menu,
            "description": description,
            "ingredients": ingredients,
            "cuisine": cuisine,
            "link": qty
        }
        self.order.append(menu)
        self.order_progress()