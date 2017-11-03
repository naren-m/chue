from utils import http

import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter


def print_json_obj(json_object):
    json_str = json.dumps(json_object, indent=4, sort_keys=True)
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))


def print_json_str(json_str):
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))
