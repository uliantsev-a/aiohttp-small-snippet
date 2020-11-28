import logging

import faust
from faust.app.base import BootStrategy as BaseBootStrategy

from micro_api.handlers import database_health_check

logger = logging.getLogger('Checker')


class App(faust.App):
    producer_only = True

    class BootStrategy(BaseBootStrategy):
        enable_kafka = False


app = App(
    'independent_checker',
    version=1,
    autodiscover=True,
    on_leader=True,
    origin='micro_api'  # imported name for this project
)


@app.crontab("* * * * *")
async def periodically_checker():
    db_health = database_health_check()
    if db_health:
        logger.info('without accidents')
    else:
        logger.warning('DB isn\'t available')


def main() -> None:
    app.main()
