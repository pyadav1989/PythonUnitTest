import unittest
import HtmlTestRunner
import SampleCalc as smple

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tesrDownClass")

    def setUp(self) -> None:
        print("setUP")
        self.cal1 = smple.Calc()

    def tearDown(self) -> None:
        print("tesrDown")

    def test_add(self):
        self.assertEqual(30, self.cal1.add(10, 20))

    def test_sub(self):
        self.assertEqual(10, self.cal1.sub(20, 10))

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./Reports/",report_title="TestReport",descriptions="Execution Report"))