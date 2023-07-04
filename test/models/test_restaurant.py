import random

import pytest

from src.models.restaurant import Restaurant

restaurant_name = 'Test'
cuisine_type = 'Unit'


class TestRestaurant:

    @pytest.fixture
    def restaurant(self):
        return Restaurant(restaurant_name, cuisine_type)

    def test_describe_restaurant(self, restaurant, capsys):
        restaurant.describe_restaurant()
        out, _ = capsys.readouterr()

        expected = (
            f'Esse restaturante chama {restaurant_name} and serve {cuisine_type}.\n'
            'Esse restaturante está servindo 0 consumidores desde que está aberto.\n'
        )

        assert out == expected

    def test_open_restaurant(self, restaurant, capsys):
        restaurant.open_restaurant()
        out, _ = capsys.readouterr()

        assert out == f'{restaurant_name} agora está aberto!\n'

    def test_open_restaurant_check_open_status(self, restaurant):
        restaurant.open_restaurant()

        assert restaurant.open is True

    def test_open_restaurant_number_served(self, restaurant):
        restaurant.open_restaurant()

        assert restaurant.number_served == 0

    def test_open_restaurant_already_opened(self, restaurant, capsys):
        restaurant.open = True
        restaurant.open_restaurant()
        out, _ = capsys.readouterr()

        assert out == f"{restaurant_name} já está aberto!\n"

    def test_close_restaurant(self,  restaurant, capsys):
        restaurant.open = True
        restaurant.close_restaurant()
        out, _ = capsys.readouterr()

        assert out == f"{restaurant_name} agora está fechado!\n"

    def test_close_restaurant_check_open_status(self,  restaurant):
        restaurant.open = True
        restaurant.close_restaurant()

        assert restaurant.open is False

    def test_close_restaurant_number_served(self,  restaurant):
        restaurant.open = True
        restaurant.close_restaurant()

        assert restaurant.number_served == 0

    def test_close_restaurant_already_closed(self,  restaurant, capsys):
        restaurant.close_restaurant()
        out, _ = capsys.readouterr()

        assert out == f"{restaurant_name} já está fechado!\n"

    def test_set_number_served(self, restaurant):
        random_total_customers = random.randint(0, 100)
        restaurant.open = True
        restaurant.set_number_served(random_total_customers)

        assert restaurant.total_customers == random_total_customers

    def test_set_total_customers_if_closed(self, restaurant, capsys):
        random_total_customers = random.randint(0, 100)
        restaurant.set_number_served(random_total_customers)
        out, _ = capsys.readouterr()

        assert out == f"{restaurant_name} está fechado!\n"

    def test_increment_number_served(self, restaurant):
        restaurant.open = True
        restaurant.increment_number_served(1)
        restaurant.increment_number_served(1)

        assert restaurant.number_served == 2

    def test_increment_number_served_closed(self, restaurant, capsys):
        restaurant.increment_number_served(1)
        out, _ = capsys.readouterr()

        assert out == f"{restaurant_name} está fechado!\n"
