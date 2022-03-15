from time import sleep


class Restaurant(object):
    def __str__(self):
        return f"This restaurant had {self._orders} orders today for a total of {self._total_sales} in sales"

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print(f"  Creating new Restaurant instance")
            cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
            cls._orders = 0
            cls._total_sales = 0
        else:
            print(f"  Using instance")

        return cls._instance

    def order_food(self, food_type):
        food = Food.order_food(food_type)
        self._orders += 1
        self._total_sales = self._total_sales + food.price()


class CheeseBurger:

    def __init__(self):
        self._price = 5.99

    def __str__(self):
        return f"{__class__.__name__}: {self._price}"

    def price(self):
        return self._price

    def prepare(self):
        print(f"{__class__.__name__}: grill all-beef patty")
        sleep(1)
        print(f"{__class__.__name__}: flip patty")
        sleep(1)
        print(f"{__class__.__name__}: put cheese on patty")
        sleep(1)
        print(f"{__class__.__name__}: put patty on bun and add toppings")
        sleep(1)
        print(f"{__class__.__name__}: All done!")
        print(f"{__class__.__name__}: {self._price}")


class Pasta:
    def __init__(self):
        self._price = 8.99

    def __str__(self):
        return f"{__class__.__name__}: {self._price}"

    def price(self):
        return self._price

    def prepare(self):
        print(f"{__class__.__name__}: boil water for noodles")
        sleep(2)
        print(f"{__class__.__name__}: Saute onions, garlic and tomatoes for sauce")
        sleep(2)
        print(f"{__class__.__name__}: put noodles in water")
        sleep(2)
        print(f"{__class__.__name__}: season the sauce ")
        sleep(2)
        print(f"{__class__.__name__}: plate noodles and add sauce on top  ")
        sleep(2)
        print(f"{__class__.__name__}: All done!")
        print(f"{__class__.__name__}: {self._price}")


class Taco:
    def __init__(self):
        self._price = 1.99

    def __str__(self):
        return f"{__class__.__name__}: {self._price}"

    def price(self):
        return self._price

    def prepare(self):
        print(f"{__class__.__name__}: get the tortilla")
        sleep(2)
        print(f"{__class__.__name__}: cook meat")
        sleep(2)
        print(f"{__class__.__name__}: put meat on tortilla")
        sleep(2)
        print(f"{__class__.__name__}: put fresh onion and cilantro on top of meat")
        sleep(2)
        print(f"{__class__.__name__}: All done!")
        print(f"{__class__.__name__}: {self._price}")


# Factory class for specific food classes
class Food:
    def __init__(self):
        print("called __init__ of Food class")

    def price(self):
        return 0

    def prepare(self):
        pass

    @staticmethod
    def order_food(food_type):
        if food_type.lower() == "cheeseburger":
            food = CheeseBurger()
        elif food_type.lower() == "pasta":
            food = Pasta()
        elif food_type.lower() == "taco":
            food = Taco()
        else:
            assert 0, f"Sorry, the restaurant does not make '{food_type}'"
        food.prepare()
        return food

def main():
    try:
        r = Restaurant()
        food = r.order_food("cheeseburger")
        if food:
            print(food)

        food = r.order_food("pasta")
        if food:
            print(food)

        food = r.order_food("taco")
        if food:
            print(food)

        r2 = Restaurant()
        print(r2)

        food = r.order_food("mac and cheese")  # doesn't exist, prints failure message
        if food:
            print(food)
            # Use this test to prove we have a single instance of Restaurant:

        r2 = Restaurant()
        print(r2)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
