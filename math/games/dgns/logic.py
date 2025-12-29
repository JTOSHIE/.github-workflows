import random
from dataclasses import dataclass
from typing import Set, Tuple, List


@dataclass(frozen=True)
class Win:
    symbol: str
    length: int
    ways: int
    payout: int
    positions: Set[Tuple[int, int]]


def play_spin(rng, bet):
    # DGNS Megaways Logic: 6 Reels, 2-7 Height
    heights = [rng.randint(2, 7) for _ in range(6)]
    board = [[rng.choice(["A", "K", "Q", "J", "T", "P1", "W"]) for _ in range(h)] for h in heights]

    # Simple evaluation for simulation
    total_win = 0
    if rng.random() < 0.25:  # 25% hit rate for sim
        total_win = bet * rng.choice([0.5, 1, 2, 5, 10])

    return {"total_win": int(total_win), "board": board}
