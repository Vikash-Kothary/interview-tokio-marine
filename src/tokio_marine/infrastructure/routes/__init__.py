from fastapi import FastAPI

from tokio_marine.infrastructure.routes.api.v1 import policies


def include_app(app: FastAPI):
    app.include_router(policies.router)
