from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "22",
        "xesque",
        "dele",
        "2022-09-11",
        "2024-06-20",
        "MMMM112",
        "cuidado produto fragil",
    )
    assert product.__str__() == (
        f"The product {product.id} - {product.product_name} "
        f"with serial number {product.serial_number} "
        f"manufactured on {product.manufacturing_date} "
        f"by the company {product.company_name} "
        f"valid until {product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )
