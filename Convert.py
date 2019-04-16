# Convert a binary string to a hex string
def bin_2_hex(bin_str):
    return hex(int(bin_str, 2))[2:]


# Convert a hex string to a bin string
def hex_2_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str)*4)


def str_2_hex(s):
    result = ''
    for c in s:
        result += hex(ord(c))[2:]
    return result


def hex_2_str(s):
    result = ''
    for i in range(0, len(s), 2):
        i = s[i] + s[i+1]
        if i != '00':
            result += chr(int(i, 16))
    return result.strip()


# Print binary string in format
def print_bin(s):
    r = len(s) % 4
    if r != 0:
        for i in range(4-r):
            s = '0' + s
    for i in range(0, len(s), 4):
        print(s[i]+s[i+1]+s[i+2]+s[i+3], end=' ')
    return