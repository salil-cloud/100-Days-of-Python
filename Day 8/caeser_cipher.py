print('''
                                           __..--"""-.
                                 __.__..--""_..--""| ||
                            __..-"""_..--"""       | ||
                    __..--""_..--"""               | ||
                  .' __--"""                       | ||
                  |."                              | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||                               | ||
                  ||       ______________          | ||
                  ||      |__|__|__|__|__|         | ||
                  ||_________________              | ||
 _________________|_______     iBook """"""""""""""' ||
|""""""------......______ """""""-------.......______||
'-----_____   """        """"""---------""""""        |
           """""-----....._____   |     ______-----"""'
                               """""""""  grp
''')

result = ""  

def caeser_cipher_encode(user_input, shifts) :
    global result  
    for s in user_input :
        if s >= 'A' and s <= 'z' :
            result += chr(ord(s) + shifts)
        else :
            result += s
    return result

def caeser_cipher_decode(shifts) :
    global result  
    decyphered = ""
    for s in result :
        if s == " " :
            decyphered += s
        decyphered += chr(ord(s) - shifts)
    return decyphered

option = "yes"  

while option == "yes" : 
    user_input = input("Tell me the message : ")
    shifts = int(input("How many shifts : "))
    encrypted = caeser_cipher_encode(user_input, shifts)
    print(f"Your Encrypted message is : {encrypted} ")
    choice = input("Do you want to decode (yes/no): ").strip().lower()
    if choice == "yes" :
        completed_decipher = caeser_cipher_decode(shifts)
        print(f"Your original message was : {completed_decipher} ")
    option = input("Do you want to continue (yes/no): ").strip().lower()
