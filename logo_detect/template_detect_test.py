import os
import unittest

from logo_detect.settings import TEST_CASE_BASE
from logo_detect.template_detect import logo_detector_map
from logo_detect.util import test_case

test_case_list = []
for name in os.listdir(TEST_CASE_BASE):
    test_case_list.append((name, test_case(name)))


class TecentTest(unittest.TestCase):
    def test_tecent(self):
        detector = logo_detector_map['tencent_right']
        for name, img in test_case_list:
            result = detector.detect_right(img)
            print name
            if "tecent" in name:
                self.assertIsNotNone(result,name)
            else:
                self.assertIsNone(result,name)

    def test_xigua(self):
        detector = logo_detector_map['xigua_right']
        for name, img in test_case_list:
            result = detector.detect_right(img)
            if "xigua" in name and "left" not in name:
                print name
                self.assertIsNotNone(result,name)
            else:
                self.assertIsNone(result,name)

    def test_xigua_left(self):
        detector = logo_detector_map['xigua_left']
        for name, img in test_case_list:
            result = detector.detect_left(img)
            if "xigua" in name and "left" in name:
                self.assertIsNotNone(result,name)
            else:
                self.assertIsNone(result,name)


if __name__ == '__main__':
    unittest.main()
