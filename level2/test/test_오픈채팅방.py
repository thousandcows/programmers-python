import unittest

from level2.오픈채팅방 import OpenChat


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
        expected = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
        self.assertEqual(expected, OpenChat.solution(record))  # add assertion here


if __name__ == '__main__':
    unittest.main()
