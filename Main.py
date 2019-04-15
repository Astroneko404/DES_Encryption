from Des import DES
from Key import Key


# Convert a binary string to a hex string
def bin_2_hex(bin_str):
    return hex(int(bin_str, 2))[2:]


# Convert a hex string to a bin string
def hex_2_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str)*4)


# Print binary string in format
def print_bin(s):
    r = len(s) % 4
    if r != 0:
        for i in range(4-r):
            s = '0' + s
    for i in range(0, len(s), 4):
        print(s[i]+s[i+1]+s[i+2]+s[i+3], end=' ')
    return


###################################
# Test 1
# Key and string are taken from HW4
init_key_bin_1 = bin(int('0123456789abcdef', 16))[2:].zfill(64)
init_str_1 = bin(int('0123456789abcdef', 16))[2:].zfill(64)
des_1 = DES(init_key_bin_1, init_str_1)
cipher_text_1 = bin_2_hex(des_1.encryption())
print_bin(cipher_text_1)
print()

###################################
# Test 2
# Key and string are taken from http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
init_key_bin_2 = hex_2_bin('133457799BBCDFF1')
init_str_2 = hex_2_bin('0123456789ABCDEF')
des = DES(init_key_bin_2, init_str_2)
cipher_text_2 = des.encryption()
print_bin(bin_2_hex(cipher_text_2))
print()

###################################
# Test 3
# Decryption of Test 2
init_key_bin_3 = hex_2_bin('133457799BBCDFF1')
init_str_3 = hex_2_bin('85e813540f0ab405')
des = DES(init_key_bin_3, init_str_3)
cipher_text_3 = des.decryption()
print_bin(bin_2_hex(cipher_text_3))