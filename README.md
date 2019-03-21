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

## Dependencies
Python 3.5+
```aiohttp``` library

## Installation
```
pip install https://github.com/TheTimebike/destiny.py.git
```
To check if destiny.py has been installed succesfully, open a Python code terminal and type "import destiny".

## Documentation

### client
> class destiny.Client(loop=None)

This class is used to define the client that destiny.py will use to make all of the requests. All of the API requests are functions of this class.

#### Parameters

- ```Loop``` - The loop which will be used to hold asynchronous functions. If not specifed, one will be created by the client.

> run()

This function is an attribute of ```client``` that tells destiny.py to run the code it has been given.

>
