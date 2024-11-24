from store.models import Product


class Cart:
    def __init__(self, request):
        # get session key from logged in users
        self.session = request.session

        cart = self.session.get("session_key")

        # create session for new users
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        # make sure cart available in all [ages of the website
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass

        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart

        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourCart = self.cart

        # update cart => product_id value into new product_qty
        ourCart[product_id] = product_qty

        self.session.modified = True

        return self.cart
