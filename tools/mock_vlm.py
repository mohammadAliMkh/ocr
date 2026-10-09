import json

from fastapi import FastAPI

app = FastAPI()


FAKE_RESULT = {
    "summary": "یک اسکرین‌شات از متن آموزشی فارسی و انگلیسی",
    "ocr_text": "یه متن فارسی و انگلیسی اسکرین‌شات بگیر",
    "document_type": "screenshot",
    "languages": ["fa", "en"],
    "entities": [],
    "notes": "mock response",
}


@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "mock-vlm",
                "object": "model",
            }
        ],
    }


@app.post("/v1/chat/completions")
async def chat_completions(payload: dict):
    return {
        "id": "mock-1",
        "object": "chat.completion",
        "model": payload.get("model", "mock-vlm"),
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": json.dumps(
                        FAKE_RESULT,
                        ensure_ascii=False,
                    ),
                },
                "finish_reason": "stop",
            }
        ],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9000)
