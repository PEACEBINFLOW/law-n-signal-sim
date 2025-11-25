from __future__ import annotations
from typing import List
import random

from .models import Tower, Device


def default_towers() -> List[Tower]:
    return [
        Tower(
            id="TWR-001",
            g_layers=("5G", "4G"),
            base_latency_ms=30.0,
            jitter_ms=12.0,
            center_frequency_mhz=3600.0,
        ),
        Tower(
            id="TWR-002",
            g_layers=("4G",),
            base_latency_ms=45.0,
            jitter_ms=15.0,
            center_frequency_mhz=1800.0,
        ),
        Tower(
            id="TWR-003",
            g_layers=("3G",),
            base_latency_ms=90.0,
            jitter_ms=25.0,
            center_frequency_mhz=900.0,
        ),
    ]


def default_devices(num_devices: int = 5) -> List[Device]:
    base_ids = ["0xA4C1", "0xB9F0", "0xC7AA", "0xD123", "0xE777"]
    layers = ["5G", "4G", "4G", "3G", "5G"]

    devices: List[Device] = []
    for i in range(num_devices):
        idx = i % len(base_ids)
        dev_id = base_ids[idx]
        if i >= len(base_ids):
            dev_id = f"{dev_id[:-1]}{i:02X}"
        devices.append(Device(id=dev_id, preferred_g_layer=layers[idx]))
    return devices


def choose_tower_for_device(device: Device, towers: List[Tower]) -> Tower:
    preferred = [t for t in towers if device.preferred_g_layer in t.g_layers]
    if preferred:
        return random.choice(preferred)
    return random.choice(towers)
