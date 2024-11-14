class ShopBillingSystem:
    def __init__(self):
        # Initializing shop items with prices
        self.items = {
            "GeekBar": 800,
            "Flavoured GeekBar": 1000,
            "Refill": 400,
            "THC Refill": 500,
            "Joints": 150,
            "Weed Gummies": 80,
            "Brownies": 100,
            "Bong": 900,
            "Penjamin": 300,
            "Almond Joy": 20,
            "Rice Krispies": 30
        }
        self.cart = []
        self.employee_name = ""
        self.customer_name = ""
        self.customer_id = ""
        self.vape_refill_count = 0
        self.joints_count = 0

    def set_employee_name(self, name):
        self.employee_name = name

    def set_customer_details(self, name, cid):
        self.customer_name = name
        self.customer_id = cid

    def add_to_cart(self, item_name, quantity):
        if item_name in self.items:
            price = self.items[item_name]
            total_price = price * quantity
            self.cart.append({
                'name': item_name,
                'price': price,
                'quantity': quantity,
                'total_price': total_price
            })
            print(f"Added {quantity} x {item_name} @ ${price} each")
            
            # Track vape refill and joints count separately
            if item_name == "Refill" or item_name == "THC Refill":
                self.vape_refill_count += quantity
            elif item_name == "Joints":
                self.joints_count += quantity
        else:
            print(f"Item '{item_name}' not found.")

    def calculate_total(self):
        return sum(item['total_price'] for item in self.cart)

    def generate_bill(self, discount_percentage=0):
        print("\n--- Bill Summary ---")
        print(f"Employee Name: {self.employee_name}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Customer ID (CID): {self.customer_id}\n")
        
        for item in self.cart:
            print(f"{item['name']} - {item['quantity']} pcs @ ${item['price']:.2f} each: ${item['total_price']:.2f}")
        
        print(f"\nVape Refills: {self.vape_refill_count}")
        print(f"No of Joints: {self.joints_count}")

        total = self.calculate_total()
        print(f"\nSubtotal: ${total:.2f}")
        
        if discount_percentage > 0:
            discount_amount = total * (discount_percentage / 100)
            discounted_total = total - discount_amount
            print(f"Discount ({discount_percentage}%): -${discount_amount:.2f}")
            print(f"Total after discount: ${discounted_total:.2f}")
        else:
            print(f"Total: ${total:.2f}")
        
        print("\nThank you for shopping with us!")

# Example Usage
shop = ShopBillingSystem()
shop.set_employee_name("Alex")
shop.set_customer_details("John Doe", "12345")
shop.add_to_cart("GeekBar", 1)
shop.add_to_cart("Refill", 2)
shop.add_to_cart("Joints", 3)

# Generate bill with a 10% discount
shop.generate_bill(discount_percentage=10)
