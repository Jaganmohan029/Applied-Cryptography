import hmac
import hashlib
import random

def xor(byteseq1, byteseq2):
    # First we convert each byte to its int value
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]
    l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in zip(l1,l2)]
    result = b''.join(l1xorl2)
    return result

def F(byteseq, k):
    # create a hmac sha1 
    h = hmac.new(k, byteseq, hashlib.sha1)
    return h.digest()[:8]

# main block processing
def feistel_block(LE_inp, RE_inp, k):
    F_func_out = F(RE_inp,k)
    RE_out = xor(F_func_out, LE_inp)
    LE_out = RE_inp    
    return LE_out, RE_out
    
def gen_keylist(keylenbytes, numkeys, seed):
    keylist = []
    random.seed(seed)
    for i in range(numkeys):
      keylist.append(random.randint(246578894847,99887776987699).to_bytes(keylenbytes, byteorder="little"))
    return keylist

def feistel_enc(inputblock, num_rounds, seed):
    # first generate the required keys
    keylist = gen_keylist(8, num_rounds, seed)
    intermediate_inputblock = inputblock
    for key in keylist:
      intermediate_LE_out, intermediate_RE_out = feistel_block(intermediate_inputblock[:4], intermediate_inputblock[4:], key)
      intermediate_inputblock =  intermediate_LE_out + intermediate_RE_out
    cipherblock = intermediate_inputblock[4:] + intermediate_inputblock[:4]
    return cipherblock
    
def feistel_enc_test(input_fname, seed, num_rounds, output_fname):
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    cipherbyteseq = b''
    inp_bytes_array = [inpbyteseq[i:i+8] for i in range(0, len(inpbyteseq), 8)]
    print(inp_bytes_array)
    # Adding spaces in the end
    if len(inp_bytes_array[-1])<8:
      inp_bytes_array[-1] = inp_bytes_array[-1]+ b' '*(8 - len(inp_bytes_array[-1]))
    
    for seq in inp_bytes_array:
      temp_cipher = feistel_enc(seq, num_rounds, seed)
      cipherbyteseq += temp_cipher
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()
    
    
def feistel_dec(inputblock, num_rounds, seed):
    # first generate the required keys
    keylist = gen_keylist(8, num_rounds, seed)
    intermediate_inputblock = inputblock
    for key in reversed(keylist):
      intermediate_LE_out, intermediate_RE_out = feistel_block(intermediate_inputblock[:4], intermediate_inputblock[4:], key)
      intermediate_inputblock = intermediate_LE_out + intermediate_RE_out
    plainblock = intermediate_inputblock[4:] + intermediate_inputblock[:4]
    return plainblock

def feistel_dec_test(input_fname, seed, num_rounds, output_fname):
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    plainbyteseq = b''
    inp_bytes_array = [inpbyteseq[i:i+8] for i in range(0, len(inpbyteseq), 8)]
    print(inp_bytes_array)
    for seq in inp_bytes_array:
      temp_plain = feistel_dec(seq, num_rounds, seed)
      plainbyteseq += temp_plain
    fout = open(output_fname, 'wb')
    fout.write(plainbyteseq)
    fout.close()

#sample functions to run the Code
feistel_enc_test("inputfile", 900091, 16, "cipherfile")
feistel_dec_test("cipherfile", 900091, 16, "plainfile")
