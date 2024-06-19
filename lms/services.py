import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name):
    """Создает продукт в страйпе"""
    product = stripe.Product.create(name=name)
    return product


def create_stripe_price(product, amount):
    """Создает цену в страйпе"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        recurring={"interval": "month"},
        product=product,
    )
    return price


def create_stripe_session(price):
    """Создает сессию для оплаты в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="subscription",
    )
    return session
