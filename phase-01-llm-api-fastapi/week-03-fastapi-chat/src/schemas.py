from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="用户发送的消息内容",
    )
    session_id: str | None = Field(
        default=None,
        description="会话ID。不传则创建新会话，传入已有ID则续接触发多轮对话",
    )
    model: str | None = Field(default=None, description="使用的LLM模型名称")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="AI助手的回复内容")
    session_id: str = Field(..., description="当前会话ID")
    model: str | None = Field(default=None, description="实际使用的模型名称")
