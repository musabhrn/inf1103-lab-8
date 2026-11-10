from inventory_manager import InventoryManager
from product import PhysicalProduct, DigitalProduct
from supplier import Supplier
from order import Order

def display_menu():
    print("=" * 35)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 35)
    print()


def main():
    display_menu()
    manager = InventoryManager()

    while True:
        print("--------MENU--------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Create Order")
        print("7. Save Inventory")
        print("8. Exit")
        print("--------------------\n")

        option = input("Enter option: ").strip()
        print()

        if option == "1":
            manager.display_all()

        elif option == "2":
            prod_type = input("Enter product type (physical/digital): ").strip().lower()
            p_id = input("Enter Product ID: ").strip()
            name = input("Enter Name: ").strip()
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            
            sup_id = input("Enter Supplier ID: ").strip()
            sup_name = input("Enter Supplier Name: ").strip()
            sup_email = input("Enter Supplier Email: ").strip()
            supplier = Supplier(sup_id, sup_name, sup_email)

            if prod_type == "physical":
                weight = float(input("Enter Weight (kg): "))
                product = PhysicalProduct(p_id, name, price, stock, supplier, weight)
            elif prod_type == "digital":
                download_size = float(input("Enter Download Size (MB): "))
                product = DigitalProduct(p_id, name, price, stock, supplier, download_size)
            else:
                print("Invalid type. Defaulting to physical product.")
                product = PhysicalProduct(p_id, name, price, stock, supplier, 0.0)

            manager.add_product(product)
            print(f"Product '{product.name}' added successfully to inventory.\n")

        elif option == "3":
            p_id = input("Enter Product ID to update: ").strip()
            try:
                quantity = int(input("Enter new stock quantity: "))
                if manager.update_stock(p_id, quantity):
                    print("Stock updated successfully!\n")
                else:
                    print(f"Product ID '{p_id}' not found.\n")
            except ValueError:
                print("Invalid quantity. Please enter a valid integer.\n")

        elif option == "4":
            p_id = input("Enter Product ID to search: ").strip()
            product = manager.find_product(p_id)
            if product:
                print("Product Found:")
                product.display_information()
                print("\n")
            else:
                print(f"Product ID '{p_id}' not found.\n")

        elif option == "5":
            p_id = input("Enter Product ID to remove: ").strip()

            success = manager.remove_product(p_id)
            if success:
                print(f"Product ID '{p_id}' removed from inventory successfully.\n")
            else:
                print(f"Product ID '{p_id}' not found in inventory.\n")
                
        elif option == "6":
            order_id = input("Enter Order ID: ").strip()
            order = Order(order_id)
            
            p_id = input("Enter Product ID to add to order: ").strip()
            product = manager.find_product(p_id)
            
            if not product:
                print(f"Product ID '{p_id}' not found.\n")
            else:
                try:
                    qty = int(input(f"Enter quantity for {product.name} (Stock available: {product.stock}): "))
                    if qty > product.stock:
                        print("Error: Requested quantity exceeds current stock!\n")
                    else:
                        # Add line, reduce stock, and print receipt all in one go
                        order.add_order_line(product, qty)
                        product.stock -= qty
                        
                        print("\n" + "=" * 30)
                        print(f"ORDER RECEIPT: {order.order_id}")
                        print("=" * 30)
                        for line in order.order_lines:
                            print(f"- {line.product.name} x {line.quantity} = ${line.calculate_subtotal():.2f}")
                        print("-" * 30)
                        print(f"Grand Total: ${order.calculate_total():.2f}")
                        print("=" * 30 + "\n")
                        
                except ValueError:
                    print("Invalid quantity. Please enter a valid integer.\n")
            
        elif option == "7":
            manager.save()
            print("Inventory saved to file successfully.\n")

        elif option == "8":
            print("Saving inventory before exit...")
            manager.save()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else: 
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()