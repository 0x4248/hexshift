# Hexshift
# A encryption algorithm that uses shifters to cipher hex.
# Github: https://www.github.com/0x4248/hexshift
# Licence: GNU General Public License v3.0
# By: 0x4248

import sys
import os
import hashlib
import hexshift
from colorama import Fore, Back, Style

version = "1.1.0"
banner = r""" **      ** ******** **     **  ******** **      ** ** ******** **********
/**     /**/**///// //**   **  **////// /**     /**/**/**///// /////**/// 
/**     /**/**       //** **  /**       /**     /**/**/**          /**    
/**********/*******   //***   /*********/**********/**/*******     /**    
/**//////**/**////     **/**  ////////**/**//////**/**/**////      /**    
/**     /**/**        ** //**        /**/**     /**/**/**          /**    
/**     /**/******** **   //** ******** /**     /**/**/**          /**    
//      // //////// //     // ////////  //      // // //           //     """


def shifter_mode_menu():
    """Shows the shifter mode menu

    Returns:
        int: Number of passes to use
    """

    while True:
        print(
            "Please select an option to adjust the security level. Increasing the number of passes will improve security but also increase processing time and storage space usage"
        )
        print("1) hexshift-8")
        print("2) hexshift-16")
        print("3) hexshift-32")
        print("4) hexshift-64")
        print("5) hexshift-128")
        print("6) hexshift-256")
        print("7) hexshift-512")
        print("8) Other")
        choice = input(">")
        if choice == "1":
            return 8
        elif choice == "2":
            return 16
        elif choice == "3":
            return 32
        elif choice == "4":
            return 64
        elif choice == "5":
            return 128
        elif choice == "6":
            return 256
        elif choice == "7":
            return 512
        elif choice == "8":
            while True:
                try:
                    number = int(input("Enter number of passes>"))
                except:
                    print("Enter a number only")
                    continue
                return number
        else:
            print("Chose a valid option 1 or 2")


def cli_encrypt():
    """Shows the encrypt menu"""

    while True:
        print("Please chose an option")
        print("1) Encrypt text")
        print("2) Encrypt file")
        choice = input(">")
        if choice == "1":
            text = input("Enter text to encrypt>").encode()
            passes = shifter_mode_menu()
            data, key = hexshift.encrypt(text, passes)
            while True:
                output_location = input(
                    "Where do you want to save the encrypted text and key>"
                )
                if os.path.exists(output_location):
                    break
                else:
                    print("Enter a valid location")
            hash_object = hashlib.md5(data)
            file_name = hash_object.hexdigest()
            open(file_name + ".txt", "wb").write(data)
            for a in key:
                for b in a:
                    open(file_name + ".key", "a").write(b)
                open(file_name + ".key", "a").write("\n")
            print("Written data file to: " + output_location + "/" + file_name + ".txt")
            print("Written key file to: " + output_location + "/" + file_name + ".key")
            sys.exit(0)
        elif choice == "2":
            file_location = input("Enter file to encrypt>")
            file_data = open(file_location, "rb").read()
            passes = shifter_mode_menu()
            data, key = hexshift.encrypt(file_data, passes)
            while True:
                output_location = input(
                    "Where do you want to save the encrypted file and key>"
                )
                if os.path.exists(output_location):
                    break
                else:
                    print("Enter a valid location")
            hash_object = hashlib.md5(data)
            file_name = hash_object.hexdigest()
            open(file_name + ".txt", "wb").write(data)
            for a in key:
                for b in a:
                    open(file_name + ".key", "a").write(b)
                open(file_name + ".key", "a").write("\n")
            print("Written data file to: " + output_location + "/" + file_name + ".txt")
            print("Written key file to: " + output_location + "/" + file_name + ".key")
            sys.exit(0)
        else:
            print(
                "Chose a valid option"
                + Fore.CYAN
                + " 1 "
                + Fore.RESET
                + "or"
                + Fore.CYAN
                + " 2"
                + Fore.RESET
            )


def cli_decrypt():
    """Shows the decrypt menu"""

    file_location = input("Enter file to decrypt>")
    key_location = input("Enter keyfile>")
    try:
        file_data = open(file_location, "rb").read()
    except FileNotFoundError:
        print("File not found")
        return
    try:
        key_data = open(key_location, "r").read()
    except FileNotFoundError:
        print("Keyfile not found")
        return
    key_data = key_data.split("\n")
    if len(key_data) != 4:
        print("Keyfile is not formatted correctly")
        return
    a = []

    for c in key_data:
        if len(c) == 0:
            break
        b = []
        for d in c:
            b.append(d)
        a.append(b)
    data = hexshift.decrypt(file_data, a)

    while True:
        output_location = input("Where do you want to save the decrypted file>")
        if os.path.exists(output_location):
            break
        else:
            print("Enter a valid location")

    file_name = input("File name to save decrypted file>")
    open(file_name, "wb").write(data)
    print("Written data file to: " + output_location + "/" + file_name)
    sys.exit(0)


if __name__ == "__main__":
    """Main function"""

    print(Fore.CYAN + banner + Style.RESET_ALL)
    print("Welcome to hexshift CLI V" + version)
    while True:
        print("Please chose an option")
        print("1) Encrypt")
        print("2) Decrypt")
        choice = input(">")
        if choice == "1":
            cli_encrypt()
            break
        elif choice == "2":
            cli_decrypt()
            break
        else:
            print(
                "Chose a valid option"
                + Fore.CYAN
                + " 1 "
                + Fore.RESET
                + "or"
                + Fore.CYAN
                + " 2"
                + Fore.RESET
            )
