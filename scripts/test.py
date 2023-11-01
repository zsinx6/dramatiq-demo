import asyncio
import time
import urllib.parse

import httpx

NUMBER_OF_REQUESTS = 10000  # Total number of requests to send

BASE_ENDPOINT_URL = "http://localhost:8000/process/"


async def send_request(client, data):
    """Function to send a single POST request with query parameters asynchronously."""
    try:
        query_params = urllib.parse.urlencode({"data": data})
        full_url = f"{BASE_ENDPOINT_URL}?{query_params}"

        response = await client.post(full_url)
        return response.status_code
    except httpx.RequestError as e:
        return str(e)


async def main():
    async with httpx.AsyncClient() as client:
        sample_data = [f"test_data_{i}" for i in range(NUMBER_OF_REQUESTS)]
        tasks = [send_request(client, data) for data in sample_data]

        start_time = time.perf_counter()

        await asyncio.gather(*tasks)

        end_time = time.perf_counter()

        total_time = end_time - start_time
        print(f"Total time taken: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
