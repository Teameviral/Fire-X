import os

ENV = bool(os.environ.get("ENV", "ANYTHING"))
if ENV:
    from heroku_config import Var as Config
else:
    from localconfig import Config


Var = Config
