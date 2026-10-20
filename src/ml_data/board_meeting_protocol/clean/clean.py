def clean(payload: dict) -> dict:
    """Pass the marker through unchanged."""
    if payload.get("corpus") != "none":
        raise ValueError("Expected corpus none")
    return dict(payload)
