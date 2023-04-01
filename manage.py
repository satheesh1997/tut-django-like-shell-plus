#!/usr/bin/env python

import click
import datetime

from IPython import start_ipython


@click.group(help="Django Like Shell and Shell Plus")
def cli():
    ...


@cli.command(help="Django Like Shell")
def shell():
    start_ipython(argv=[])


@cli.command(help="Django Like Shell Plus", name="shell_plus")
def shell_plus():
    start_ipython(
        argv=[],
        user_ns={
            "datetime": datetime,
        },
    )


if __name__ == "__main__":
    cli.add_command(shell)
    cli.add_command(shell_plus)
    cli()
