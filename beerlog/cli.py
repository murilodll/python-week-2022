from typing import Optional

import typer
from rich import print
from rich.console import Console
from rich.table import Table

from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer App")
console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adiciona Novas Cervejas"""
    # print(name, style, flavor, image, cost)
    if add_beer_to_database(name, style, flavor, image, cost):
        print("New BEER!!")
    else:
        print("Fail My Friend")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """Lista as Cervejas"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog")
    headers = [
        "id",
        "name",
        "flavor",
        "style",
        "cost",
        "image",
        "rate",
        "date",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
