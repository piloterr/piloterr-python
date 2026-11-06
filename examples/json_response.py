"""Call the featured endpoint and print the JSON result."""

import json
import os

from piloterr import PiloterrClient

with PiloterrClient(os.environ["PILOTERR_API_KEY"]) as client:
    response = client.amazon_product(query="B09DFCB66S")
    print(json.dumps(response.data, indent=2))
