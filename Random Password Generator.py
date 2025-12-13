import random 
import string

def password_generator():
    print("-Random Password Generator-")

    try:
        uzunluk = int(input("How many characters should your password have?:"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    karakter_havuzu = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakter_havuzu) for _ in range(uzunluk))
    print("Generated Password:", sifre)

password_generator()
            
              



