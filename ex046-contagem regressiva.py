from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1.0)
print('\033[;31;40mBUM! BUM! POOOW!\033[m')