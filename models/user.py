class User():
    """User model, defines a user and attrs"""

    def __init__(self, *args, **kwargs):
        """initializes a user object"""
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self._password = kwargs.get('_password')
        self.monthly_income = kwargs.get('monthly_income')
