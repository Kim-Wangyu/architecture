from dataclasses import dataclass
from msilib.schema import Class


@dataclass
class Domain:
    ...


@dataclass
class User(Domain):
    name: str


@dataclass
class Product(Domain):
    name: str
