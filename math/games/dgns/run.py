from logic import play_spin
import random


def run_test(spins=1000):
    total_bet = 100 * (10**8)
    wins = 0
    print("Starting JTOSHIE DGNS Simulation...")
    for _ in range(spins):
        res = play_spin(random.Random(), total_bet)
        wins += res["total_win"]

    rtp = (wins / (spins * total_bet)) * 100
    print(f"Results: {rtp:.2f}% RTP")


if __name__ == "__main__":
    run_test()
