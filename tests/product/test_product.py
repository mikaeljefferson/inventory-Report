from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="22",
        company_name="xesque",
        product_name="dele",
        manufacturing_date="2022-09-11",
        expiration_date="2024-06-20",
        serial_number="MMMM112",
        storage_instructions="cuidado produto fragil",
    )

    assert product.id == "22"
    assert product.company_name == "xesque"
    assert product.product_name == "dele"
    assert product.manufacturing_date == "2022-09-11"
    assert product.expiration_date == "2024-06-20"
    assert product.serial_number == "MMMM112"
    assert product.storage_instructions == "cuidado produto fragil"
