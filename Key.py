from Table import comp_d_box
from Table import parity_drop_table


def parity_drop(k64: str) -> str:
    k56 = ''
    for i in range(56):
        idx = parity_drop_table[i] - 1
        k56 += k64[idx]
    return k56


def shift_left(s: str, nbits: int) -> str:
    result: str = s[nbits:] + s[:nbits]
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
    # print('k56:', k56, 'with length', len(k56))

    for i in range(16):
        left = k56[:28]
        right = k56[28:]
        # print(left, right)
        if i == 0 or i == 1 or i == 8 or i == 15:
            left = shift_left(left, 1)
            right = shift_left(right, 1)
        else:
            left = shift_left(left, 2)
            right = shift_left(right, 2)
        # print(left, right)
        k = comp_d(left, right)
        k56 = left + right
        k_stream.append(k)
    return k_stream


class Key:
    def __init__(self, init_key):
        self.__k64 = init_key
        self.key_stream = key_gen(self.__k64)
        # for i in range(16):
        #     self.print_key(i)
        return

    def print_key(self, idx):
        print('Key idx = ' + str(idx+1))
        k = self.key_stream[idx]
        for i in range(0, len(k), 4):
            bit = k[i] + k[i+1] + k[i+2] + k[i+3]
            print(bit, end=' ')
        print()
        return