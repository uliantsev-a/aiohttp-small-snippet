import collections
import logging
import logging.config
import os
from argparse import ArgumentParser
from addict import Dict

import yaml


def configure_logging():
    with open('logging.yml', 'rt') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)


def get_parser():
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "--log-level", default="INFO",
        help="Python logging level [default: %(default)s]")
    parser.add_argument(
        "--web-host", default="0.0.0.0",
        help="Web server host [default: %(default)s]"
    )
    parser.add_argument("--web-port", default="8080", help="Web server port [default: %(default)s]")
    return parser


def load_config():
    """
    Define configuration from environment or arguments
    with this order for priority.
    :return: Dict of config
    """
    cm = collections.ChainMap()
    parser = get_parser()
    cm = cm.new_child(vars(parser.parse_args()))

    env = {}
    for k, v in os.environ.items():
        k = k.lower()
        if k not in cm:
            continue
        env[k] = v
    cm = cm.new_child(env)

    return Dict(**cm)
