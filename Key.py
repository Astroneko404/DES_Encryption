parity_drop_table = [57, 49, 41, 33, 25, 17, 9, 1,
                     58, 50, 42, 34, 26, 18, 10, 2,
                     59, 51, 43, 35, 27, 19, 11, 3,
                     60, 52, 44, 34, 63, 55, 47, 39,
                     31, 23, 15, 7, 62, 54, 46, 38,
                     30, 22, 14, 6, 61, 53, 45, 37,
                     29, 21, 13, 5, 28, 20, 12, 4]


def parity_drop(k64: str) -> str:
    k56 = ''
    for i in range(56):
        idx = parity_drop_table[i] - 1
        k56 += k64[idx]
    return k56


def shift_left(s: str, nbits: int) -> str:
    result: str = s[nbits:] + s[:nbits-1]
    return result


class Key:
    def __init__(self, init_key):
        self.key_stream = []
        self.__k64 = init_key
        return
    
    