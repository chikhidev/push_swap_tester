import random
import os
import urllib.request

INT_MAX = 2147483647
INT_MIN = -2147483648
GREEN = "\033[0;92m"
RESET = "\033[0;0m"
RED = "\033[0;91m"
GREEN_BOLD = "\033[1;92m"
RED_BOLD = "\033[1;91m"
MAGNETA_BOLD = "\033[1;95m"

tests = [
    {"n": 5, "max": 12},
    {"n": 100, "max": 700},
    {"n": 500, "max": 5500}
]

global success
success = True
checker = ""

def testParsnig():
    print("\nTesting parsing ------------------------------------")
    cmd = './push_swap -0001 2 "3 +00004" 5 "6 7 8" +9 10'
    result = os.popen(cmd).read().strip()
    print(cmd, end=" ")
    if len(result) > 0:
        print(RED + "❌" + RESET)
        exit(1)
    else:
        print(GREEN + "✅" + RESET)
    
def checkAlreadySorted():
    print("\nTesting already sorted list ------------------------")
    cmd = './push_swap -15 8 12 42 1337'
    print(cmd, end=" ")
    result = os.popen(cmd).read().strip()
    if len(result) > 0:
        print(RED + "❌" + RESET)
        exit(1)
    else:
        print(GREEN + "✅" + RESET)

def runTest(n):
    array = []
    for i in range(n):
        newRandom = random.randint(INT_MIN, INT_MAX)
        if newRandom not in array : array.append(newRandom)
    initRes = "./push_swap " + " ".join(map(str, array))
    cmd = initRes + " | wc -l"
    result = os.popen(cmd).read().strip()
    checkerRes = os.popen(initRes + " | " + checker + " " + " ".join(map(str, array))).read().strip()
    print(f"{result}\tmoves", end=" ")

    for test in tests:
        if test["n"] == n:
            if int(result) > test["max"] or checkerRes != "OK":
                global success
                success = False
                print("❌", end="\t")
            else:
                print("✅", end="\t")
            break
    print(f"Checker: ", end=" ")
    if checkerRes == "OK":
        print(GREEN + checkerRes + RESET)
    else:
        print(RED + checkerRes + RESET)

def getChecker():
    global checker
    if operatingSystem == "nt":
        print("This script is not supported in Windows")
        exit(1)
    elif operatingSystem == "linux" or operatingSystem == "posix":
        checker = "./checker_linux"
        if not os.path.isfile(checker):
            print("checker_linux not found")
            try:
                print(GREEN_BOLD + "Downloading checker_linux..." + RESET)
                checker_url = "https://cdn.intra.42.fr/document/document/25123/checker_linux"
                urllib.request.urlretrieve(checker_url, checker)
                os.system("chmod 777 checker_linux")
            except:
                print("Error downloading checker_linux")
                exit(1)
    elif operatingSystem == "darwin":
        checker = "./checker_Mac"
        if not os.path.isfile(checker):
            print("checker_Mac not found")
            try:
                checker_url = "https://cdn.intra.42.fr/document/document/25122/checker_Mac"
                urllib.request.urlretrieve(checker_url, checker)
                os.system("chmod 777 checker_Mac")
            except:
                print("Error downloading checker_Mac")
                exit(1)
    else:
        print("OS not supported")
        exit(1)

if __name__ == "__main__":

    operatingSystem = os.name

    print(MAGNETA_BOLD + "Welcome to the push_swap tester!" + RESET)

    checkAlreadySorted()

    testParsnig()

    getChecker()
    timesToRunTest = int(input("\nHow many times do you want to run the test for cases(10, 100, 500): "))

    if (os.system("make") != 0):
        print("Error compiling push_swap")
        exit(1)

    for test in tests:
        print(f"\nRunning tests for n = {test['n']}\n")
        for i in range(timesToRunTest):
            runTest(test['n'])

    if success:
        print(GREEN_BOLD + "\nAll tests passed successfully! 🥳\n" + RESET)
    else:
        print(RED_BOLD + "\nSome tests failed 😞...\n")