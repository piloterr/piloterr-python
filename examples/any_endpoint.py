"""Call any path with request() and handle API errors."""

from piloterr import JsonResponse, PiloterrAPIError, PiloterrClient

with PiloterrClient() as client:  # reads PILOTERR_API_KEY
    try:
        response = client.request("GET", "/v1/usage")
        if isinstance(response, JsonResponse):
            print(response.data)
    except PiloterrAPIError as error:
        print(f"HTTP {error.status}: {error}")
