class supplier:
    def __init__(self, supplier_id : str, name : str, contact_email : str) -> None:
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self) -> None:
        print(f"ID: {self.supplier_id} | Name: {self.name} | Email: {self.contact_email}")