def communication_module(packet):
    header = packet[0:4]
    d1 = int(packet[8:12])
    d2 = int(packet[12: 16])
    res = {'0F12': d1 + d2, 'B7A2': d1 - d2, 'C3D9': d1 * d2}
    instruct = res[packet[4:8]]
    if instruct > 9999:
        instruct = str('9999')
    elif instruct < 0:
        instruct = str('0000')
    else:
        instruct = str(instruct)
    return header + 'FFFF' + (4 - len(instruct)) * '0' + instruct + '0000' + packet[-4:]
