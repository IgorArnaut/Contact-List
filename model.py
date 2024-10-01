class Contact:
    def __init__(self, firstname, lastname, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}: {self.phone}, {self.email}"