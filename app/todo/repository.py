from sqlalchemy import select
from app.todo.database import TaskOrm, new_session
from app.todo.shemas import STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id



    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            
            return task_models
        
    @classmethod
    async def update_task(cls,
                          task_id: int,
                          **update_data):
        async with new_session() as session:
            result = await session.execute(
                select(TaskOrm).where(TaskOrm.id == task_id)
            )
            task = result.scalar_one_or_none()

            for key, value in update_data.items():
                setattr(task, key, value)
            
            await session.commit()
            await session.refresh(task)
            return task
        
    @classmethod
    async def delete_task(cls, task_id: int):
        async with new_session() as session:
            result = await session.execute(
                select(TaskOrm).where(TaskOrm.id == task_id)
            )
            task = result.scalar_one_or_none()
            
            await session.delete(task)
            await session.commit()
