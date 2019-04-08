from Des import DES
from Key import Key

# The key is taken from HW4
init_key_hex = '0123456789abcdef'
init_key_bin = bin(int(init_key_hex, 16))[2:].zfill(64)
# print('Initial 64-bit key is:', init_key_bin)
# key = Key(init_key_bin)
# key.print_key(0)

init_str = bin(int('0123456789abcdef', 16))[2:].zfill(64)
des = DES(init_key_bin, init_str)
des.encryption()