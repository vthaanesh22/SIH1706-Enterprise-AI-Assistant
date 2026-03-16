import random

def send_otp():
    otp = random.randint(100000,999999)
    print("Your OTP:", otp)
    return otp

generated_otp = send_otp()

user_otp = int(input("Enter OTP: "))

if user_otp == generated_otp:
    print("Login successful")
else:
    print("Invalid OTP")
