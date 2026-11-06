# Examples

```sh
pip install piloterr
export PILOTERR_API_KEY="YOUR_API_KEY"
python examples/json_response.py
```

- `json_response.py` — call the featured endpoint and print the JSON result.
- `binary_response.py` — save a binary response to a file.
- `async_client.py` — use `AsyncPiloterrClient`.
- `any_endpoint.py` — call any path with `request()` and handle API errors.
- `wait_for_job.py` — start an async job and wait for its result.
