class Linear:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, x, *args, **kwargs):
        return self.a * x + self.b
