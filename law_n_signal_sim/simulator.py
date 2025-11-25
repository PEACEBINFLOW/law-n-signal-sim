from __future__ import annotations
from typing import Iterable, List, Tuple
import random

from .models import Tower, Device, RouteSnapshot
from .topology import default_towers, default_devices, choose_tower_for_device


_CHANNEL_NAMES = ["Delta", "Gamma", "Omega", "Theta"]


class SignalSimulator:
    def __init__(
        self,
        towers: List[Tower] | None = None,
        devices: List[Device] | None = None,
        seed: int | None = None,
    ) -> None:
        self.towers = towers or default_towers()
        self.devices = devices or default_devices()
        self._rng = random.Random(seed)

    def step(self, t: int) -> List[RouteSnapshot]:
        snapshots: List[RouteSnapshot] = []

        for dev in self.devices:
            tower = choose_tower_for_device(dev, self.towers)
            latency = self._latency_for_tower(tower)
            quality = self._quality_from_latency(latency)
            channel = self._make_channel(tower, dev)

            snapshots.append(
                RouteSnapshot(
                    device=dev.id,
                    channel=channel,
                    tower_id=tower.id,
                    frequency=tower.center_frequency_mhz,
                    g_layer=dev.preferred_g_layer,
                    latency_ms=latency,
                    signal_quality=quality,
                )
            )

        return snapshots

    def run(self, steps: int = 5) -> Iterable[Tuple[int, List[RouteSnapshot]]]:
        for t in range(steps):
            yield t, self.step(t)

    # ---- internal helpers ----

    def _latency_for_tower(self, tower: Tower) -> float:
        jitter = self._rng.gauss(0.0, tower.jitter_ms)
        latency = max(5.0, tower.base_latency_ms + jitter)
        return round(latency, 2)

    def _quality_from_latency(self, latency_ms: float) -> float:
        q = 1.0 - (latency_ms / 200.0)
        q = max(0.0, min(1.0, q))
        return round(q, 2)

    def _make_channel(self, tower: Tower, dev: Device) -> str:
        name = self._rng.choice(_CHANNEL_NAMES)
        idx = int(tower.center_frequency_mhz // 100) % 100
        return f"{name}.Freq({idx})"
