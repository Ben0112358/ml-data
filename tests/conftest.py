import importlib
import sys

import pytest


def _purge_package(prefix: str) -> None:
    for name in list(sys.modules):
        if name == prefix or name.startswith(prefix + "."):
            del sys.modules[name]


@pytest.fixture
def ml_data_env(monkeypatch, tmp_path):
    monkeypatch.setenv("ML_HOMELAB_ROOT", str(tmp_path))
    monkeypatch.setenv("OUTPUT_SUFFIX", "smoke_suffix")
    monkeypatch.setenv("RAW_DATA_DIR", "data/raw")
    monkeypatch.setenv("CLEAN_DATA_DIR", "data/clean")
    monkeypatch.setenv("LOGS_DIR", "logs/data")
    _purge_package("ml_data")
    importlib.import_module("ml_data.config")
    yield
