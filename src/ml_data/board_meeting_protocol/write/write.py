import json
import pathlib as pl


def write(payload: dict, path: pl.Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")
