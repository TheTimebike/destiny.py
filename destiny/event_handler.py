class EventHandler:
    def __init__(self, focus):
        pass
        
    def _trigger_on_run(self):
        if hasattr(self, "on_run"):
            self.on_run()
            
    def _trigger_on_recieve(self, recieved):
        if hasattr(self, "on_recieve"):
            self.on_recieve(recieved)
            
    def _trigger_on_get_request(self, request):
        if hasattr(self, "on_get_request"):
            self.on_get_request(request)
            
    def _trigger_on_post_request(self):
        if hasattr(self, "on_post_request"):
            self.on_post_request(request)
