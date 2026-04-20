from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

VECTOR_STORE_ID = "YOUR_VECTOR_STORE_ID"

class Query(BaseModel):
    message: str

@app.post("/search")
def search(query: Query):
    response = client.responses.create(
        model="gpt-4.1",
        input=query.message,
        tools=[
            {
                "type": "file_search",
                "vector_store_ids": [VECTOR_STORE_ID]
            },
            {
                "type": "web_search"
            }
        ],
        tool_choice="auto"
    )

    try:
        text = response.output[0].content[0].text
    except:
        text = str(response)

    return {"response": text}