import re


class 修理:
    def __init__(self):
        pass

    def 取代(self, 原本資料, 害去):
        原本 = self._清掉換逝(原本資料)
        修好 = []
        開始所在 = 0
        for 一逝 in self._清掉換逝(害去):
            這馬所在 = 開始所在
            for 這馬所在 in range(開始所在, len(原本)):
                if re.match(
                    一逝.replace('?', r'.') + r'\Z',
                    原本[這馬所在]
                ):
                    修好.append(原本[這馬所在])
                    開始所在 = 這馬所在
                    break
            else:
                for 這馬所在 in range(開始所在):
                    if re.match(
                        一逝.replace('?', r'.') + r'\Z',
                        原本[這馬所在]
                    ):
                        修好.append(原本[這馬所在])
                        開始所在 = 這馬所在
                        break
                else:
                    修好.append(一逝)
        return 修好

    def _清掉換逝(self, 資料):
        return [一逝.rstrip() for 一逝 in 資料]
