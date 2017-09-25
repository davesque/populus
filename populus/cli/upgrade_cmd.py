import logging
import click
from .main import main

from populus.api.upgrade import (
    upgrade_project,
)

from populus.config.versions import (
    LATEST_VERSION,
)


@main.command('upgrade')
@click.pass_context
@click.option(
    '-t',
    '--to-version',
    'to_version',
    default=LATEST_VERSION,
)
def upgrade_cmd(ctx, to_version):
    """
    Generate project layout with an example contract.
    """
    logger = logging.getLogger('populus.cli.upgrade')
    project_dir = ctx.obj['PROJECT_DIR']

    upgrade_project(project_dir, logger)
