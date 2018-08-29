from pypattyrn.creational.factory import Factory, AbstractFactory
from Patterns.factory import convertionFactoryCurrency, convertionFactoryLongitude


class convertionFactory(AbstractFactory):

    def __init__(self):
        super().__init__()
        self._register('longitude_factory', convertionFactoryLongitude())  # Register an convertionFactoryLongitude with a keyword.
        self._register('currency_factory', convertionFactoryCurrency())  # convertionFactoryCurrency with a keyword.

    def create(self, convertion_type, number):  # Implement the Abstract create method.
        if convertion_type == 1 or convertion_type == 2:
            return self._factories['longitude_factory'].create(convertion_type, number)
        elif convertion_type == 3 or convertion_type == 4:
            return self._factories['currency_factory'].create(convertion_type, number)
        else:
            return None