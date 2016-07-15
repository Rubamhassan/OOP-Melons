"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    shipped = False
    base_price = 5
    
    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        if country_code:
            self.country_code = country_code

       
    def get_total(self):
        """Calculate price."""
        total = (1 + self.tax) * self.qty * self.base_price
        print total

    def mark_shipped(self):
        """Set shipped to true."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    tax = 0.08
    country_code = "USA"

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    country_code = "international"

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

