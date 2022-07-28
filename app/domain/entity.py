from dataclasses import dataclass
from msilib.schema import Class


@dataclass
class User:
    name: str


@dataclass
class Product:
    name: str
