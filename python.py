import random
def generate_otp(length=4):
    otp = ''
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp
# Test the function
if __name__ == "__main__":
    otp = generate_otp()
    print("Generated OTP:", otp)
