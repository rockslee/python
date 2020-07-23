import unittest
from function.function import get_formatted
class NamesTestCase(unittest.TestCase):
    """测试"""
    def test_first_last_name(self):
        """能够正确地处理Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted("janis","joplin")
        self.assertEqual(formatted_name,"Janis Joplin")
unittest.main()