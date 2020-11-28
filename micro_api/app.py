import logging
from typing import Optional

from aiohttp import web
from mode import Service

from micro_api import config
from micro_api.faust_app import app as faust_app
from micro_api.handlers import healthcheck, home

logger = logging.getLogger('MicroAPI')


class MicroService(Service):
    def __init__(
        self,
        web_host: Optional[str] = None,
        web_port: Optional[int] = None,
    ):
        super().__init__()
        self.app = web.Application()
        logger.info("host on %s", config.web_host)
        self.host = web_host or config.web_host
        self.port = web_port or config.web_port
        self.runner = None
        self.site = None

    def on_init_dependencies(self):
        return [faust_app]

    async def on_start(self):
        self.runner = web.AppRunner(self.app)
        self._configure_router()
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()
        logger.info("Serving on %s:%s", self.host, self.port)

    def _configure_router(self):
        self.app.router.add_route("GET", "/", home, name='home')
        self.app.router.add_route("GET", "/healthcheck", healthcheck, name='healthcheck')

    async def on_stop(self):
        if self.runner is not None:
            await self.runner.cleanup()
