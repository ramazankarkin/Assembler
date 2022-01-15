"""
150119512 - Ramazan KARKIN
150119842 - Ahmet Kerem AKPINAR
150115065 - Abdülkadir ASLAN
150118029 - Rumeysa ULUSOY
"""
path = "input.txt"
# reading file
with open(path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
inputFileArr = []
# getting parsed string from input file
for i in range(0, len(lines)):
    split = lines[i].split(" ")
    op = split[0]
    left_op = split[1].split(",")
    inputFileArr.append([op] + left_op)
# print(inputFileArr)
newlist = []
# remove 'R' from register name
for i in range(0, len(inputFileArr)):
    newlist.append([x.split('R')[1] if 'R' in x else x for x in inputFileArr[i][1:]])


# print(newlist)
# convert decimal to binary form according to ISA
def binary_con(n):
    binary = ""
    for j in range(0, len(newlist[n])):
        if int(newlist[n][j]) >= 0:
            binary = binary + str(f'{int(newlist[n][j]):04b}')
        else:
            binary = binary + (bin((1 << 6) + int(newlist[n][j]))[2:])

    if inputFileArr[n][0] in ["ANDI", "ADDI", "ORI", "XORI"]:
        if int(newlist[n][2]) >= 0:
            while 14 - len(binary) > 0:
                binary = binary[:8] + "0" + binary[8:]
        else:
            while 14 - len(binary) > 0:
                binary = binary[:8] + "1" + binary[8:]

    if inputFileArr[n][0] in ["LD", "ST"]:
        if int(newlist[n][1]) >= 0:
            while 14 - len(binary) > 0:
                binary = binary[:4] + "0" + binary[4:]
        else:
            while 14 - len(binary) > 0:
                binary = binary[:4] + "1" + binary[4:]

    if inputFileArr[n][0] in ["JUMP"]:
        if int(newlist[n][0]) >= 0:
            while 14 - len(binary) > 0:
                binary = "0" + binary
        else:
            while 14 - len(binary) > 0:
                binary = "1" + binary

    return binary


# convert decimal to binary form according to ISA for these registers ["BEQ", "BGT", "BLT", "BGE", "BLE"]

def binary_con2(n):
    binary2 = ""
    for j in range(0, len(newlist[n])):
        if j < 2:
            if int(newlist[n][j]) >= 0:
                binary2 = binary2 + str(f'{int(newlist[n][j]):04b}')
            else:
                binary2 = binary2 + (bin((1 << 6) + int(newlist[n][j]))[2:])
        elif j == 2:
            if int(newlist[n][j]) >= 0:
                binary2 = binary2 + str(f'{int(newlist[n][j]):06b}')
            else:
                binary2 = binary2 + (bin((1 << 6) + int(newlist[n][j]))[2:])
        else:
            print("Please enter 3 input for branch instruction")

    return binary2


# convert binary form to hexadecimal
def bin_hex(binary):
    return f'{int(binary, 2):0{(len(binary) + 3) // 4}x}'


opcode_list = [["AND", "0000"],
               ["OR", "0001"],
               ["ADD", "0010"],
               ["XOR", "0011"],
               ["ANDI", "0100"],
               ["ORI", "0101"],
               ["ADDI", "0110"],
               ["XORI", "0111"],
               ["LD", "1000"],
               ["ST", "1101"],
               ["JUMP", "1111"],
               ["BEQ", "1010"],
               ["BGT", "1001"],
               ["BLT", "1100"],
               ["BGE", "1011"],
               ["BLE", "1110"]]
print("v2.0 raw")
# print hexadecimal form of input.txt file according to our ISA structure
for i in range(0, len(inputFileArr)):
    if inputFileArr[i][0] == opcode_list[0][0]:  # AND
        binary = opcode_list[0][1] + binary_con(i)[:4] + "00" + binary_con(i)[4:]
        # print(inputFileArr[i])
        # print(binary)
        print(bin_hex(binary))
    elif inputFileArr[i][0] == opcode_list[1][0]:  # OR
        binary = opcode_list[1][1] + binary_con(i)[:4] + "00" + binary_con(i)[4:]
        print(bin_hex(binary))
    elif inputFileArr[i][0] == opcode_list[2][0]:  # ADD
        binary = opcode_list[2][1] + binary_con(i)[:4] + "00" + binary_con(i)[4:]
        print(bin_hex(binary))
    elif inputFileArr[i][0] == opcode_list[3][0]:  # XOR
        binary = opcode_list[3][1] + binary_con(i)[:4] + "00" + binary_con(i)[4:]
        print(bin_hex(binary))
    elif inputFileArr[i][0] == opcode_list[4][0]:  # ANDI
        binary = opcode_list[4][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[5][0]:  # ORI
        binary = opcode_list[5][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[6][0]:  # ADDI
        binary = opcode_list[6][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[7][0]:  # XORI
        binary = opcode_list[7][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[8][0]:  # LD
        binary = opcode_list[8][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[9][0]:  # ST
        binary = opcode_list[9][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[10][0]:  # JUMP
        binary = opcode_list[10][1] + binary_con(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[11][0]:  # BEQ
        binary = opcode_list[11][1] + binary_con2(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[12][0]:  # BGT
        binary = opcode_list[12][1] + binary_con2(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[13][0]:  # BLT
        binary = opcode_list[13][1] + binary_con2(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[14][0]:  # BGE
        binary = opcode_list[14][1] + binary_con2(i)
        print(bin_hex(binary))

    elif inputFileArr[i][0] == opcode_list[15][0]:  # BLE
        binary = opcode_list[15][1] + binary_con2(i)
        print(bin_hex(binary))

    else:
        print("Please enter correct input.")
