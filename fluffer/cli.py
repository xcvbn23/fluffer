import click

from fluffer.fluffer import extract
from fluffer.utils import setup_logger

logger = setup_logger(__name__)

@click.command()
@click.argument('url')
def extract_url(url: str):
    logger.debug("Extracting URL %s.", url)
    extract(url)

if __name__ == "__main__":
    extract_url()