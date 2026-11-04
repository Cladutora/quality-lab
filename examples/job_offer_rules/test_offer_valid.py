"""Portfolio validation using synthetic records only."""
import unittest
from offer_valid import is_valid_offer, is_review_offer


class OfferSelectionTests(unittest.TestCase):
    def row(self, **changes):
        row = dict(tier='Priority', remote_ok='yes', job_url='https://example.com/job/1', status='New', applied_date='')
        row.update(changes)
        return row

    def test_actionable_priority_remote_offer(self):
        self.assertTrue(is_valid_offer(self.row()))

    def test_all_supported_remote_flags(self):
        for flag in ['yes', 'TRUE', '1', ' y ']:
            with self.subTest(flag=flag):
                self.assertTrue(is_valid_offer(self.row(remote_ok=flag)))

    def test_nonpriority_or_nonremote_excluded(self):
        for changes in [dict(tier='Other'), dict(remote_ok='no'), dict(remote_ok='')]:
            with self.subTest(changes=changes):
                self.assertFalse(is_valid_offer(self.row(**changes)))

    def test_missing_url_excluded_from_both_queues(self):
        row = self.row(job_url=' ', status='Review')
        self.assertFalse(is_valid_offer(row))
        self.assertFalse(is_review_offer(row))

    def test_application_date_excludes_actionable_offer(self):
        self.assertFalse(is_valid_offer(self.row(applied_date='2026-01-01')))

    def test_terminal_statuses_excluded(self):
        for status in ['Applied', 'Interview', 'Offer', 'Rejected', 'Withdrawn', 'Closed', 'Declined', 'Discarded']:
            with self.subTest(status=status):
                row = self.row(status=status, notes='review: synthetic example')
                self.assertFalse(is_valid_offer(row))
                self.assertFalse(is_review_offer(row))

    def test_applied_prefix_excluded(self):
        row = self.row(status='Applied - quiz pending')
        self.assertFalse(is_valid_offer(row))
        self.assertFalse(is_review_offer(row))

    def test_review_statuses_go_to_review_queue(self):
        for status in ['Review', 'Deferred', 'Hold', 'Skipped']:
            with self.subTest(status=status):
                row = self.row(status=status)
                self.assertFalse(is_valid_offer(row))
                self.assertTrue(is_review_offer(row))

    def test_notes_markers_trigger_review(self):
        for note in ['REVIEW: confirm scope', 'skipped: confirm location']:
            self.assertTrue(is_review_offer(self.row(notes=note)))

    def test_incomplete_record_is_not_actionable(self):
        self.assertFalse(is_valid_offer({}))
        self.assertFalse(is_review_offer({}))


if __name__ == '__main__':
    unittest.main()
