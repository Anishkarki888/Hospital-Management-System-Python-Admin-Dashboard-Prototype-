class Person:
    """Person Class"""

    def __init__(self, first_name: str, surname: str):
        self._first_name = first_name
        self._surname = surname

    def full_name(self):
        return f"{self._first_name} {self._surname}"
    
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, new_first_name: str):
        self._first_name = new_first_name

    def get_surname(self):
        return self._surname
    
    def set_surname(self, surname: str):
        self._surname = surname
