import sys

def caesar_str_enc(plaintext, K):
    ciphertext=""
    for ch in plaintext:
        encch = caesar_ch_enc(ch, K)
        ciphertext = ciphertext + encch
        
    return ciphertext

def caesar_ch_enc(ch, K):
    if ch == ' ':
      return ch
    uniform_plain_ascii = ord(ch) -  97
    uniform_cipher_ascii = (uniform_plain_ascii + K)%26
    encch= chr(uniform_cipher_ascii + 97)
    
    return encch
    

def caesar_str_dec(ciphertext, K):
    plaintext = ""
    for ch in ciphertext:
        decch = caesar_ch_dec(ch, K)
        plaintext = plaintext + decch
        
    return plaintext

def caesar_ch_dec (ch, K):
    if ch == ' ':
      return ch
    uniform_cipher_ascii = ord(ch) - 97
    uniform_plain_ascii = (uniform_cipher_ascii - K)%26
    decch = chr(uniform_plain_ascii +  97)
    
    return decch


def test_module():
    K = int(sys.argv[1])
    input_str = sys.argv[2]
        
    print(input_str)
    encstr = caesar_str_enc(input_str, K)
    print(encstr)
    decstr = caesar_str_dec(encstr, K)
    print(decstr)
    
    
if __name__=="__main__":
    test_module()

# In this case, if you call your file like this:
# >python caear_hw.py 3 "string to be encoded"
# it should first print the above string
# then the encrypted version of it
# and next the decrypted version of it i.e., the original one
