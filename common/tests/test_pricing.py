from shop_common.pricing import total_with_tax
from shop_common.validation import normalize

def test_total_with_tax():
    assert total_with_tax(100) == 108.25

def test_normalize():
    assert normalize("  Laptop ") == "laptop"