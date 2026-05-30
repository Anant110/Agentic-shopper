import pandas as pd
from pydantic import BaseModel, Field

orders_df = pd.read_csv(
    "data/orders.csv"
)
# print(orders_df)

# Getting an order

class OrderIdInput(BaseModel):
    order_id:str=Field(description="Order ID like O0001, O0002, O0009 etc")

def get_order(order_id):
    """Fetch order information using order ID."""
    order = orders_df[
        orders_df["order_id"] == order_id
    ]

    if order.empty:
        return None

    return order.iloc[0].to_dict()

if __name__ == "__main__":
    print("Testing get_order...")

    result = get_order("O0009")

    print(result)