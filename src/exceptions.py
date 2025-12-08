from fastapi import HTTPException, status

def unauthorized(detail: str = "Unauthorized"):
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

def bad_request(detail: str = "Bad request"):
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

def not_found(detail: str = "Not Found"):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
