from Key import Key
from Table import ex_d_box
from Table import final_permutation
from Table import initial_permutation
from Table import straight_perm_table
from Table import s_box
import textwrap


# s1 and s2 are binary strings with same length
def xor(s1, s2):
    result = ''
    for i in range(len(s1)):
        c1 = int(s1[i])
        c2 = int(s2[i])
        r = (c1 != c2)
        result += str(r)
    return result


def feistel(s32, key):
    s48 = ''

    # Bit expansion
    for i in range(48):
        idx = ex_d_box[i] - 1
        s48 += s32[idx]

    # XOR
    s48 = xor(s48, key)

    # S-boxes
    s32 = ''
    str_list = textwrap.wrap(s48, 8)
    for i in range(7):
        s = str_list[i]
        row = int(s[0] + s[5], 2)
        col = int(s[1:5], 2)
        box = s_box[i]
        sub = bin(box[row][col])[2:].zfill(4)
        s32 += sub

    # Permutation
    result = ''
    for i in range(32):
        idx = straight_perm_table[i] - 1
        result += s32[idx]
    return result


# The initial key and text should be both 64-bit
class DES:
    def __init__(self, key64, s64):
        self.key = Key(key64)
        self.s64 = s64

    def encryption(self):
        key_stream = self.key.key_stream

        # Initial permutation
        s_init = ''
        for i in range(64):
            idx = initial_permutation[i]
            s_init += self.s64[idx]
        left = s_init[:32]
        right = s_init[32:]

        return