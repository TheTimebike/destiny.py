class EventHandler:
    def __init__(self, focus):
        self.focus = focus
        pass
    
    async def _trigger_event(self, event, *argv):
        function = getattr(self, event)
        self.focus._loop.create_task(function(argv))
    
    async def _trigger_on_run(self, params):
        if hasattr(self, "on_run"):
            await self.on_run()
            
    async def _trigger_on_data_recieve(self, params):
        if hasattr(self, "on_data_recieve"):
            await self.on_data_recieve(params[0])
            
    async def _trigger_on_get_request(self, params):
        if hasattr(self, "on_get_request"):
            print("triggered")
            await self.on_get_request(params[0])
            
    async def _trigger_on_post_request(self, params):
        if hasattr(self, "on_post_request"):
            await self.on_post_request(params[0])
