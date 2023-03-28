import unittest
import bmi

class Testbmi(unittest.TestCase):

    def test_findBMI_76_265(self) -> None:
        self.assertAlmostEqual(bmi.findBMI(76, 265), 32.25328947368421)

    def test_findBMI_70_155(self) -> None:
        self.assertAlmostEqual(bmi.findBMI(70, 155), 22.237755102040815)

    def test_findBMI_71_135(self) -> None:
        self.assertAlmostEqual(bmi.findBMI(71, 135), 18.826621702043244)

    def test_classifyBMI_underweight_mid(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(14),'underweight')

    def test_classifyBMI_underweight_top(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(18), 'underweight')

    def test_classifyBMI_normal_bottom(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(19), 'normal')

    def test_classifyBMI_normal_mid(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(22), 'normal')

    def test_classifyBMI_normal_top(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(24), 'normal')

    def test_classifyBMI_over_bottom(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(25), 'overweight')

    def test_classifyBMI_over_mid(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(27), 'overweight')

    def test_classifyBMI_over_top(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(29), 'overweight')

    def test_classifyBMI_obese_bottom(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(30), 'obese')

    def test_classifyBMI_ovese_mid(self) -> None:
        self.assertAlmostEqual(bmi.classifyBMI(33), 'obese')



if __name__ == '__main__':
    unittest.main()