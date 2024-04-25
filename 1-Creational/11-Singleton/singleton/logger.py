import random
class Logger:
    _instance = None
    _instanceName = ""
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instanceName = f"Name:{random.randint(0,10)}"
            cls._instance = super(Logger,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    def log_info(self, message):
        print(f"INFO -> {message}")
    def log_warning(self, message):
        print(f"WARNING -> {message}")
    def log_error(self, message):
        print(f"ERROR -> {message}")
    