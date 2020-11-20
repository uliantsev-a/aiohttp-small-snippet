import logging

from micro_api.utils import load_config

__version__ = '0.1.0'

logger = logging.getLogger('MicroAPI')
config = load_config()
