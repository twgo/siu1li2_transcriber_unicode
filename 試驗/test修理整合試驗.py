from os.path import abspath, join, dirname
from unittest.case import TestCase
from 修trs.修理 import 修理


class 修理試驗(TestCase):
    maxDiff = None

    def setUp(self):
        資料夾 = join(dirname(abspath(__file__)), '..', 'trs')
        self.原本 = join(資料夾, 'csgr04-zy-20130418-0616-0625.trs')
        self.害去 = join(資料夾, 'csgr04-new.trs')
        self.修好 = join(資料夾, 'csgr04-new-fixed.trs')

    def test_csgr04頭前100逝(self):
        with open(self.原本) as 原本:
            with open(self.害去) as 害去:
                with open(self.修好) as 修好:
                    self.assertEqual(
                        修理().取代(原本.readlines(), 害去.readlines())[:100],
                        修理()._清掉換逝(修好.readlines())[:100],
                    )
