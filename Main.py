from Des import DES
from Key import Key


def bin_2_hex(bin_str):
    return hex(int(bin_str, 2))[2:]


# Print binary string in format
def print_bin(s):
    for i in range(0, len(s), 4):
        print(s[i]+s[i+1]+s[i+2]+s[i+3], end=' ')
    return


###################################
# Test 1
# Key and string are taken from HW4
# init_key_bin = bin(int('0123456789abcdef', 16))[2:].zfill(64)
# init_str = bin(int('0123456789abcdef', 16))[2:].zfill(64)
# des = DES(init_key_bin, init_str)
# cipher_text = bin_2_hex(des.encryption())
# print_bin(cipher_text)

###################################
# Test 2
# Key and string are taken from http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
init_key_bin = '0001001100110100010101110111100110011011101111001101111111110001'
init_str = '0000000100100011010001010110011110001001101010111100110111101111'
des = DES(init_key_bin, init_str)
cipher_text = des.encryption()
print_bin(bin_2_hex(cipher_text))
