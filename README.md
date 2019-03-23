# destiny.py
destiny.py is an asynchronous API wrapper for the Destiny2 API. The module is designed to make requesting information from the Destiny2 API simpler and more accessable to users. The main structure for the module is event based, with certain events triggering at different times and executing code written by the user.

```
import destiny
client = destiny.Client()
@client.event
async def on_run():
	manifest = await client.get_manifest()
client.run()
```
