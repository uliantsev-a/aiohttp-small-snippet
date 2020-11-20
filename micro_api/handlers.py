from typing import Union

from aiohttp import web
from aiohttp.abc import AbstractView
from aiohttp.web import Request, StreamResponse
import micro_api


def healthcheck(_: Request) -> Union[StreamResponse, AbstractView]:
    return web.json_response(dict(
        healthy=True,
        version=micro_api.__version__
    ))
