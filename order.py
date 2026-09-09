from dataclasses import dataclass, field
from enum import Enum

class Side(Enum):
    BID="bid"
    ASK="ask"

class OrderType(Enum):
    LIMIT="limit"
    MARKET="market"

@dataclass
class Order:
    order_id: int
    side: Side
    order_type: OrderType
    price: float| None
    quantity: int
    remaining_quantity: int = field(init=False)
    
    def __post_init__(self):
        self.remaining_quantity=self.quantity

    timestamp: int # This is a monotonic counter, not actual time. This avoids float calculation errors.

