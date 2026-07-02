def evaluate_parameter(value, limits):

    limit_type = limits.get("type")

    # ---------------- MAX TYPE ----------------
    if limit_type == "max":
        max_val = limits["max"]

        if value <= max_val:
            return 1.0, "safe"

        deviation = (value - max_val) / max_val

        if deviation <= 0.2:
            return 0.7, "warning"
        else:
            return 0.0, "critical"

    # ---------------- MIN TYPE ----------------
    if limit_type == "min":
        min_val = limits["min"]

        if value >= min_val:
            return 1.0, "safe"

        deviation = (min_val - value) / min_val

        if deviation <= 0.2:
            return 0.7, "warning"
        else:
            return 0.0, "critical"

    # ---------------- RANGE TYPE ----------------
    if limit_type == "range":
        min_val = limits["min"]
        max_val = limits["max"]

        if min_val <= value <= max_val:
            return 1.0, "safe"

        if value < min_val:
            deviation = (min_val - value) / min_val
        else:
            deviation = (value - max_val) / max_val

        if deviation <= 0.2:
            return 0.7, "warning"
        else:
            return 0.0, "critical"

    return 0, "unknown"