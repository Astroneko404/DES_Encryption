from Des import DES


# Key_list is a list with 3 keys of 64-bit
# Input_str should be also 64-bit
class TriDES:
    def __init__(self, key_list, input_str):
        self.key_list = key_list
        self.des1 = DES(self.key_list[0], input_str)

    def encryption(self):
        out1 = self.des1.ecb_encryption()
        des2 = DES(self.key_list[1], out1)
        out2 = des2.ecb_encryption()
        des3 = DES(self.key_list[2], out2)
        result = des3.ecb_encryption()
        return result