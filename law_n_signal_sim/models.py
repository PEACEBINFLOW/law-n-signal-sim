from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Tower:
    id: str
    g_layers: Tuple[str, ...]
    base_latency_ms: float
    jitter_ms: float
    center_frequency_mhz: float


@dataclass
class Device:
    id: str
    preferred_g_layer: str


@dataclass
class RouteSnapshot:
    device: str
    channel: str
    tower_id: str
    frequency: float
    g_layer: str
    latency_ms: float
    signal_quality: float

    def to_dict(self) -> dict:
        return {
            "device": self.device,
            "channel": self.channel,
            "tower_id": self.tower_id,
            "frequency": self.frequency,
            "g_layer": self.g_layer,
            "latency_ms": self.latency_ms,
            "signal_quality": self.signal_quality,
        }
