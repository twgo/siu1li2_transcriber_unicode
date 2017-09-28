import re


class 修理:
    def __init__(self):
        pass

    def 取代(self, 原本, 害去):
        修好 = []
        開始所在 = 0
        for 一逝 in 害去:
            這馬所在 = 開始所在
            比較物件 = re.compile(一逝.rstrip().replace('?', r'.') + r'\Z')
            for 這馬所在 in range(開始所在, len(原本)):
                if 比較物件.match(
                    原本[這馬所在].rstrip()
                ):
                    修好.append(原本[這馬所在])
                    開始所在 = 這馬所在
                    break
            else:
                for 這馬所在 in range(開始所在):
                    if 比較物件.match(
                        原本[這馬所在].rstrip()
                    ):
                        修好.append(原本[這馬所在])
                        開始所在 = 這馬所在
                        break
                else:
                    修好.append(一逝)
        return 修好
