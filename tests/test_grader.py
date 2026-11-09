import unittest
from sigma_geo.grader import grade

class GraderTests(unittest.TestCase):
    def test_correct_response_passes(self):
        self.assertTrue(grade("stale_evidence", True, {"label":"stale_evidence","abstain":True,"rationale":"Old."})["passed"])
    def test_wrong_label_fails(self):
        self.assertFalse(grade("stale_evidence", True, {"label":"supported","abstain":True,"rationale":"No."})["passed"])
    def test_false_abstention_is_detected(self):
        r = grade("invariant_under_valid_reprojection", False, {"label":"invariant_under_valid_reprojection","abstain":True,"rationale":"Unsure."})
        self.assertTrue(r["false_abstention"])
        self.assertFalse(r["passed"])
    def test_malformed_response_fails_safely(self):
        self.assertFalse(grade("stale_evidence", True, None)["passed"])
    def test_missing_rationale_fails(self):
        self.assertFalse(grade("stale_evidence", True, {"label":"stale_evidence","abstain":True})["passed"])

if __name__ == "__main__":
    unittest.main()
