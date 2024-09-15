from datetime import datetime


class Expenses():
    """Defines expenditure and attrs"""

    def __init__(self, *args, **kwargs):
        """Instantiates an expense"""
        self.name = kwargs.get('name')
        self.category = kwargs.get('category')
        self.amount = kwargs.get('amount')
        self.created = kwargs.get('created')
