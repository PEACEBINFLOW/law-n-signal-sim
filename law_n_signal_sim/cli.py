from __future__ import annotations
import argparse

from .simulator import SignalSimulator
from .exporters import format_table


def main() -> None:
    parser = argparse.ArgumentParser(description="Law-N signal simulator (network.routes generator)")
    parser.add_argument("--steps", type=int, default=5, help="Number of timesteps to simulate")
    parser.add_argument("--devices", type=int, default=5, help="Number of devices (if using default topology)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible runs")
    args = parser.parse_args()

    sim = SignalSimulator(
        devices=None,  # default_devices will use args.devices indirectly
        towers=None,
        seed=args.seed,
    )

    # quick hack: adjust device count if using default
    if args.devices != len(sim.devices):
        from .topology import default_devices
        sim.devices = default_devices(num_devices=args.devices)

    for t, routes in sim.run(steps=args.steps):
        print(f"t={t}")
        print(format_table(routes))
        print()


if __name__ == "__main__":
    main()
