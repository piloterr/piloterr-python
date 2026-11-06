"""Use the asyncio client."""

import asyncio

from piloterr import AsyncPiloterrClient


async def main() -> None:
    async with AsyncPiloterrClient() as client:  # reads PILOTERR_API_KEY
        response = await client.amazon_product(query="B09DFCB66S")
        print(response.data)


asyncio.run(main())
