import pandas as pd
import ast

inventory_df=pd.read_csv("data/product_inventory.csv")
# print(inventory_df)

from pydantic import BaseModel, Field
from typing import Optional, List


class SearchProductsInput(BaseModel):
    max_price: Optional[float] = None
    size: Optional[str] = None
    is_sale: Optional[bool] = None
    tags: Optional[List[str]] = None


def search_products(
    max_price=None,
    size=None,
    is_sale=None,
    tags=None
):
    """
    Search products based on price, size,
    sale status and product tags.
    """

    results = inventory_df.copy()

    # Price filtering
    if max_price:
        results = results[
            results["price"] <= max_price
        ]

    # Sale filtering
    if is_sale is not None:
        results = results[
            results["is_sale"] == is_sale
        ]

    # Tag filtering
    if tags:
        for tag in tags:
            results = results[
                results["tags"].str.contains(
                    tag,
                    case=False,
                    na=False
                )
            ]

    # Size stock filtering
    if size:

        def check_stock(row):

            stock = ast.literal_eval(
                row["stock_per_size"]
            )

            return stock.get(str(size), 0) > 0

        results = results[
            results.apply(check_stock, axis=1)
        ]

    # Bestsellers first
    results = results.sort_values(
        by="bestseller_score",
        ascending=False
    )

    return results.head(5).to_dict(
        orient="records"
    )
    
class productInput(BaseModel):
    product_id: str = Field(description="The product ID to retrieve")
# create the product
def get_product(product_id):
    
    """Get product details using product ID."""

    product = inventory_df[
        inventory_df["product_id"] == product_id
    ]

    if product.empty:
        return {"error": "Product not found"}
    
    return product.iloc[0].to_dict()