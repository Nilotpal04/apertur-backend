from pydantic import BaseModel

class FrameResponse(BaseModel):
    framed: bool
    frames_count: int
    