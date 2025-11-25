from law_n_signal_sim.models import Tower, Device
from law_n_signal_sim.simulator import SignalSimulator

if __name__ == "__main__":
    towers = [
        Tower(id="TWR-001", g_layers=("5G", "4G"), base_latency_ms=25.0, jitter_ms=10.0, center_frequency_mhz=3600.0),
        Tower(id="TWR-002", g_layers=("4G",),        base_latency_ms=40.0, jitter_ms=12.0, center_frequency_mhz=1800.0),
        Tower(id="TWR-003", g_layers=("3G",),        base_latency_ms=80.0, jitter_ms=20.0, center_frequency_mhz=900.0),
    ]

    devices = [
        Device(id="0xA4C1", preferred_g_layer="5G"),
        Device(id="0xB9F0", preferred_g_layer="4G"),
        Device(id="0xC7AA", preferred_g_layer="4G"),
        Device(id="0xD123", preferred_g_layer="5G"),
    ]

    sim = SignalSimulator(towers=towers, devices=devices)
    for t, routes in sim.run(steps=2):
        print(f"t={t}, routes={len(routes)}")
        for row in routes:
            print(row)
        print()
