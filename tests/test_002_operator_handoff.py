import unittest

from readmission_signal_board.models import Record
from readmission_signal_board.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="patient-002", exposure=59102, signal=0.844, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
