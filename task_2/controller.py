import json

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.order = model.order # Здесь должны храниться данные, которые нужно отображать
        self.filename = "menu.json"

    def show_product(self):
        """Передает данные из модели в представление для отображения."""
        self.view.display_product(self.order)

    def save_product(self):
        """Сохраняет данные в JSON файл"""
        try:
            with open(self.filename, 'w') as fp:
                json.dump(self.order, fp, ensure_ascii=False, indent=4)
            print('Данные сохранены в файл')
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def load_product(self):
        """Загружает данные из JSON файла"""
        try:
            with open(self.filename, 'r') as f:
                self.order = json.load(f)
            print('Данные загружены из файла')
        except FileNotFoundError:
            print('Файл не найден, создан новый файл')
        except Exception as e:
            print(f"Ошибка при загрузке данных из файла: {e}")