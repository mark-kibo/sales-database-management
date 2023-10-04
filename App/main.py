from models.models import session
from models.models import Branch, Supplier, Customer

# Create the SQLAlchemy engine and session

def main():
    """Sales Management CLI"""
    while True:
        print("\nAvailable Commands:")
        print("1. Create Branch")
        print("2. Get Branch by ID")
        print("3. Create Supplier")
        print("4. Get Supplier by ID")
        print("5. Create Customer")
        print("6. Get Customer by ID")
        print("7. See Customer's Branches")
        print("8. Add Customer to a Branch")
        print("9. Add Supplier to a Branch")
        print("10. See Suppliers in a Branch")
        print("11. See Branches of a Supplier")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Branch Name: ")
            location = input("Enter Branch Location: ")
            manager = input("Enter Branch Manager: ")
            branch = Branch.create(name, location, manager)
            print(f"Branch with ID {branch.id} created successfully.")
        elif choice == "2":
            branch_id = int(input("Enter Branch ID: "))
            branch = Branch.get_by_id(branch_id)
            if branch:
                print(f"Branch ID: {branch.id}, Name: {branch.name}, Location: {branch.location}, Manager: {branch.manager}")
            else:
                print("Branch not found")
        elif choice == "3":
            name = input("Enter Supplier Name: ")
            address = input("Enter Supplier Address: ")
            contact_person = input("Enter Contact Person: ")
            supplier = Supplier.create(name, address, contact_person)
            print(f"Supplier with ID {supplier.id} created successfully.")
        elif choice == "4":
            supplier_id = int(input("Enter Supplier ID: "))
            supplier = Supplier.get_by_id(supplier_id)
            if supplier:
                print(f"Supplier ID: {supplier.id}, Name: {supplier.name}, Address: {supplier.address}, Contact Person: {supplier.contact_person}")
            else:
                print("Supplier not found")
        elif choice == "5":
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            phone_number = input("Enter Phone Number: ")
            branch_id = int(input("Enter Branch ID for the customer: "))
            customer = Customer.create(name, email, phone_number, branch_id)
            print(f"Customer with ID {customer.id} created successfully.")
        elif choice == "6":
            customer_id = int(input("Enter Customer ID: "))
            customer = Customer.get_by_id(customer_id)
            if customer:
                branch = customer.get_branch_info()
                print(f"Customer ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone Number: {customer.phone_number}")
                print(f"Branch Info - ID: {branch.id}, Name: {branch.name}, Location: {branch.location}, Manager: {branch.manager}")
            else:
                print("Customer not found")
        elif choice == "7":
            customer_id = int(input("Enter Customer ID: "))
            customer = Customer.get_by_id(customer_id)
            if customer:
                branches = customer.get_customer_branches()
                if branches:
                    print(f"Branches for Customer ID {customer.id}:")
                    for branch in branches:
                        print(f"Branch ID: {branch.id}, Name: {branch.name}, Location: {branch.location}, Manager: {branch.manager}")
                else:
                    print("Customer is not associated with any branches.")
            else:
                print("Customer not found")
        elif choice == "8":
            customer_id = int(input("Enter Customer ID: "))
            branch_id = int(input("Enter Branch ID to add the customer: "))
            customer = Customer.get_by_id(customer_id)
            branch = Branch.get_by_id(branch_id)
            if customer and branch:
                branch.add_customer(customer)
                print(f"Customer ID {customer.id} added to Branch ID {branch.id} successfully.")
            else:
                print("Customer or Branch not found.")
        elif choice == "9":
            supplier_id = int(input("Enter Supplier ID: "))
            branch_id = int(input("Enter Branch ID to add the supplier: "))
            supplier = Supplier.get_by_id(supplier_id)
            branch = Branch.get_by_id(branch_id)
            if supplier and branch:
                branch.add_supplier(supplier)
                print(f"Supplier ID {supplier.id} added to Branch ID {branch.id} successfully.")
            else:
                print("Supplier or Branch not found.")
        elif choice == "10":
            branch_id = int(input("Enter Branch ID: "))
            branch = Branch.get_by_id(branch_id)
            if branch:
                suppliers = branch.get_suppliers()
                if suppliers:
                    print(f"Suppliers in Branch ID {branch.id}:")
                    for supplier in suppliers:
                        print(f"Supplier ID: {supplier.id}, Name: {supplier.name}, Address: {supplier.address}, Contact Person: {supplier.contact_person}")
                else:
                    print("No suppliers in this branch.")
            else:
                print("Branch not found")
        elif choice == "11":
            supplier_id = int(input("Enter Supplier ID: "))
            supplier = Supplier.get_by_id(supplier_id)
            if supplier:
                branches = supplier.get_branches()
                if branches:
                    print(f"Branches of Supplier ID {supplier.id}:")
                    for branch in branches:
                        print(f"Branch ID: {branch.id}, Name: {branch.name}, Location: {branch.location}, Manager: {branch.manager}")
                else:
                    print("Supplier is not associated with any branches.")
            else:
                print("Supplier not found")
        elif choice == "12":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
