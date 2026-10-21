"""
status_demo.py - Status Normalization Utility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normalizes various task and workflow status strings into canonical status states.
Python standard library only.
"""

from typing import Any


# Canonical status mapping dictionary (case-folded and stripped keys)
_STATUS_MAP: dict[str, str] = {
    "todo": "pending",
    "not started": "pending",
    "working": "in_progress",
    "in progress": "in_progress",
    "done": "completed",
    "finished": "completed",
}


def normalize_status(status: Any) -> str:
    """
    Normalize arbitrary status inputs to canonical status values.

    Canonical statuses:
        - "pending"
        - "in_progress"
        - "completed"
        - "unknown" (default for unmapped/unsupported values and non-string inputs)

    Rules:
        - Non-string inputs (None, int, bool, list, etc.) return "unknown".
        - Leading and trailing whitespace is stripped.
        - Matching is case-insensitive.
        - Unsupported/unrecognized values return "unknown".

    Args:
        status: The raw input status to normalize.

    Returns:
        str: Canonical status string.
    """
    if not isinstance(status, str):
        return "unknown"

    cleaned = status.strip().lower()
    return _STATUS_MAP.get(cleaned, "unknown")


# ============================================================================
# Test Cases (Using Python Standard Library unittest)
# ============================================================================

import unittest


class TestNormalizeStatus(unittest.TestCase):
    """Test suite covering all specification examples and edge cases."""

    def test_specification_examples(self):
        """Test all explicit examples requested in the specification."""
        self.assertEqual(normalize_status("todo"), "pending")
        self.assertEqual(normalize_status("not started"), "pending")
        self.assertEqual(normalize_status("working"), "in_progress")
        self.assertEqual(normalize_status("IN PROGRESS"), "in_progress")
        self.assertEqual(normalize_status("done"), "completed")
        self.assertEqual(normalize_status("finished"), "completed")
        self.assertEqual(normalize_status("cancelled"), "unknown")

    def test_case_insensitivity(self):
        """Verify case-insensitivity across various casings."""
        self.assertEqual(normalize_status("TODO"), "pending")
        self.assertEqual(normalize_status("ToDo"), "pending")
        self.assertEqual(normalize_status("Not Started"), "pending")
        self.assertEqual(normalize_status("Working"), "in_progress")
        self.assertEqual(normalize_status("DONE"), "completed")
        self.assertEqual(normalize_status("Finished"), "completed")

    def test_whitespace_handling(self):
        """Verify leading and trailing whitespace is safely ignored."""
        self.assertEqual(normalize_status("  todo  "), "pending")
        self.assertEqual(normalize_status("\tnot started\n"), "pending")
        self.assertEqual(normalize_status("   working   "), "in_progress")
        self.assertEqual(normalize_status("  IN PROGRESS  "), "in_progress")
        self.assertEqual(normalize_status(" done "), "completed")
        self.assertEqual(normalize_status("\nfinished\t"), "completed")

    def test_non_string_inputs(self):
        """Verify non-string inputs return 'unknown'."""
        self.assertEqual(normalize_status(None), "unknown")
        self.assertEqual(normalize_status(123), "unknown")
        self.assertEqual(normalize_status(45.67), "unknown")
        self.assertEqual(normalize_status(True), "unknown")
        self.assertEqual(normalize_status(False), "unknown")
        self.assertEqual(normalize_status([]), "unknown")
        self.assertEqual(normalize_status({}), "unknown")
        self.assertEqual(normalize_status(object()), "unknown")

    def test_unsupported_and_empty_strings(self):
        """Verify unmapped or empty strings return 'unknown'."""
        self.assertEqual(normalize_status(""), "unknown")
        self.assertEqual(normalize_status("   "), "unknown")
        self.assertEqual(normalize_status("archived"), "unknown")
        self.assertEqual(normalize_status("blocked"), "unknown")
        self.assertEqual(normalize_status("random_status_123"), "unknown")


if __name__ == "__main__":
    print("=" * 60)
    print("Running normalize_status Demonstration & Unit Tests")
    print("=" * 60)

    # Quick visual demonstration
    sample_inputs = [
        "todo",
        "not started",
        "working",
        "IN PROGRESS",
        "done",
        "finished",
        "cancelled",
        "  todo  ",
        None,
        123,
        "blocked",
    ]

    print("\nDemonstration Results:")
    for item in sample_inputs:
        result = normalize_status(item)
        print(f"  {repr(item):<20} -> {repr(result)}")

    print("\n" + "-" * 60)
    print("Running unittest test suite...")
    print("-" * 60)

    # Run unittest
    unittest.main(verbosity=2)
