class PositiveDefinite(object):
    """
    PositiveDefinite holds a value that is
    definitely a positive integer value.
    """

    def __init__(self, initval=1):
        self.value = initval

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if type(value) is int and value > 0:
            self.value = value
        else:
            raise ValueError("Value is definitely not positive.")
