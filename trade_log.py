from dataclasses import dataclass
from order import Side

@dataclass
class Trade:
    trade_id: int
    price: float
    quantity: int
    aggressor_side: Side
    resting_order_id: int
    incoming_order_id: int
    timestamp: int