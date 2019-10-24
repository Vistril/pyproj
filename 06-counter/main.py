import pip, os

print("Checking package installations, please hold...")
os.system('pip install pytest -q --user --no-warn-script-location')
os.system('pip install pytest-sugar -q --user')

import pytest
import counter as student

def main():
    a = ''
    while a not in ('run','test'):
        print("Choose an option:\n\tRun\n\tTest")
        a = input("Your choice: ")
        a = a.lower()
    if a=="run":
        print("\n--Running Program--\n")
        student.main()
    elif a=="test":
        print("\n--Testing Program--\n")
        pytest.main(['-v'])

if __name__ == '__main__':
    main()
    print("\n--Operation Complete--")
    input("Press the Enter key to exit...")
