from fastapi import APIRouter
from schemas.request import AskRequest
from agent.logic import generate_plan

from db.database import SessionLocal
from db.models import RequestLog

from typing import List
from schemas.request import HistoryItem

router = APIRouter()


@router.post("/ask")
def ask_agent(request: AskRequest):
    db = SessionLocal()

    result = generate_plan(request.input)

    # salva nel DB
    log = RequestLog(
        user_input=request.input,
        ai_output=result
    )

    db.add(log)
    db.commit()
    db.close()

    return {"response": result}

@router.get("/history", response_model=List[HistoryItem])
def get_history():
    db = SessionLocal()

    logs = db.query(RequestLog).order_by(RequestLog.created_at.desc()).all()

    db.close()

    return logs