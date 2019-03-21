class EventHandler:
    def __init__(self, focus):
        pass
        
    def _trigger_on_run(self):
        if hasattr(self, "on_run"):
            self.on_run()
            
    def _trigger_on_recieve(self):
        if hasattr(self, "on_recieve"):
            self.on_recieve()
            
    def _register_authorisation(self):
    
