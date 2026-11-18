#!/usr/bin/env python3
"""Dependency-free structural audit for educational Solidity exercises."""
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
tests = sorted((root / "src" / "test").glob("*.sol"))
errors = []
entries = []
for path in tests:
    data = path.read_text(encoding="utf-8")
    pragmas = re.findall(r"^\s*pragma\s+solidity\s+([^;]+);", data, re.M)
    if len(pragmas) != 1:
        errors.append(f"{path.name}: expected exactly one Solidity pragma")
    if "SPDX-License-Identifier:" not in data[:300]:
        errors.append(f"{path.name}: missing SPDX license identifier")
    if "forge-std/Test.sol" not in data:
        errors.append(f"{path.name}: missing Foundry test import")
    entries.append({"file": str(path.relative_to(root)), "pragma": pragmas[0] if pragmas else None,
                    "test_functions": len(re.findall(r"\bfunction\s+test\w*\s*\(", data))})
if not tests:
    errors.append("No Solidity exercises found")
report = {"exercise_files": len(tests), "entries": entries, "errors": errors}
print(json.dumps(report, indent=2))
sys.exit(1 if errors else 0)
