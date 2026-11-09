from inventory_manager import InventoryManager
from product import PhysicalProduct, DigitalProduct
from supplier import Supplier

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
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------\n")

        option = input("Enter option: ").strip()
        print()

        if option == "1":
            manager.display_all()

        elif option == "2":
            prod_type = input("Enter product type (physical/digital): ").strip().lower()
            p_id = input("Enter Product ID: ")
            name = input("Enter Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            
            sup_id = input("Enter Supplier ID: ")
            sup_name = input("Enter Supplier Name: ")
            sup_email = input("Enter Supplier Email: ")
            supplier = Supplier(sup_id, sup_name, sup_email)

            if prod_type == "physical":
                weight = float(input("Enter Weight (kg): "))
                product = PhysicalProduct(p_id, name, price, stock, supplier, weight)
            elif prod_type == "digital":
                download_size = float(input("Enter Download Size (MB): "))
                product = DigitalProduct(p_id, name, price, stock, supplier download_size)
            else:
                print("Invalid type. Defaulting to physical product.")
                product = PhysicalProduct(p_id, name, price, stock, supplier, 0.0)

            manager.add_product(product)

        elif option == "3":
            manager.update_stock()

        elif option == "4":
            product_id = input("Enter Product ID to search: ").strip()
    
            product = manager.find_product(product_id)
            
            if product:
                product.display_information()
                print()
            else:
                print("Product not found.\n")
            
        elif option == "5":
            manager.save()
        elif option == "6":
            print("Saving inventory before exit...")
            manager.save()
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else: 
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()