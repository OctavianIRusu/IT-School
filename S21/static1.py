class UserAccount:

    def __init__(self, email) -> None:
        self.email = email
        self.__favourites_products = []

    def add_fav(self, product):
        self.__favourites_products.append(product)

    @property
    def favourites(self):
        return self.__favourites_products


class Product:

    count = 0  # atribut de clasa / atribut static

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        Product.count += 1

    def add_to_favourites(self, user_account):
        user_account.add_fav(self)

    def __str__(self) -> str:
        return f"<Product name: {self.name}>"

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    user1 = UserAccount("tavi@test.com")
    prod1 = Product("Masline", 34)
    prod2 = Product("Bulion", 5)

    products = (Product("Ulei de masline", 45), (Product("Ceapa", 3)))

    products[-1].add_to_favourites(user1)

    # print(user1.favourites)

    # atributele clasice se acceseaza utilizand numele clasei.numele atributului
    print(Product.count)
    print(prod1.count)

    # prod1.count = 22 # asa nu, se creeaza un atribut de instanta
    Product.count = 45

    print(Product.count)
    print(prod1.count)
    print(prod2.count)

    # prod1.xyz = "Python is fun" # se creeaza un atribut nou pentru obiectul prod1
    # print(prod1.xyz)
