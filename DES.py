from bitstring import BitArray

# Lists for DES Encryption Process.

# Initial Permutation Phase List
Book_IP_List = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]
# Programmatic List Conversion
IP_List = [x-1 for x in Book_IP_List]

# Expansion Phase List
Book_E_List = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
E_List = [x-1 for x in Book_E_List]

# Substitution Phase List
S_Box_list = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2
[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],
# Box-3
[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],
# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],
# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6
[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8
[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]
]

# Decimal to 4 bit Binary string conversion for S_Boxes.
Dec_2_Bin_string = {
    0: '0000',
    1: '0001',
    2: '0010',
    3: '0011',
    4: '0100',
    5: '0101',
    6: '0110',
    7: '0111',
    8: '1000',
    9: '1001',
    10: '1010',
    11: '1011',
    12: '1100',
    13: '1101',
    14: '1110',
    15: '1111'}

# Permutation Phase List
Book_P_List = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]
P_List = [x-1 for x in Book_P_List]

# Inverse Initial Permuation Phase List
Book_IIP_List = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25]
IIP_List = [x-1 for x in Book_IIP_List]

# Lists used in Key Generation Process.
# Permuted Choice 1 Phase List.
Book_PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4]
PC_1 = [x-1 for x in Book_PC_1]

# Shift Table for Left Circular Shift.
Shift_List = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Permuted Choice 2 Phase List.
Book_PC_2 = [
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32]
PC_2 = [x-1 for x in Book_PC_2]


# Utility Functions for use while Encryption and Decryption Processes.

# Bytes to Bits Conversion Function
def bytes2bit_seq(input_block):
  bits_list = [bin(int(b))[2:].zfill(8) for b in input_block]
  bit_seq = ''.join(bits_list)  
  return bit_seq

# Bits to Bytes Conversion Function.
def bin2byte_seq(input_block):
  input_block = '0b' + input_block
  temp = BitArray(input_block)
  byte_seq = temp.bytes
  return byte_seq

# A Common Permutation Function for all types of Permutations. The List is referenced using permutation_list.
def Permutation(bitstr, permutation_list):
  permuted_bit_seq = None
  IP_out = [bitstr[b] for b in permutation_list]
  permuted_bit_seq = ''.join(IP_out)
  return permuted_bit_seq

# Left Circular Shifts Implementation Function.
def shift(C_inp, D_inp, shift):
  return C_inp[shift:] + C_inp[:shift], D_inp[shift:] + D_inp[:shift]

# End of Utility Functions.

key_list = [] # A global Key List is created to update with the keys generated.

# DES Key Generation Function.
def des_generate_key_list(C_inp, D_inp, num_rounds):
  global key_list
  key_list = []
  for i in range(num_rounds):
    C_out, D_out = shift(C_inp, D_inp, Shift_List[i])
    key48 = Permutation(C_inp + D_inp, PC_2)
    key_list.append(key48)
    C_inp = C_out
    D_inp = D_out
  return key_list

# DES Ecnryption/Decryption Functions.

# Expansion Function.
def Expansion(inputbitstr32, E_List):
  outputbitstr48 = ''
  IP_out = [inputbitstr32[b] for b in E_List]
  outputbitstr48 = ''.join(IP_out)
  return outputbitstr48

# Bitwise XOR Function.
def Bitwise_XOR(bitstr1,bitstr2):
  xor_result = None
  xor_result = [str(int(x)^int(y)) for x,y in zip(bitstr1,bitstr2)]
  xor_result = ''.join(xor_result)
  return xor_result

# Substitution Utility Functions
def SBox_lookup(input6bitstr, S_Box_listindex):
  row = 0
  col = 0
  row = int(input6bitstr[:1]+input6bitstr[-1:],base=2)
  col = int(input6bitstr[1:5],base=2)
  S_Box_list_value = S_Box_list[S_Box_listindex][row][col]
  # Need to convert to 4 bits binary string    
  return Dec_2_Bin_string[S_Box_list_value]

def DES_substitution(inputbitstr48):
  SBox_input_list = [inputbitstr48[i:i+6] for i in range(0, len(inputbitstr48), 6)]
  SBox_output = []
  for idx in range(8):
    SBox_output.append(SBox_lookup(SBox_input_list[idx],idx))
  SBox_outbitstr32 = ''.join(SBox_output)
  return SBox_outbitstr32

# Main DES round function involving: Expansion, Key Mixing, Substitution, Permuation Function calls
def F_function(bitstr32, keybitstr48):
  outbitstr32 = ''
  outbitstr48 = Expansion(bitstr32, E_List)
  XOR_outbitstr48 = Bitwise_XOR(outbitstr48, keybitstr48)
  SBox_outbitstr32 = DES_substitution(XOR_outbitstr48)
  outbitstr32 = Permutation(SBox_outbitstr32, P_List)
  return outbitstr32

# DES Round phase (Fiestel mode implementation)
def DES_round(LE_inp32, RE_inp32, key48):
  LE_out32 = RE_inp32 
  F_out32 = F_function(RE_inp32, key48)
  RE_out32 = Bitwise_XOR(F_out32, LE_inp32)
  return LE_out32, RE_out32

