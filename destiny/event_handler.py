class EventHandler:
    def __init__(self, focus):
        pass
    
    def _trigger_event(self, event):
        self.focus._loop._run_until_complete( getattr(self, event)() )
    
    async def _trigger_on_run(self):
        if hasattr(self, "on_run"):
            await self.on_run()
            
    async def _trigger_on_recieve(self, recieved):
        if hasattr(self, "on_recieve"):
            await self.on_recieve(recieved)
            
    async def _trigger_on_get_request(self, request):
        if hasattr(self, "on_get_request"):
            await self.on_get_request(request)
            
    async def _trigger_on_post_request(self):
        if hasattr(self, "on_post_request"):
            await self.on_post_request(request)
