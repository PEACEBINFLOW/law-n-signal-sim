from law_n_signal_sim.models import Tower, Device
from law_n_signal_sim.simulator import SignalSimulator

towers = [
    Tower(id="TWR-001", g_layers=("5G", "4G"), base_latency_ms=25.0, jitter_ms=10.0, center_frequency_mhz=3600.0),
    Tower(id="TWR-002", g_layers=("4G",),        base_latency_ms=45.0, jitter_ms=15.0, center_frequency_mhz=1800.0),
]

devices = [
    Device(id="0xA4C1", preferred_g_layer="5G"),
    Device(id="0xB9F0", preferred_g_layer="4G"),
]

sim = SignalSimulator(towers=towers, devices=devices)
for t, routes in sim.run(steps=2):
    print(f"t={t} routes={len(routes)}")
