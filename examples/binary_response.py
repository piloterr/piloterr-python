"""Save a binary response to a file."""

import os

from piloterr import BinaryResponse, PiloterrClient

with PiloterrClient(os.environ["PILOTERR_API_KEY"]) as client:
    response = client.website_screenshot(url="https://example.com")
    if isinstance(response, BinaryResponse):
        with open("screenshot.png", "wb") as file:
            file.write(response.bytes)
        print(f"Saved screenshot.png ({response.content_type}, {len(response.bytes)} bytes)")
    else:
        print(response.data)
