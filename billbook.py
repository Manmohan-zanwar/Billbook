import tkinter as tk
from tkinter import messagebox, ttk

class ShopBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Billing System")
        self.root.geometry("500x600")
        self.root.configure(bg='#AFE1AF')  # Parrot green background

        # Define shop items
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
        self.vape_refill_count = 0
        self.joints_count = 0

        # Employee and Customer details
        self.create_input_fields()
        self.create_item_selection()
        self.create_cart_and_bill_buttons()

    def create_input_fields(self):
        tk.Label(self.root, text="Employee Name", bg='#AFE1AF', fg='white').pack(pady=5)
        self.employee_name_entry = tk.Entry(self.root)
        self.employee_name_entry.pack(pady=5)

        tk.Label(self.root, text="Customer Name", bg='#AFE1AF', fg='white').pack(pady=5)
        self.customer_name_entry = tk.Entry(self.root)
        self.customer_name_entry.pack(pady=5)

        tk.Label(self.root, text="Customer ID (CID)", bg='#AFE1AF', fg='white').pack(pady=5)
        self.customer_id_entry = tk.Entry(self.root)
        self.customer_id_entry.pack(pady=5)

    def create_item_selection(self):
        tk.Label(self.root, text="Select Item", bg='#AFE1AF', fg='white').pack(pady=5)

        # Use ttk Combobox for a better dropdown experience
        self.item_var = tk.StringVar()
        self.item_dropdown = ttk.Combobox(self.root, textvariable=self.item_var, values=list(self.items.keys()), state="readonly")
        self.item_dropdown.current(0)  # Set default selection
        self.item_dropdown.pack(pady=5)

        tk.Label(self.root, text="Quantity", bg='#AFE1AF', fg='white').pack(pady=5)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack(pady=5)

    def create_cart_and_bill_buttons(self):
        add_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart, bg="white", fg="black")
        add_button.pack(pady=10)

        bill_button = tk.Button(self.root, text="Generate Bill", command=self.generate_bill, bg="white", fg="black")
        bill_button.pack(pady=10)

        self.bill_text = tk.Text(self.root, height=15, width=50, bg="white")
        self.bill_text.pack(pady=10)

    def add_to_cart(self):
        item_name = self.item_var.get()
        quantity = self.quantity_entry.get()

        if not quantity.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid quantity.")
            return

        quantity = int(quantity)
        price = self.items[item_name]
        total_price = price * quantity
        self.cart.append({
            'name': item_name,
            'price': price,
            'quantity': quantity,
            'total_price': total_price
        })

        # Track vape refill and joints count
        if item_name == "Refill" or item_name == "THC Refill":
            self.vape_refill_count += quantity
        elif item_name == "Joints":
            self.joints_count += quantity

        self.quantity_entry.delete(0, tk.END)
        self.bill_text.insert(tk.END, f"Added {quantity} x {item_name} @ ${price} each\n")

    def calculate_total(self):
        return sum(item['total_price'] for item in self.cart)

    def generate_bill(self):
        employee_name = self.employee_name_entry.get()
        customer_name = self.customer_name_entry.get()
        customer_id = self.customer_id_entry.get()

        if not (employee_name and customer_name and customer_id):
            messagebox.showerror("Input Error", "Please fill all details.")
            return

        total = self.calculate_total()
        self.bill_text.delete(1.0, tk.END)
        self.bill_text.insert(tk.END, "--- Bill Summary ---\n")
        self.bill_text.insert(tk.END, f"Employee Name: {employee_name}\n")
        self.bill_text.insert(tk.END, f"Customer Name: {customer_name}\n")
        self.bill_text.insert(tk.END, f"Customer ID (CID): {customer_id}\n\n")

        for item in self.cart:
            self.bill_text.insert(tk.END, f"{item['name']} - {item['quantity']} pcs @ ${item['price']:.2f} each: ${item['total_price']:.2f}\n")
        
        self.bill_text.insert(tk.END, f"\nVape Refills: {self.vape_refill_count}")
        self.bill_text.insert(tk.END, f"\nNo of Joints: {self.joints_count}\n")
        self.bill_text.insert(tk.END, f"\nTotal: ${total:.2f}\n")
        self.bill_text.insert(tk.END, "\nThank you for shopping with us!")

# Initialize the application
root = tk.Tk()
app = ShopBillingSystem(root)
root.mainloop()
