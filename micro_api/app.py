from aiohttp import web
from mode import Service

from micro_api import logger
from micro_api.handlers import healthcheck


class MicroService(Service):
    def __init__(self, web_host: str = 'localhost', web_port: int = 8080):
        super().__init__()
        self.app = web.Application()
        self.host = web_host
        self.port = web_port
        self.runner = None
        self.site = None

    async def on_start(self):
        self.runner = web.AppRunner(self.app)
        self._configure_router()
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()
        logger.info("Serving on %s:%s", self.host, self.port)

    def _configure_router(self):
        self.app.router.add_route("GET", "/healthcheck", healthcheck)

    async def on_stop(self):
        if self.runner is not None:
            await self.runner.cleanup()
