from dataclasses import dataclass
from enum import Enum

class OrderStatus(str, Enum):
    """
    Enum for order status
    """
    NEW = "new"
    PARTIALLY_FILLED = "partially_filled"
    FILLED = "filled"
    CANCELED = "canceled"
    REJECTED = "rejected"

@dataclass
class Order:
    status: OrderStatus
    symbol: str         # Symbol of the order


order = Order(status=OrderStatus.NEW, symbol="AAPL")
print(order)
