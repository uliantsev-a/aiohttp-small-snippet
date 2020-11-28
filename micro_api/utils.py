import collections
import logging
import logging.config
import os
import sys
from argparse import ArgumentParser
from addict import Dict

import yaml
from dotenv import load_dotenv


def configure_logging():
    curr_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.dirname(os.path.abspath(__name__))
    log_path = os.path.join(root_path, 'log')

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    with open(os.path.join(curr_path, 'logging.yml'), 'rt') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)


def get_parser():
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "--log-level", default="INFO",
        help="Python logging level [default: %(default)s]",
    )
    parser.add_argument(
        "--web-host", default="localhost",
        help="Web server host [default: %(default)s]",
    )
    parser.add_argument(
        "--web-port", default="8080", type=int,
        help="Web server port [default: %(default)s]",
    )
    parser.add_argument("--postgres_user")
    parser.add_argument("--postgres_password")
    parser.add_argument("--postgres_host")
    parser.add_argument("--postgres_port", type=int)
    parser.add_argument("--postgres_db")
    return parser


def load_config():
    """
    Define configuration from environment or arguments
    with this order for priority.
    :return: Dict of config
    """
    if 'alembic' in sys.argv[0]:
        return Dict()
    cm = collections.ChainMap()

    parser = get_parser()
    args = vars(parser.parse_args())
    cm = cm.new_child(args)

    env_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(env_dir, ".env"))

    env = {}
    for k, v in os.environ.items():
        k = k.lower()
        if k not in cm:
            continue
        env[k] = v
    cm = cm.new_child(env)

    return Dict(**cm)
