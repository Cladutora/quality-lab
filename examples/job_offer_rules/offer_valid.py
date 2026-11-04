"""Shared validity rules for remote-job CRM rows."""

from __future__ import annotations

from schema import REVIEW_STATUSES, TERMINAL_STATUSES


def is_valid_offer(row: dict[str, str]) -> bool:
    if (row.get("tier") or "").strip() != "Priority":
        return False
    if (row.get("remote_ok") or "").strip().lower() not in {"yes", "true", "1", "y"}:
        return False
    if (row.get("applied_date") or "").strip():
        return False
    if not (row.get("job_url") or "").strip():
        return False
    status = (row.get("status") or "").strip().lower()
    if status in TERMINAL_STATUSES or status in REVIEW_STATUSES:
        return False
    if status.startswith("applied"):
        return False
    return True


def is_review_offer(row: dict[str, str]) -> bool:
    if not (row.get("job_url") or "").strip():
        return False
    status = (row.get("status") or "").strip().lower()
    if status in TERMINAL_STATUSES or status.startswith("applied"):
        return False
    if status in REVIEW_STATUSES:
        return True
    notes = (row.get("notes") or "").lower()
    return "review:" in notes or "skipped:" in notes
