"""Start an async job and wait for its result."""

from piloterr import PiloterrClient

with PiloterrClient() as client:  # reads PILOTERR_API_KEY
    submitted = client.amazon_product(query="B09DFCB66S", is_async=True)
    job = client.wait_for_job(
        submitted.data["job_id"],
        on_progress=lambda j: print(j["status"], j.get("progress")),
    )
    print(job.data)