# Main DES Encryption Function. Takes 64 bit plain text, 64 bit Key, and number of rounds as args.
def DES_enc(inputblock, num_rounds, inputkey64):
  cipherblock = ''
  # Initial Permutation
  inputblock = Permutation(inputblock, IP_List)
  # Left and right input blocks
  LE_inp32 = inputblock[:32]
  RE_inp32 = inputblock[32:]
  # -------------- KEYING ----------------------- #
  # Permutation choice 1 for key. Done only once
  inputkey64 = Permutation(inputkey64, PC_1)
  C_inp = inputkey64[:28]
  D_inp = inputkey64[28:]
  des_generate_key_list(C_inp, D_inp, num_rounds)
  # -------------- KEYING ----------------------- #
  
  # -------------- DES Rounds ----------------------- #
  for rnd in range(num_rounds):
    # Key Gen for rnd th round.
    key48 = key_list[rnd]
    # DES round function call for rnd th round.
    LE_out32, RE_out32 = DES_round(LE_inp32, RE_inp32, key48)
    # Setting up the DATA variables for rnd+1 th round.
    LE_inp32 = LE_out32
    RE_inp32 = RE_out32
  # -------------- DES Rounds ----------------------- #

  # -------------- After all DES Rounds ----------------- #
  # 32 Bit Swap
  cipher_bitseq64 = RE_inp32 + LE_inp32
  # Inverse Initial Permutation
  cipherblock = Permutation(cipher_bitseq64, IIP_List)
  return cipherblock

# Main DES Decryption Function. Takes 64 bit cipher text, 64 bit Key, and number of rounds as args.
def DES_dec(inputblock, num_rounds, inputkey64):
  plainblock = ''
  # Initial Permutation
  inputblock = Permutation(inputblock, IP_List)
  
  # -------------- KEYING ----------------------- #
  # Left and right input blocks
  LE_inp32 = inputblock[:32]
  RE_inp32 = inputblock[32:]
  # Permutation choice 1 for key. Done only once
  inputkey64 = Permutation(inputkey64, PC_1)
  C_inp = inputkey64[:28]
  D_inp = inputkey64[28:]
  des_generate_key_list(C_inp, D_inp, num_rounds)
  # -------------- KEYING ----------------------- #
  
  # -------------- DES Rounds ----------------------- #
  for rnd in range(num_rounds-1, -1, -1):
    # Key Gen for rnd th round.
    key48 = key_list[rnd]
    # DES round function call for rnd th round.
    LE_out32, RE_out32 = DES_round(LE_inp32, RE_inp32, key48)
    # Setting up the DATA variables for rnd+1 th round.
    LE_inp32 = LE_out32
    RE_inp32 = RE_out32
  # -------------- DES Rounds ----------------------- #

  # -------------- After all DES Rounds ----------------- #
  # 32 Bit Swap
  plain_bitseq64 = RE_inp32 + LE_inp32
  # Inverse Initial Permutation
  plainblock = Permutation(plain_bitseq64, IIP_List)
  return plainblock

# Utility Function which takes the plain text from a file as bytes and passes it to the DES_enc function.
def DES_enc_test(input_fname, inputkey64, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    if not isinstance(inputkey64, bytes):
      inputkey64 = bytes(inputkey64, 'utf-8')
    inputkey64 = bytes2bit_seq(inputkey64)
    cipherbyteseq = b''
    inp_bytes_array = [inpbyteseq[i:i+8] for i in range(0, len(inpbyteseq), 8)]
    # Adding spaces as padding in the last element
    if len(inp_bytes_array[-1])<8:
      inp_bytes_array[-1] = inp_bytes_array[-1]+ b' '*(8 - len(inp_bytes_array[-1]))
    for seq in inp_bytes_array:
      seq = bytes2bit_seq(seq)
      temp_cipher = DES_enc(seq, num_rounds, inputkey64)
      temp_cipher = bin2byte_seq(temp_cipher)
      cipherbyteseq += temp_cipher
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()

# Utility Function which takes the cipher text from a file as bytes and passes it to the DES_dec function.
def DES_dec_test(input_fname, inputkey64, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    if not isinstance(inputkey64, bytes):
      inputkey64 = bytes(inputkey64, 'utf-8')
    inputkey64 = bytes2bit_seq(inputkey64)
    plainbyteseq = b''
    # do the decryption rounds
    inp_bytes_array = [inpbyteseq[i:i+8] for i in range(0, len(inpbyteseq), 8)]
    for seq in inp_bytes_array:
      seq = bytes2bit_seq(seq)
      temp_plain = DES_dec(seq, num_rounds, inputkey64)
      temp_plain = bin2byte_seq(temp_plain)
      plainbyteseq += temp_plain
    # write the plainbyteseq to output file
    fout = open(output_fname, 'wb')
    fout.write(plainbyteseq)
    fout.close()

DES_enc_test('plain_file', '<anykey>', 16, 'cipher_file')
DES_dec_test('cipher_file', '<anykey>', 16, 'new_plain_file')
