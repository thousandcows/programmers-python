import unittest

from level2.파일명정렬 import SortFileName


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        files =["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
        expected =["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
        self.assertEqual(expected, SortFileName.solution(files))  # add assertion here

    def test_case_two(self):
        files =["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
        expected =["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
        self.assertEqual(expected, SortFileName.solution(files))

if __name__ == '__main__':
    unittest.main()
