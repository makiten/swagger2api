from click import (command, echo, option, argument, File)
from colorama import (Fore, Style)
from message import Output
import importlib
import json
import sys


@command()
@argument('swagger', type=File('rb'))
@option('-a',
        '--adapter',
        default='javascript',
        help='The language to output to')
def cli(swagger, adapter):
    try:
        converter = importlib.import_module(
            '.{0}'.format(adapter.lower()),
            'adapters'
        )

        echo(converter.convert(swagger.read()))
    except Exception as e:
        echo(e)
        echo(
            Output.error(
                'Could not convert file. Package ' +
                Style.BRIGHT +
                Fore.YELLOW +
                'swagger2api.adapters.{0}'.format(adapter.lower()) +
                Style.RESET_ALL +
                ' does not exist.'
            )
        )
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    cli()
