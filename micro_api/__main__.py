from mode import Worker

import micro_api
from micro_api import logger
from micro_api.app import MicroService
from micro_api.utils import configure_logging


def main():
    configure_logging()

    logger.info("Micro API version %s", micro_api.__version__)
    Worker(MicroService(), loglevel="info").execute_from_commandline()


main()
