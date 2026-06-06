def run_cart():
    print("--- 🛒 SMART SHOPPING CART ---")
    cart = {}

    while True:
        try:
            item = input("Enter item (or '2' to checkout): ").strip().title()
            if item == '2': 
                break
                
            if not item:
                print("Item cannot be empty!")
                continue

            # Check for duplicates
            if item in cart:
                print(f"⚠️ '{item}' is already in the cart.")
                confirm = input("Add another one? (y/n): ").strip().lower()
                if confirm != 'y': 
                    continue

            cart[item] = cart.get(item, 0) + 1
            print(f"✅ Added {item}!")
            
        except Exception as e:
            print(f"Error: {e}")

    # Final Summary
    print("\n--- 📦 FINAL CART ---")
    for item, qty in cart.items():
        print(f"• {item}: {qty}")

if __name__ == "__main__":
    run_cart()
