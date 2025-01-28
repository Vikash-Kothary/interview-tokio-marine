from fastapi import FastAPI

from tokio_marine.infrastructure import routes

def create_app():
    app = FastAPI(
        title="interview-tokio-marine",
        description="TMHCC Insurance Underwriting Project - Senior Software Developer Interview Exercise.",
        version="0.1.0",
        docs_url="/",
    )
    routes.include_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
