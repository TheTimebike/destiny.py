class DestinyException(Exception):
    pass

class HTTPException(DestinyException):
    pass

class NoGatewayException(DestinyException):
    """An exception that is raised when a client function is used when there is no open gateway.
    """
    def __init__(self):
        super(NoGatewayException, self).__init__("There Is No Open Gateway, Use client.run()")

class NotFound(DestinyException):
    """An exception that is raised when a request returns no information.
    """
    def __init__(self):
        super(NotFound, self).__init__("The Requested Data Could Not Be Found")

class TokenException(DestinyException):
    """An exception that is raised when an API token is not provided to the client.
    """
    def __init__(self):
        super(TokenException, self).__init__("No API Token Was Provided")

class LanguageNotFoundException(DestinyException):
    """An exception that is raised when a language is provided to the manifest that is not valid
    """
    def __init__(self):
        super(LanguageNotFoundExceptiom, self).__init__("Language Provided Was Not Found")