from gtts import gTTS
from os import urandom
from sys import byteorder


def ten_num():
    num_l = []
    for i in range(1, 5):
        n_bytes = urandom(8)
        num = int.from_bytes(n_bytes, byteorder)
        num_l.insert(0, num)
    return num_l

list_nums = ten_num()
list_nums = [str(x) for x in list_nums]
list_nums = " ".join(list_nums)

tts = gTTS(list_nums, slow=True)
tts.save("god.mp3")
