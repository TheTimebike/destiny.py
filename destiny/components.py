class Components:
    """Represents the data given back by API requests.
    Attributes will be added to this class depending on what components are requested to it.

    components
        This is a list of components that the object currently has stored.
    
    """    
    def __init__(self):
        self.components = []
        pass

    def _add_attr(self, name, component):
        setattr(self, name, component)
        self.components.append(name)
