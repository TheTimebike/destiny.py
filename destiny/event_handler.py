class EventHandler:
    def __init__(self, focus):
        pass
    
    def _trigger_event(self, event, **args):
        self.focus._loop._run_until_complete( getattr(self, event)(args) )
    
    async def _trigger_on_run(self):
        if hasattr(self, "on_run"):
            await self.on_run()
            
    async def _trigger_on_recieve(self, params):
        if hasattr(self, "on_recieve"):
            await self.on_recieve(params[0])
            
    async def _trigger_on_get_request(self, params):
        if hasattr(self, "on_get_request"):
            await self.on_get_request(params[0])
            
    async def _trigger_on_post_request(self, params):
        if hasattr(self, "on_post_request"):
            await self.on_post_request(params[0])
