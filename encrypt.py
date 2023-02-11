import random
def generate_shifter():
    shifter = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    random.shuffle(shifter)
    return shifter
def encrypt(data,shift_times):
    data = data.hex().upper()
    iterate = 0
    shifter = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    shifters = []
    for i in range(shift_times):
        output = ""
        shift_list = generate_shifter()
        shifters.append(shift_list)
        for d in data:
            index = shifter.index(d)
            output = output + shift_list[index]
        data = output
    return bytes(bytearray.fromhex(data)),shifters
