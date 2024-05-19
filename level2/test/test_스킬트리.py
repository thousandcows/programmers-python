import unittest

from level2.스킬트리 import SkillTree


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        skill = "CBD"
        skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
        expected = 2
        self.assertEqual(
            expected, SkillTree.solution(skill, skill_trees)
        )  # add assertion here


if __name__ == "__main__":
    unittest.main()
