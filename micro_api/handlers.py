from typing import Union

from aiohttp import web
from aiohttp.abc import AbstractView
from aiohttp.web import Request, StreamResponse

import micro_api
from micro_api.models import db


def database_health_check() -> bool:
    try:
        # to check database we will execute raw query
        db.session.query("1").from_statement("SELECT 1").all()
        return True
    except Exception:
        return False


def home(request: Request) -> None:
    location = request.app.router['healthcheck'].url_for()
    raise web.HTTPFound(location=location)


def healthcheck(_: Request) -> Union[StreamResponse, AbstractView]:
    return web.json_response(dict(
        healthy=True,
        database_healthy=database_health_check(),
        version=micro_api.__version__
    ))
