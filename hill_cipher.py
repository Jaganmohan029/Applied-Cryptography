# Hill cipher
import numpy as np

def matrixinvmod26(M):
    Mod26invTable = {}
    for m in range(26):
      for n in range(26):
        if (m*n)%26==1:
            Mod26invTable[m] = n
    
    # Calculate Minv26
    Minv = np.linalg.inv(M)
    Mdet = np.linalg.det(M)
    
    # Let's find Mdet26 and Mdetinv26
    Mdet26 = Mdet%26
    if Mdet26 in Mod26invTable:
        Mdetinv26 = Mod26invTable[Mdet26]
    else:
        Mdetinv26 = None
    
    # Now, Let's find Madj26
    Madj = Mdet*Minv
    Madj26 = Madj%26
    
    # So, The mod-26 inverse of M from equation (1) will be
    Minv26 = (Mdetinv26*Madj26)%26
    Minv26 = np.matrix.round(Minv26, 0)%26
    
    return Minv26

def hill_enc(M, plaintext):
    global pt_length
    pt_length = len(plaintext)
    plaintext = plaintext.replace(' ','')
    plaintext = plaintext.lower()
    plain_matrix_list = []
    if (len(plaintext)%3 != 0):
        if len(plaintext)%3 == 1:
          plaintext = plaintext + 'jj'
        else:
          plaintext = plaintext + 'j'

    pt_ascii_list = [ord(c)-97 for c in plaintext]
    for i in range(0,len(pt_ascii_list),3):
        sub_list = pt_ascii_list[i:i+3]
        plain_matrix_list.append(sub_list)

    c_list = []
    for sublist in plain_matrix_list:
        temp_list = np.matmul(sublist,M)%26
        temp_list = (np.matrix.round(temp_list,0)).tolist()
        
        c_list = c_list + temp_list
    
    char_list = [chr(index+97) for index in c_list]
    c = ''.join(char_list)
    return c

def hill_dec(M, ciphertext):
    cipher_matrix_list = []
    Minv26 = matrixinvmod26(M)
    ct_ascii_list = [ord(c)-97 for c in ciphertext]
    for i in range(0,len(ct_ascii_list),3):
        sub_list = ct_ascii_list[i:i+3]
        cipher_matrix_list.append(sub_list)
    p_list = []
    for sublist in cipher_matrix_list:
        temp_list = np.matmul(sublist,Minv26)%26
        temp_list = temp_list.tolist()
        p_list = p_list + temp_list
    char_list = [chr(int(ind)+97) for ind in p_list]
    p = ''.join(char_list)
    p = p[:pt_length]
    return p
