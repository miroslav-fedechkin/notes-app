from fastapi import HTTPException, status


class NotesExceptions(HTTPException):
    status_code = 500
    detail = ''
    def __init__(self):
        super().__init__(
            status_code = self.status_code, 
            detail = self.detail
            )
        

class TaskDoesNotExist(NotesExceptions):
    status_code = status.HTTP_403_FORBIDDEN
    details = 'This task does not exist'

