# from abc import ABC, abstractmethod
#
#
# class Book:
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre
#
#
# class OrderSource(ABC):
#     @abstractmethod
#     def get_order(self, user: str) -> Book:
#         pass
#
#
# class DictOrderSource(OrderSource):
#     def __init__(self, orders):
#         self.orders = orders
#
#     def get_order(self, user: str) -> Book:
#         return self.orders.get(user)
#
#
# class FileOrderSource(OrderSource):
#     def __init__(self, filepath):
#         self.filepath = filepath
#
#     def get_order(self, user: str) -> Book:
#         import json
#         with open(self.filepath, 'r') as file:
#             orders = json.load(file)
#             if user in orders:
#                 book_data = orders[user]
#                 return Book(**book_data)
#         return None
#
#
# class DeliveryMethod(ABC):
#     @abstractmethod
#     def send(self, user: str, book: Book):
#         pass
#
#
# class EmailDelivery(DeliveryMethod):
#     def __init__(self, email_provider):
#         self.email_provider = email_provider
#
#     def send(self, user: str, book: Book):
#         print(f"Отправляем книгу '{book.title}' авторства {book.author} пользователю {user} на почтовый адрес {self.email_provider[user]}")
#
#
# class PackageDelivery(DeliveryMethod):
#     def __init__(self, service_name):
#         self.service_name = service_name
#
#     def send(self, user: str, book: Book):
#         print(f"Отправляем книгу '{book.title}' авторства {book.author} пользователю {user} через сервис {self.service_name}")
#
# class App:
#     def __init__(self, order_source: OrderSource, delivery_method: DeliveryMethod):
#         self.order_source = order_source
#         self.delivery_method = delivery_method
#
#     def send_book(self, user: str):
#         book = self.get_book_stored_by_user(user)
#         if book:
#             self.delivery_method.send(user, book)
#         else:
#             print(f"Для пользователя {user} заказ не найден")
#
#     def get_book_stored_by_user(self, user: str) -> Book:
#         return self.order_source.get_order(user)
#
#
# if __name__ == "__main__":
#
#     orders_dict = {
#         "alice": Book("1984", "George Orwell", "Dystopia"),
#         "bob": Book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
#     }
#
#     email_provider = {
#         "alice": "alice@example.com",
#         "bob": "bob@example.com"
#     }
#
#
#     order_source = DictOrderSource(orders_dict)
#     delivery_method = EmailDelivery(email_provider)
#
#     app = App(order_source, delivery_method)
#     app.send_book("alice")
#     app.send_book("bob")
