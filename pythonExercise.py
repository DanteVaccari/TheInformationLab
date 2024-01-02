import random

def multiply_until_success():
    
    while True:
        A = random.randint(1, 9)
        B = random.randint(1, 9)

        C = A * B

        print(f"A: {A}, C: {C}")

        if C == 4:
            print("Success!")
            print(f"A: {A}, B: {B}")
            break

multiply_until_success()
