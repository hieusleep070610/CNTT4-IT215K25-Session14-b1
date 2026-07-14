from datetime import datetime
from schemas.reponse import BaseResponse


def create_response(
        status_code: int,
        message: str,
        path: str,
        data=None,
        error=None
):
    return BaseResponse(
        statusCode=status_code,
        message=message,
        error=error,
        data=data,
        path=path,
        timestamp=datetime.now()
    )