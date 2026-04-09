from datetime import datetime

class HistoryItem(BaseModel):
    id: int
    user_input: str
    ai_output: str
    created_at: datetime

    class Config:
        from_attributes = True