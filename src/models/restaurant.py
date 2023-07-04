class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.total_customers = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # BUG: A varaivel self.cuisine_type está como nome do restaurante
        # FIX: Alteramos a variavel de self.cuisine_type para self.restaurant_name
        print(f"Esse restaturante chama {self.restaurant_name} and serve {self.cuisine_type}.")
        print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            # BUG: A variavel self.open do restaurante está marcado como False
            # FIX: Alteramos a variavel self.open para True
            self.open = True

            # BUG: A variavel number_served está sendo reatribuiada para -2,
            # FIX: A variavel self.number_served foi removida, pois ja esta sendo inicializada com valor 0 no construtor
            print(f"{self.restaurant_name} agora está aberto!")
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            # BUG: A variavel self.number_served está sendo atribuida para o total de clientes,
            #  Sendo que a mesma variavel esta sendo sobrescrevida em outra função, increment_number_served, do codigo
            # FIX: Criamos uma variavel, self.total_customers, para guardar o total de clientes atendidos no dia,
            #  Evitando que a variavel self.number_served seja sobrescrevida na função: increment_number_served.
            self.total_customers = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            # BUG: A variavel self.number_served não esta sendo incrementada, esta sendo reatribuido um novo valor
            # FIX: Adicionamos a logica para que a variavel self.number_served seja incrementada com o valor recebido.
            self.number_served = self.number_served + more_customers
        else:
            print(f"{self.restaurant_name} está fechado!")
