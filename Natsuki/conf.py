import sys
from envparse import env
from HexzyBot import LOGGER


DEFAULTS = {
    "LOAD_MODULES": True,
}

def get_str_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.str(name, default=default)) and not required:
        LOGGER.warn("No str key: " + name)
        return None
    elif not data:
        LOGGER.critical("No str key: " + name)
        sys.exit(2)
    else:
        return data

def get_int_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.int(name, default=default)) and not required:
        LOGGER.warn("No int key: " + name)
        return None
    elif not data:
        LOGGER.critical("No int key: " + name)
        sys.exit(2)
    else:
        return data
    
def get_list_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.list(name, default=default)) and not required:
        LOGGER.warn("No list key: " + name)
        return []
    elif not data:
        LOGGER.critical("No list key: " + name)
        sys.exit(2)
    else:
        return data


def get_bool_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.bool(name, default=default)) and not required:
        LOGGER.warn("No bool key: " + name)
        return False
    elif not data:
        LOGGER.critical("No bool key: " + name)
        sys.exit(2)
    else:
        return data
