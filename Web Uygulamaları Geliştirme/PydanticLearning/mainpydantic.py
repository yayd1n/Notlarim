from pydantic import BaseModel

class ProductPydantic(BaseModel):
    name: str
    price: float
    in_stock: bool

if __name__ == '__main__':
    external_data= {
        "name": "Laptop",
        "price": "999.99",
        "in_stock": "True"
    }

    product = ProductPydantic(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")

    )

print(type(product.in_stock))
print(type(product.price))
print(type(product.name))