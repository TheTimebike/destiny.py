class DestinyException(Exception):
    pass

class HTTPException(DestinyException):
    pass

class NoGatewayException(DestinyException):
    def __init__(self):
        super(NoGatewayException, self).__init__("There Is No Open Gateway, Use client.run()")

class NotFound(DestinyException):
    def __init__(self):
        super(NotFound, self).__init__("The Requested Data Could Not Be Found")

class TokenException(DestinyException):
    def __init__(self):
        super(TokenException, self).__init__("No API Token Was Provided")