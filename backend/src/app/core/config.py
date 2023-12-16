# Standard Library
import logging
from logging.config import dictConfig

import environ

dictConfig(
    config={
        'version': 1,
        'formatters': {
            'f': {
                'format': '{"level": "%(levelname)-4s", "timestamp": "%(asctime)s", '
                          '"module": "%(name)s", "body": "%(message)s"}'
            }
        },
        'handlers': {
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.INFO}
        },
        'root': {
            'handlers': ['h'],
            'level': logging.INFO,
        }
    }
)


@environ.config(prefix='')
class AppConfig:
    @environ.config(prefix="API")
    class API:
        host = environ.var()
        title = environ.var()
        version = environ.var()
        prefix = environ.var()
        debug = environ.bool_var()
        allowed_hosts = environ.var()

    @environ.config(prefix="MONGO")
    class Mongo:
        host = environ.var()
        port = environ.var(converter=int)
        username = environ.var()
        password = environ.var()
        db = environ.var()
        configs_collection = environ.var()

    @environ.config(prefix="JWT")
    class JWT:
        access_token_expire_minutes = environ.var(converter=int)
        private_key = environ.var()
        public_key = environ.var()
        algorithm = environ.var()

    env = environ.var()

    api: API = environ.group(API)
    jwt: JWT = environ.group(JWT)
    mongo: Mongo = environ.group(Mongo)


CONFIG: AppConfig = AppConfig.from_environ()  # type: ignore
