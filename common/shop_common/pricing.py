TAX_RATE = 0.0825

def total_with_tax(subtotal, rate=TAX_RATE):
    return round(subtotal * (1 + rate), 2)