class Cart:
    def __init__(self, request):
        #get session key from logged in users 
        self.session = request.session

        cart = self.session.get("session_key")

        # create session for new users
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        
        # make sure cart available in all [ages of the website
        self.cart = cart

