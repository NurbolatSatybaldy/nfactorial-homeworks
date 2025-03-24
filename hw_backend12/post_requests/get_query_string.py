import httpx

async def get_query_string():
    url = "https://httpbin.org/get"  # Using httpbin for testing
    params = {
        "query": "blue shoes"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

# Run the function
import asyncio
asyncio.run(get_query_string())
