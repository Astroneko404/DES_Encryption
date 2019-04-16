from Key import Key
from Table import ex_d_box
from Table import final_permutation
from Table import initial_permutation
from Table import straight_perm_table
from Table import s_box
import textwrap
from multiprocessing.pool import Pool


# s1 and s2 are binary strings with same length
def xor(s1, s2):
    result = ''
    for i in range(len(s1)):
        c1 = int(s1[i])
        c2 = int(s2[i])
        r = int(c1 != c2)
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
    str_list = textwrap.wrap(s48, 6)
    for i in range(8):
        s = str_list[i]
        row = int(s[0] + s[5], 2)
        col = int(s[1:5], 2)
        box = s_box[i]
        sub = bin(box[row][col])[2:].zfill(4)
        # print(s, row, col, sub)
        s32 += sub

    # Permutation
    result = ''
    for i in range(32):
        idx = straight_perm_table[i] - 1
        result += s32[idx]
    return result


# The initial key and text should be both 64-bit
class DES:
    def __init__(self, key64, input_str):
        if len(key64) != 64:
            raise Exception('The length of key should be 64')

        # Get the key stream
        self.key = Key(key64)

        # Preprocess the input string
        # Padding at the end of string
        r = len(input_str) % 64
        if r != 0:
            for i in range(64 - r):
                input_str += '0'
        self.input_list = textwrap.wrap(input_str, 64)

    def encryption(self, s64):
        if len(s64) != 64:
            raise Exception('The length of input string should be 64')
        key_stream = self.key.key_stream

        # Initial permutation
        s_init = ''
        for i in range(64):
            idx = initial_permutation[i] - 1
            s_init += s64[idx]
        left = s_init[:32]
        right = s_init[32:]
        # print(left, right)

        # 16 rounds
        for i in range(16):
            tmp = feistel(right, key_stream[i])
            left = xor(left, tmp)
            if i != 15:
                left, right = right, left
            # print('Round idx = ' + str(i))
            # print('Left: ' + str(left) + '; ' + 'Right: ' + str(right) + '\n')
        s_fin_tmp = left + right

        # Final permutation
        s_fin = ''
        for i in range(64):
            idx = final_permutation[i] - 1
            s_fin += s_fin_tmp[idx]

        return s_fin

    def decryption(self, s64):
        if len(s64) != 64:
            raise Exception('The length of input string should be 64')
        key_stream = self.key.key_stream

        # Initial permutation
        s_init = ''
        for i in range(64):
            idx = initial_permutation[i] - 1
            s_init += s64[idx]
        left = s_init[:32]
        right = s_init[32:]
        # print(left, right)

        # 16 rounds with reversed keys
        for i in range(16):
            tmp = feistel(right, key_stream[15-i])
            left = xor(left, tmp)
            if i != 15:
                left, right = right, left
            # print('Round idx = ' + str(i))
            # print('Left: ' + str(left) + '; ' + 'Right: ' + str(right) + '\n')
        s_fin_tmp = left + right

        # Final permutation
        s_fin = ''
        for i in range(64):
            idx = final_permutation[i] - 1
            s_fin += s_fin_tmp[idx]

        return s_fin

    def ecb_encryption(self):
        result = ''
        for s in self.input_list:
            cipher = self.encryption(s)
            result += cipher
        return result

    def ecb_encryption_mp(self):
        result = ''
        pool = Pool(processes=len(self.input_list))
        cipher = [pool.apply(self.encryption, args=(s,)) for s in self.input_list]
        for c in cipher:
            result += c
        return result

    def ecb_decryption(self):
        result = ''
        for s in self.input_list:
            plain = self.decryption(s)
            result += plain
        return result

    def cbc_encryption(self, iv):
        if len(iv) != 64:
            raise Exception('The length of IV should be 64')
        result_list = []
        result = ''

        for i in range(len(self.input_list)):
            text_block = self.input_list[i]
            if i == 0:
                v = iv
            else:
                v = result_list[i-1]
            in_text = xor(text_block, v)
            out_text = self.encryption(in_text)

            result_list.append(out_text)
            result += out_text
        return result

    def cbc_decryption(self, iv):
        if len(iv) != 64:
            raise Exception('The length of IV should be 64')
        result = ''

        for i in range(len(self.input_list)):
            text_block = self.input_list[i]
            if i == 0:
                v = iv
            else:
                v = self.input_list[i-1]
            in_text = self.decryption(text_block)
            out_text = xor(in_text, v)

            result += out_text
        return result