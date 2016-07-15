"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    shipped = False
    base_price = 5
    
    def __init__(self, species, qty, country_code, order_type, tax):
        self.species = species
        self.qty = qty
        self.country_code = country_code
       
    def get_total(self, qty, base_price):
        """Calculate price."""
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08
    country_code = "USA"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, country_code, order_type, tax)
        self.order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        self.country_code = country_code
        self.order_type = "international"


    def get_country_code(self):
        """Return the country code."""
        return self.country_code


InternationalMelonOrder(AbstractMelonOrder)
DomesticMelonOrder(AbstractMelonOrder)