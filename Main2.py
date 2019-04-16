from Convert import bin_2_hex, hex_2_str, hex_2_bin, print_bin, str_2_hex
from Des import DES
from datetime import datetime

###################################
# Test 10
# ECB and CBC runtime test
# Text is from Wikipedia
if __name__ == '__main__':
    init_key_bin = hex_2_bin('133457799BBCDFF1')
    in_str = "Courbet was the lead ship of her class of four dreadnought battleships, the first ones built for the " \
             "French Navy. In World War I, after helping to sink the Austro-Hungarian protected cruiser SMS Zenta in " \
             "August 1914, she provided cover for the Otranto Barrage that blockaded the Austro-Hungarian Navy in the " \
             "Adriatic Sea, and often served as a flagship. Although upgraded several times before World War II, " \
             "by the 1930s she was no longer considered to be a first-line battleship and spent much of that decade " \
             "as a gunnery training ship. A few weeks after the German invasion of France on 10 May 1940, Courbet was " \
             "hastily reactivated. She supported Allied troops in the defence of Cherbourg during mid-June. As part " \
             "of Operation Catapult, she was seized in Portsmouth by British forces on 3 July and was turned over to " \
             "the Free French a week later. She was used as a stationary anti-aircraft battery and as an " \
             "accommodation ship there. "
    init_str = hex_2_bin(str_2_hex(in_str))
    des = DES(init_key_bin, init_str)

    total_run = 20

    print("Original ECB mode encryption runtime test start")
    start_time = datetime.now()
    for i in range(total_run):
        text = des.ecb_encryption()
        # if i % 5 == 0 and i != 0:
        #     print('Finished', i, 'runs')
    finish_time = datetime.now() - start_time
    print(total_run, 'times of original ECB mode encryption finished with', finish_time)

    print('ECB mode encryption with multiprocessing runtime test start')
    start_time = datetime.now()
    for i in range(total_run):
        text = des.ecb_encryption_mp()
        # if i % 5 == 0 and i != 0:
        #     print('Finished', i, 'runs')
    finish_time = datetime.now() - start_time
    print(total_run, 'times of ECB mode encryption with multiprocessing finished with', finish_time)

    print("Original CBC mode encryption runtime test start")
    iv = hex_2_bin('AB125AFC396214F3')
    start_time = datetime.now()
    for i in range(total_run):
        text = des.cbc_encryption(iv)
        # if i % 5 == 0 and i != 0:
        #     print('Finished', i, 'runs')
    finish_time = datetime.now() - start_time
    print(total_run, 'times of original CBC mode encryption finished with', finish_time)