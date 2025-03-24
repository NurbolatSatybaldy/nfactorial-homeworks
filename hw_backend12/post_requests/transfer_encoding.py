import httpx

async def post_chunked_data():
    url = "https://httpbin.org/post"  # Using httpbin for testing
    
    # Chunks of data to send
    chunks = [
        b"Hello, ",
        b"world!"
    ]
    
    # Headers specifying chunked transfer encoding
    headers = {
        "Transfer-Encoding": "chunked"
    }

    # Using httpx's AsyncClient to handle the request
    async with httpx.AsyncClient() as client:
        # Initiate the POST request with chunked transfer encoding
        async with client.stream("POST", url, headers=headers) as response:
            # Write the chunks of data
            for chunk in chunks:
                await response.arequest.write(chunk)
            
            # End the chunked transfer with a chunk of size 0
            await response.arequest.write(b"0\r\n\r\n")  # This signals the end of the chunks

            # Check the status code and response text
            print(f"Status code: {response.status_code}")
            print(f"Response text: {response.text}")

# To run the function
import asyncio
asyncio.run(post_chunked_data())
