print("-------------------------------------------- Caesar Cipher Tool --------------------------------------------------")
print("                              💀 WELCOME TO CAESAR CIPHER PROGRAM BY HARIS RANGREZ 💀 ") 
def encrypt(text, shift_value):
    output = ""
    for ch in text:
        if ch == " ":
            output += " "
        elif ch.isupper():
            output += chr((ord(ch) + shift_value - 65) % 26 + 65)
        else:
            output += chr((ord(ch) + shift_value - 97) % 26 + 97)
    return output

def decrypt(text, shift_value):
    output = ""
    for ch in text:
        if ch == " ":
            output += " "
        elif ch.isupper():
            output += chr((ord(ch) - shift_value - 65) % 26 + 65)
        else:
            output += chr((ord(ch) - shift_value - 97) % 26 + 97)
    return output

if __name__=="__main__": 
    print("1. ENCRYPTION🔒")
    print("2. DECRYPTION🔓")
    result = ""
    ch='yes'
    while(ch.lower()=='yes'):
        mode = int(input("Select any one of the modes 1️⃣   or 2️⃣  : "))
        if mode == 1:
            text = input("Enter the input text🙂: ")
            shift_value = int(input("Enter the shift value 😶‍🌫️: "))
            result = encrypt(text, shift_value)
            print("After Encryption 🕵️  :", result)
        elif mode == 2:
            text = input("Enter the input text🙂: ")
            shift_value = int(input("Enter the shift value 😶‍🌫️ : "))
            result = decrypt(text, shift_value)
            print("After decryption 🕵️  :", result)
        else:
            print("Invalid option 🥱")
        ch=input("Do you want to continue yes✅/no❌:")
