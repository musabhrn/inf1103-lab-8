from product import Product

class OrderLine:
    """Represents one product and the quantity of that product requested in an order."""
    
    def __init__(self, product: Product, quantity: int) -> None:
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        """Calculates and returns the subtotal (product price * quantity)."""
        return self.product.price * self.quantity