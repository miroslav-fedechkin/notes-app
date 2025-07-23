from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from shemas import STask, STaskAdd, STaskId


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post('/add_task')
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return STaskId(id=task_id)


@router.get('/')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

