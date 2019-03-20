parity_drop_table = [57, 49, 41, 33, 25, 17, 9, 1,
                     58, 50, 42, 34, 26, 18, 10, 2,
                     59, 51, 43, 35, 27, 19, 11, 3,
                     60, 52, 44, 34, 63, 55, 47, 39,
                     31, 23, 15, 7, 62, 54, 46, 38,
                     30, 22, 14, 6, 61, 53, 45, 37,
                     29, 21, 13, 5, 28, 20, 12, 4]

comp_d_box = [14, 17, 11, 24, 1, 5, 3, 28,
              15, 6, 21, 10, 23, 19, 12, 4,
              26, 8, 16, 7, 27, 20, 13, 2,
              41, 52, 31, 37, 47, 55, 30, 40,
              51, 45, 33, 48, 44, 49, 39, 56,
              34, 53, 46, 42, 50, 36, 29, 32]


def parity_drop(k64: str) -> str:
    k56 = ''
    for i in range(56):
        idx = parity_drop_table[i] - 1
        k56 += k64[idx]
    return k56


def shift_left(s: str, nbits: int) -> str:
    result: str = s[nbits:] + s[:nbits - 1]
    return result


def comp_d(left: str, right: str) -> str:
    k56 = left + right
    k48 = ''
    for i in range(48):
        idx = comp_d_box[i] - 1
        k48 += k56[idx]
    return k48


def key_gen(k64: str):
    k_stream = []

    k56 = parity_drop(k64)
    for i in range(15):
        left = k56[:28]
        right = k56[28:]
        if i == 0 or i == 1 or i == 8 or i == 15:
            left = shift_left(left, 1)
            right = shift_left(right, 1)
        else:
            left = shift_left(left, 2)
            right = shift_left(right, 2)
        k = comp_d(left, right)
        k_stream.append(k)
    return k_stream


class Key:
    def __init__(self, init_key):
        self.__k64 = init_key
        self.key_stream = key_gen(self.__k64)
        return
