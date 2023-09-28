from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
from typing import List


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        if not self.path.endswith('.json'):
            raise ValueError("Invalid file format")

        with open(self.path, 'r') as file:
            data = json.load(file)

        response = [
            Product(
                id=product['id'],
                product_name=product['product_name'],
                company_name=product['company_name'],
                manufacturing_date=product['manufacturing_date'],
                expiration_date=product['expiration_date'],
                serial_number=product['serial_number'],
                storage_instructions=product['storage_instructions'],
            )
            for product in data
        ]

        return response


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
