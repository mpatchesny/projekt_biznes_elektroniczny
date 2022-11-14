# W technologii Sellenium, który przeprowadzi proces testowania procesu zakupowego:
# - Przejdzie przez proces rejestracji nowego konta,
# - Doda do koszyka 10 produktów (w różnych ilościach) z dwóch różnych kategorii
# - Usunie z koszyka 1 produkt,
# - Wybierze płatność przy odbiorze,
# - Wybierze jednego z dwóch przewoźników,
# - Zatwierdzi zamówienie,
# - Sprawdzi status zamówienia.

def register_new_account():
    pass

def add_product_to_basket(amount, category):
    pass

def remove_product_from_basket(product_name):
    pass

def do_checkout():
    pass

def select_cash_on_delivery():
    pass

def approve_order():
    pass

def check_order_status():
    pass

def run_all_tests():
    register_new_account()
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    add_product_to_basket(amount, category)
    remove_product_from_basket(product_name)
    do_checkout()
    select_cash_on_delivery()
    approve_order()
    check_order_status()

run_all_tests()