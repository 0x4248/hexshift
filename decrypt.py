def decrypt(data,shifters):
    data = data.hex().upper()
    iterate = 0
    shifter = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for s in reversed(shifters):
        output = ""
        for d in data:
            index = s.index(d)

            output = output + shifter[index]
        data = output
    return bytes(bytearray.fromhex(data))