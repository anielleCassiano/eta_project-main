import pytest

from src.models.ice_cream_stand import IceCreamStand

restaurant_name = 'Test'
cuisine_type = 'Unit'


class TestIceCreamStand:

    @pytest.fixture
    def ice_cream_stand(self):
        return IceCreamStand(restaurant_name, cuisine_type, ['Morango', 'Chocolate'])

    @pytest.fixture
    def ice_cream_stand_no_flavors(self):
        return IceCreamStand(restaurant_name, cuisine_type, [])

    def test_add_flavor_not_in_storage(self, ice_cream_stand_no_flavors, capsys):
        ice_cream_stand_no_flavors.add_flavor('Morango')
        out, _ = capsys.readouterr()

        assert out == "Estamos sem estoque atualmente!\n"

    def test_add_flavor_already_exists(self, ice_cream_stand, capsys):
        ice_cream_stand.add_flavor('Morango')
        out, _ = capsys.readouterr()

        assert out == "\nSabor já disponivel!\n"

    def test_add_flavor(self, ice_cream_stand, capsys):
        flavor = 'Ameixa'
        ice_cream_stand.add_flavor(flavor)
        out, _ = capsys.readouterr()

        assert out == f"{flavor} adicionado ao estoque!\n"

    def test_find_flavor_not_in_storage(self, ice_cream_stand_no_flavors, capsys):
        ice_cream_stand_no_flavors.find_flavor('Morango')
        out, _ = capsys.readouterr()

        assert out == "Estamos sem estoque atualmente!\n"

    def test_find_flavor(self, ice_cream_stand, capsys):
        flavor = 'Chocolate'
        ice_cream_stand.find_flavor(flavor)
        out, _ = capsys.readouterr()

        assert out == f"Temos no momento {flavor}!\n"

    def test_find_flavor_no_exists(self, ice_cream_stand, capsys):
        flavor = 'Ameixa'
        ice_cream_stand.find_flavor(flavor)
        out, _ = capsys.readouterr()

        assert out == f"Não temos no momento {flavor}!\n"

    def test_flavors_available_not_in_storage(self, ice_cream_stand_no_flavors, capsys):
        ice_cream_stand_no_flavors.flavors_available()
        out, _ = capsys.readouterr()

        assert out == "Estamos sem estoque atualmente!\n"

    def test_flavors_available_exists(self, ice_cream_stand, capsys):
        expeted = ("\n"
                   "No momento temos os seguintes sabores de sorvete disponíveis:\n"
                   "\t-Morango\n"
                   "\t-Chocolate\n")

        ice_cream_stand.flavors_available()
        out, _ = capsys.readouterr()

        assert out == expeted
