Mala
====
Get metadata from DHT network.
A BEP-9 implementation on Python 3.5+

Usage
-----
.. code-block:: python

    import asyncio
    from mala import get_metadata

    loop = asyncio.get_event_loop()
    metainfo = loop.run_until_complete(get_metadata(
        'infohash', 'ip', 'port', loop=self.loop
    )


Or, use with `Maga <https://github.com/whtsky/maga>`_

.. code-block:: python

    from maga import Maga
    from mala import get_metadata


    class Crawler(Maga):
        async def handle_get_peers(self, infohash, addr):
            pass

        async def handle_announce_peer(self, infohash, addr, peer_addr):
            metainfo = await get_metadata(
                infohash, peer_addr[0], peer_addr[1], loop=self.loop
            )

    crawler = Crawler()
    crawler.run(port=0)
