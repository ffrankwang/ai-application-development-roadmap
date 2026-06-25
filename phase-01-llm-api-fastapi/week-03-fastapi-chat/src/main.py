import uuid
from fastapi import FastAPI
from llm_service import generate_reply, MODEL
from schemas import ChatRequest, ChatResponse

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    session_id = request.session_id or str(uuid.uuid4())
    reply = generate_reply(request.message, session_id)

    if reply is None:
        return ChatResponse(
            reply="服务暂时不可用，请稍后重试。",
            session_id=session_id,
            model=request.model or MODEL,
        )

    return ChatResponse(
        reply=reply,
        session_id=session_id,
        model=request.model or MODEL,
    )
