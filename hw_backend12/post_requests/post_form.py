import httpx

async def post_form_data():
    url = "https://httpbin.org/post"  # Using httpbin for testing
    data = {
        "username": "admin",
        "password": "secret"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data, headers=headers)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")

# Run the function
import asyncio
asyncio.run(post_form_data())
