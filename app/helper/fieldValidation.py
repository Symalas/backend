import json

class Validation():

    def __init__(self):
        self.errorMessage = []
    
    def validate(self, field, message):
        if field is None or len(field) <= 1:
            self.errorMessage.append(message)

    def error(self):
        return self.errorMessage