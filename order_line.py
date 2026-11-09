from product import Product

class OrderLine:
    """Represents one product and the quantity of that product requested in an order."""
    
    def __init__(self, product: Product, quantity: int) -> None:
        self._product: Product = product
        self._quantity: int = quantity

    @property
    def product(self) -> Product:
        return self._product

    @property
    def quantity(self) -> int:
        return self._quantity

    def calculate_subtotal(self) -> float:
        """Calculates and returns the subtotal (product price * quantity)."""
        return self._product.price * self._quantity