from unittest.case import TestCase
from 修trs.修理 import 修理


class 修理試驗(TestCase):
    def test_header無改(self):
        原本 = [
            '<?xml version="1.0" encoding="UTF-8"?>'
        ]
        害去 = [
            '<?xml version="1.0" encoding="UTF-8"?>'
        ]
        self.assertEqual(
            修理().取代(原本, 害去),
            原本,
        )

    def test_speaker無改(self):
        原本 = [
            '<Speaker id="spk1" name="麗香同事" check="no" dialect="native" accent="" scope="local"/>'
        ]
        害去 = [
            '<Speaker id="spk1" name="????" check="no" dialect="native" accent="" scope="local"/>'
        ]
        self.assertEqual(
            修理().取代(原本, 害去),
            原本,
        )

    def test_版本更新(self):
        原本 = [
            '<Trans scribe="ZiiYu" audio_filename="csgr04" version="14" version_date="130626">'
        ]
        害去 = [
            '<Trans scribe="ZiiYu" audio_filename="csgr04" version="16" version_date="170924">'
        ]
        self.assertEqual(
            修理().取代(原本, 害去),
            害去,
        )

    def test_字幕(self):
        原本 = [
            'ah1 vor5 lan1 gin2-a1 kah1-za1 guainn2-diam3 hior4-kun3 不然我們今天提早打烊休息吧//'
        ]
        害去 = [
            'ah1 vor5 lan1 gin2-a1 kah1-za1 guainn2-diam3 hior4-kun3 ?????????????//'
        ]
        self.assertEqual(
            修理().取代(原本, 害去),
            原本,
        )

    def test_連續三逝(self):
        原本 = '''<Speakers>
<Speaker id="spk1" name="麗香同事" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="麗香" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk3" name="三哥" check="no" dialect="native" accent="" scope="local"/>
'''.split('\n')
        害去 = '''<Speakers>
<Speaker id="spk1" name="????" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="??" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk3" name="??" check="no" dialect="native" accent="" scope="local"/>
'''.split('\n')
        self.assertEqual(
            修理().取代(原本, 害去),
            原本,
        )

    def test_改先後(self):
        原本 = '''<Speakers>
<Speaker id="spk3" name="三哥" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk1" name="麗香同事" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="麗香" check="no" dialect="native" accent="" scope="local"/>
'''.split('\n')
        害去 = '''<Speakers>
<Speaker id="spk1" name="????" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="??" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk3" name="??" check="no" dialect="native" accent="" scope="local"/>
'''.split('\n')
        self.assertEqual(
            修理().取代(原本, 害去),
            '''<Speakers>
<Speaker id="spk1" name="麗香同事" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="麗香" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk3" name="三哥" check="no" dialect="native" accent="" scope="local"/>
'''.split('\n'),
        )
