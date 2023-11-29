def iva_21(n):
    return n * 0.21


def iva_4(n):
    return n * 0.04


def discount_10(n):
    return n * 0.1


def total(basket):
    total_b = {"price": 0, "iva": 0, "discount": 0}
    if basket[0]["discount"] is None:
        total_b["price"] = basket[0]["iva"](basket[0]["price"]) + basket[0]["price"]
        total_b["iva"] = basket[0]["iva"](basket[0]["price"])
    else:
        total_b["price"] = basket[0]["discount"](basket[0]["price"]) + basket[0]["price"]
        total_b["discount"] = basket[0]["discount"](basket[0]["price"])
        total_b["iva"] = basket[0]["iva"](basket[0]["price"])
    return total_b











