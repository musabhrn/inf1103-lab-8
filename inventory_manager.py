import json
import os
from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier

class InventoryManager:
    def __init__(self, filename: str ="inventory.json"):
        self._filename: str = filename
        self._products: list[Product] = []
        self.load()

    def add_product(self, product: Product) -> None:
        self._products.append(product)

    def remove_product(self, product_id: str) -> bool:
            product = self.find_product(product_id)
            if product:
                self._products.remove(product)
                return True
            return False

    def find_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def update_stock(self, product_id: str, new_stock: int) -> bool:
        product = self.find_product(product_id)
        if product:
            product.update_stock(new_stock)
            return True
        return False

    def save(self) -> None:
        data = [p.to_dict() for p in self._products]
        with open(self._filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self) -> None:
        if os.path.exists(self._filename):
            try:
                with open(self._filename, "r") as f:
                    data = json.load(f)
                    self._products = []
                    for item in data:
                        sup_data = item.get("supplier")
                        supplier = None
                        if sup_data:
                            supplier = Supplier(
                                sup_data.get("supplier_id"),
                                sup_data.get("name"),
                                sup_data.get("contact_email")
                            )

                        if item.get("type") == "physical":
                            prod = PhysicalProduct(
                                item["id"], item["name"], item["price"], item["stock"], supplier, item["weight"]
                            )
                        elif item.get("type") == "digital":
                            prod = DigitalProduct(
                                item["id"], item["name"], item["price"], item["stock"], supplier, item["download_size"]
                            )
                        else:
                            prod = PhysicalProduct(
                                item["id"], item["name"], item["price"], item["stock"], supplier, 0.0
                            )
                        self._products.append(prod)
            except Exception as e:
                print(f"Error loading inventory: {e}")
                self._products = []
        else:
            self._products = []

    def display_all(self) -> None:
        if not self._products:
            print("No products in inventory.")
        else:
            for product in self._products:
                product.display_information()
            print()