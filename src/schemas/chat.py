from pydantic import BaseModel, Field


class UserInput(BaseModel):
    message: str = Field(
        description="The message to send to the chatbot",
        example=["Hello, how are you?"]
    )
    thread_id: str | None = Field(
        description="Thread id to persist and continue a multi-turn conversation.",
        default=None,
        examples=["847c6285-8fc9-4560-a83f-4e6285809254"]
    )
    user_id: str | None = Field(
        description="User id to persist and continue a conversation across multiple threads",
        default=None,
        examples=["847c6285-8fc9-4560-a83f-4e6285809254"]
    )

class StreamInput(UserInput):
    stream_tokens: bool = Field(
        description="Whether to stream tokens or not",
        default=False
    )
