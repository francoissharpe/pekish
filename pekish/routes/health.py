from fastapi import APIRouter

from pekish import schemas


router = APIRouter()


@router.get("/ping", response_model=schemas.Status)
def ping():
    return schemas.Status(message="ok")


@router.get("/report", response_model=schemas.Status)
def report():
    return schemas.Status(message="ok")
