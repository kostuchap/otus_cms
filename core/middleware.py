from fastapi import Request, Response


def component_middleware(request: Request, call_next) -> Response:
    print(f"Request: {request.method} {request.url}")

    response = call_next(request)

    print(f"Response: {response.status_code}")

    return response
