class Singleton:
    __isinstance = None

    def __new__(cls):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)
        return cls.__isinstance

    def __del__(self):
        Singleton.__isinstance = None
