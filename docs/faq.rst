Frequently Asked Questions
==========================

A list of frequently asked questions to help new users with their questions.

.. contents:: Questions
   :local:

Events
--------

What is an event?
~~~~~~~~~~~~~~~~~

An event is a piece of code that gets run at key points in the lifespan of a code. An example of an event
would be ``on_data_recieve``, which passes a request to the function whenever the client receives a piece of
data. 

Why does my code have to be inside an on_run event?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is important for your main block of code to be inside the on_run event as that is the section of code that
gets triggered whenever the application has prepared itself. Having the code executed this way also allows for
the client to manage running the code, which would have to be done manually without it.

How do I write my own events?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can tell the client that a function you have wrote is an event by decorating it with ``@client.event``.
This will register the function in the client and will execute the code whenever the event is triggered.

What events are there?
~~~~~~~~~~~~~~~~~~~~~~

You are able to see all of the different events in the `Event Reference <https://destinypy.readthedocs.io/en/latest/api.html#event-reference>`.

Coroutines
----------

What is a coroutine?
~~~~~~~~~~~~~~~~~~~~

A coroutine is a type of function that must be invoked with the prefix of 
``await`` Python 3.5+ or ``yield from`` Python 3.4-. When Python encounters a 
coroutine, it pauses its current task and works on what you've asked it to do.

When/where should I use await/yield from?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are only able to use await/yield from on coroutines. Coroutines are only able to be awaited inside
another async function. You can tell if a function is async if it is defined with ``async def`` or is
awaited itself.


General
-------

Im new to this API, where can I find some basic examples?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`You can find some basic examples of the API usage here. <https://github.com/TheTimebike/destiny.py/tree/master/examples>`_.

Where can I find the documentation for all of this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are able to find documentation for the functions in the `API Reference <https://destinypy.readthedocs.io/en/latest/api.html>`_.

You are able to find documentation for the events in the `Event Reference <https://destinypy.readthedocs.io/en/latest/api.html#event-reference>`_.

You are able to find documentation for the objects/classes in the `Object Reference <https://destinypy.readthedocs.io/en/latest/api.html#object-reference>`_.

Am I able to make my own API requests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By calling client.gatewaySession, you are able to make get and post requests of your own to the Destiny2 API.

Does this intentionally look like a copy of discord.py?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes.