import random
import os

INT_MAX = 2147483647
INT_MIN = -2147483648
GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"

tests = [
    {"n": 5, "max": 12},
    {"n": 100, "max": 700},
    {"n": 500, "max": 5500}
]

global success
success = True

def runTest(n):
    array = []
    for i in range(n):
        newRandom = random.randint(INT_MIN, INT_MAX)
        if newRandom not in array : array.append(newRandom)
    cmd = "./push_swap " + " ".join(map(str, array)) + " | wc -l"
    result = os.popen(cmd).read().strip()
    print(f"{result}\tmoves", end=" ")

    for test in tests:
        if test["n"] == n:
            if int(result) > test["max"]:
                global success
                success = False
                print("❌")
            else:
                print("✅")
            break

if __name__ == "__main__":
    timesToRunTest = int(input("How many times do you want to run the test for cases(10, 100, 500): "))
    max = 0
    min = 0

    if (os.system("make") != 0):
        print("Error compiling push_swap")
        exit(1)

    for test in tests:
        print(f"\nRunning tests for n = {test['n']}\n")
        for i in range(timesToRunTest):
            try:
                runTest(test['n'])
            except:
                print("Error running test")

    if success:
        print(GREEN + "\nAll tests passed successfully! 🥳\n" + RESET)
    else:
        print(RED + "\nSome tests failed 😞...\n")