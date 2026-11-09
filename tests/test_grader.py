import unittest
from sigma_geo.grader import grade


class GraderTests(unittest.TestCase):
    def test_correct_response_passes(self):
        result = grade("stale_evidence", True, {"label":"stale_evidence","abstain":True,"rationale":"Out of date."})
        self.assertTrue(result["passed"])

    def test_wrong_label_fails(self):
        result = grade("stale_evidence", True, {"label":"supported","abstain":True,"rationale":"No."})
        self.assertFalse(result["passed"])

    def test_false_abstention_is_detected(self):
        result = grade("invariant_under_valid_reprojection", False,
                       {"label":"invariant_under_valid_reprojection","abstain":True,"rationale":"Unsure."})
        self.assertTrue(result["false_abstention"])
        self.assertFalse(result["passed"])

    def test_missed_abstention_is_detected(self):
        result = grade("stale_evidence", True,
                       {"label":"stale_evidence","abstain":False,"rationale":"Looks fine."})
        self.assertTrue(result["missed_abstention"])
        self.assertFalse(result["passed"])

    def test_malformed_response_fails_safely(self):
        self.assertFalse(grade("stale_evidence", True, None)["passed"])

    def test_missing_rationale_fails(self):
        self.assertFalse(grade("stale_evidence", True, {"label":"stale_evidence","abstain":True})["passed"])

    def test_blank_rationale_fails(self):
        self.assertFalse(grade("stale_evidence", True,
                               {"label":"stale_evidence","abstain":True,"rationale":"   "})["passed"])

    def test_string_boolean_is_not_accepted(self):
        self.assertFalse(grade("stale_evidence", True,
                               {"label":"stale_evidence","abstain":"true","rationale":"Old."})["passed"])


if __name__ == "__main__":
    unittest.main()
