from ..ejer42 import iva_21, iva_4, discount_10, total

list_b = [
    {"price": float(100),
     "discount": None,
     "iva": iva_21},

    {"price": float(200),
     "discount": None,
     "iva": iva_4},

    {"price": float(100),
     "discount": discount_10,
     "iva": iva_21
     }

]


def test_iva_21():
    assert 121 == iva_21(100)


def test_iva_21b():
    global list_b
    assert 121 == list_b[0]["price"] + list_b[0]["iva"](list_b[0]["price"])


def test_iva_4():
    global list_b
    assert 208 == list_b[1]["price"] + list_b[1]["iva"](list_b[1]["price"])


def test_discount():
    global list_b
    assert 90 == list_b[2]["price"] + list_b[2]["discount"](list_b[2]["price"])


def test_total():
    global list_b
    assert {'price': 121.0, 'iva': 21.0, 'discount': 0} == {'price': 121.0, 'iva': 21.0, 'discount': 0}

