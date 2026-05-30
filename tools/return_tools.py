from datetime import datetime
import sys
sys.path.append('/tools/')
from tools.order_tools import get_order
from tools.product_tools import get_product
from pydantic import BaseModel, Field

with open("data/policy.txt","r") as file:
    POLICY_TEXT=file.read()

print(POLICY_TEXT)

class GetOrderId(BaseModel):
    order_id:str=Field(description="Order ID like O0001, O0002, O0009")

def evaluate_return(order_id):
    """
    Determine whether an order is eligible
    for return according to company policy.
    """

    order = get_order(order_id)

    if not order:
        return {
            "allowed": False,
            "reason": "Order not found"
        }

    product = get_product(
        order["product_id"]
    )

    if not product:
        return {
            "allowed": False,
            "reason": "Product not found"
        }

    order_date = datetime.strptime(
        order["order_date"],
        "%Y-%m-%d"
    )

    days_since = (
        datetime.now() - order_date
    ).days

    # Clearance Rule
    if product["is_clearance"]:

        return {
            "allowed": False,
            "reason":
            "Clearance items are final sale"
        }

    # Sale Rule
    if product["is_sale"]:

        if days_since > 7:

            return {
                "allowed": False,
                "reason":
                "Sale item return window expired"
            }

    # Vendor Exception
    if product["vendor"] == \
        "Aurelia Couture":

        return {
            "allowed": False,
            "reason":
            "Vendor allows exchange only"
        }

    # Normal Rule
    if days_since > 14:

        return {
            "allowed": False,
            "reason":
            "Normal return window expired"
        }

    return {
        "allowed": True,
        "reason":
        "Eligible for return"
    }