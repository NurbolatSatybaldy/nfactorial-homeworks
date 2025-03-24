import httpx
import json

async def post_json_data():
    url = "https://httpbin.org/post"  # Using httpbin for testing
    json_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    headers = {
        "Content-Type": "application/json",
        # Remove Content-Length header since httpx handles it automatically
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=json_data, headers=headers)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

# Run the function
import asyncio
asyncio.run(post_json_data())

