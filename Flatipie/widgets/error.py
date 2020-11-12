
class FlatipieError(Exception):
    def __init__(self, message: str=None):
        if message is None:
            FlatipieError("An error occured")

class UnknownStyleError(FlatipieError):
    def __init__(self, message: str=None):
        if message is None:
            message = "Unknown style please read the docs for help"
            super().__init__(message)
        

class WidgetsNotFound(FlatipieError):
  def __init__(self, message):
    super().__init__("Unknown widget")
   
   
