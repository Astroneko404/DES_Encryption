from Convert import bin_2_hex, hex_2_str, hex_2_bin, print_bin, str_2_hex
from Des import DES

###################################
# Test 1
# Key and string are taken from HW4
init_key_bin_1 = bin(int('0123456789abcdef', 16))[2:].zfill(64)
init_str_1 = bin(int('0123456789abcdef', 16))[2:].zfill(64)
des_1 = DES(init_key_bin_1, init_str_1)
text_1 = bin_2_hex(des_1.encryption(des_1.input_list[0]))
print_bin(text_1)
print()

###################################
# Test 2
# Key and string are taken from http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
init_key_bin_2 = hex_2_bin('133457799BBCDFF1')
init_str_2 = hex_2_bin('0123456789ABCDEF')
des_2 = DES(init_key_bin_2, init_str_2)
text_2 = des_2.encryption(des_2.input_list[0])
print_bin(bin_2_hex(text_2))
print()

###################################
# Test 3
# Decryption of Test 2
init_key_bin_3 = hex_2_bin('133457799BBCDFF1')
init_str_3 = hex_2_bin('85e813540f0ab405')
des_3 = DES(init_key_bin_3, init_str_3)
text_3 = des_3.decryption(des_3.input_list[0])
print_bin(bin_2_hex(text_3))
print()

###################################
# Test 4
# ECB mode encryption
init_key_bin_4 = hex_2_bin('133457799BBCDFF1')
init_str_4 = hex_2_bin('0123456789ABCDEF0123456789ABCD')
des_4 = DES(init_key_bin_4, init_str_4)
text_4 = des_4.ecb_encryption()
print_bin(bin_2_hex(text_4))
print()

###################################
# Test 5
# ECB mode decryption
init_key_bin_5 = hex_2_bin('133457799BBCDFF1')
init_str_5 = hex_2_bin('85e813540f0ab405ecc1a6e177f393b1')
des_5 = DES(init_key_bin_5, init_str_5)
text_5 = des_5.ecb_decryption()
print_bin(bin_2_hex(text_5))
print()

###################################
# Test 6
# CBC mode encryption
init_key_bin_6 = hex_2_bin('133457799BBCDFF1')
init_str_6 = hex_2_bin('0123456789ABCDEF0123456789ABCD')
iv_6 = hex_2_bin('AB125AFC396214F3')
des_6 = DES(init_key_bin_6, init_str_6)
text_6 = des_6.cbc_encryption(iv_6)
print_bin(bin_2_hex(text_6))
print()

###################################
# Test 7
# CBC mode decryption
init_key_bin_7 = hex_2_bin('133457799BBCDFF1')
init_str_7 = hex_2_bin('50bd35a7cab04b71eb1dbc5c70b27c59')
iv_7 = hex_2_bin('AB125AFC396214F3')
des_7 = DES(init_key_bin_7, init_str_7)
text_7 = des_7.cbc_decryption(iv_7)
print_bin(bin_2_hex(text_7))
print()

###################################
# Test 8
# Text encryption
init_key_bin_8 = hex_2_bin('133457799BBCDFF1')
init_str_8 = hex_2_bin(str_2_hex('Hello World!'))
iv_8 = hex_2_bin('AB125AFC396214F3')
des_8 = DES(init_key_bin_8, init_str_8)
text_8 = des_8.cbc_encryption(iv_8)
print_bin(bin_2_hex(text_8))
print()

###################################
# Test 9
# Text decryption
init_key_bin_9 = hex_2_bin('133457799BBCDFF1')
init_str_9 = hex_2_bin('440f3378b91694203b928223b00cfe48')
iv_9 = hex_2_bin('AB125AFC396214F3')
des_9 = DES(init_key_bin_9, init_str_9)
text_9 = hex_2_str(bin_2_hex(des_9.cbc_decryption(iv_9)))
print(text_9)

