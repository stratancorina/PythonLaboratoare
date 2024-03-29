import os.path
from cryptography.fernet import Fernet
import re



def create_key(p):
    key = Fernet.generate_key()
    with open(p, 'wb') as f:
        f.write(key)


def load_key(p):
    # create_key(p)
    with open(p, "rb") as f:
        key = f.read()
    return key


def encrypt_master_password():
    psw = "korina"
    with open("masterpassword.txt", "w") as f:
        encrypt = Fernet(key).encrypt(psw.encode())
        f.write(encrypt.decode())


def checkMasterPassword():  # function to check the master password
    # encrypt_master_password()
    password = input("Please enter the Master Password: ")
    text_file = open("masterpassword.txt", "r")
    master_password = text_file.read()
    decrypt_mp = Fernet(key).decrypt(master_password.encode()).decode()
    text_file.close()
    if password == decrypt_mp:
        return True
    else:
        return False


def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)
    if str == None:
        return False

    if re.search(p, str):
        return True
    else:
        return False


def site_exists(str):
    with open('pwmanager.db', 'r+') as f:
        lines = [line.strip() for line in f.readlines()]
        if str in lines:
            return True
        else:
            return False


def username_exists(str):
    with open('pwmanager.db', 'r+') as f:
        lines = [line.strip() for line in f.readlines()]
        i = lines.index(str)
        if str in lines:
            return lines[i+1]
        else:
            return ("False")


def appendNew():  # This function will append new password in the txt file
    file = open("pwmanager.db", 'a+')
    website = input("Website: ")
    if isValidURL(website):
        if site_exists(website):
            print("This site already exists with an inserted password with the username: ")
            print(str(username_exists(website)))
            answ = input("Do you want to update it? (y/n)")
            if answ == "y":
                updateExisting(website)
            else:
                pass
        else:
            userName = input("Username: ")
            password = input("Password: ")
            web = website + "\n"
            usr = userName + "\n"
            pwd = Fernet(key).encrypt(password.encode()).decode()
            file.write("\n")
            file.write(web)
            file.write(usr)
            file.write(pwd)
            file.close
            print("Done!")
    else:
        print("Site is not valid. Try again!")
        appendNew()


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def updateExisting(site):
    with open('pwmanager.db', 'r+') as f:
        lines = [line.strip() for line in f.readlines()]
        i = lines.index(site)
        new_password = input("Insert the new password: ")
        new_pwd = Fernet(key).encrypt(new_password.encode()).decode() + "\n"
        index = i + 2
        replace_line('pwmanager.db', index, new_pwd)
        print("Done!")


def updatePassword():
    with open('pwmanager.db', 'r+') as f:
        lines = [line.strip() for line in f.readlines()]
        try:
            site = input('Enter site: ')
            if isValidURL(site):
                i = lines.index(site)
                new_password = input("Insert the new password: ")
                new_pwd = Fernet(key).encrypt(new_password.encode()).decode()
                index = i + 2
                replace_line('pwmanager.db', index, new_pwd)
                print("Done!")
            else:
                print("Site is not valid. Try again!")
                updatePassword()
        except ValueError:
            print('Site not found!')


def remove_line(linetoskip):
    with open('pwmanager.db', 'r') as read_file:
        lines = read_file.readlines()
    currentLine = 1
    with open('pwmanager.db', 'w') as write_file:
        for line in lines:
            if currentLine == linetoskip + 1:
                pass
            elif currentLine == linetoskip + 2:
                pass
            elif currentLine == linetoskip + 3:
                pass
            else:
                write_file.write(line)
            currentLine += 1


def deletePassword():
    with open('pwmanager.db', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    try:
        site = input('Enter site: ')
        if isValidURL(site):
            i = lines.index(site)
            remove_line(i)
            print("Done!")
        else:
            print("Site is not valid. Try again!")
            deletePassword()
    except ValueError:
        print('Site not found!')


def getPassword():
    with open('pwmanager.db', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        try:
            site = input('Enter site: ')
            if isValidURL(site):
                i = lines.index(site)
                print("website: " + lines[i])
                print("username: " + lines[i + 1])
                password_to_decrypt = lines[i + 2]
                decrypt_password = Fernet(key).decrypt(password_to_decrypt.encode()).decode()
                print("password: " + decrypt_password)
            else:
                print("Site is not valid. Try again!")
                getPassword()
        except ValueError:
            print('Site not found!')


if __name__ == '__main__':
    key = load_key("thekey.key")
    path = "pwmanager.db"
    print('Welcome to your Password Manager!')
    logged = True
    while logged:
        if checkMasterPassword():
            print("""You're in!
            add - Insert a new password;
            remove - Delete a password;
            update -  Update a password;
            get -  Get a password;
            x - Quit """)

            done = False

            while not done:
                option = input("What do you want to do? \n")
                if option == "add":
                    # if checkMasterPassword():
                        appendNew()
                    # else:
                    #     print("Wrong password. Try again")
                elif option == "remove":
                    # if checkMasterPassword():
                        deletePassword()
                    # else:
                    #     print("Wrong password. Try again")
                elif option == "update":
                    # if checkMasterPassword():
                        updatePassword()
                    # else:
                    #     print("Wrong password. Try again")
                elif option == "get":
                    # if checkMasterPassword():
                        getPassword()
                    # else:
                    #     print("Wrong password. Try again")
                elif option == "x":
                    ans = input("Are you sure you want to quit?(y/n) \n")
                    if ans == "y":
                        done = True
                        logged = False
                        print("Bye bye!")
                    else:
                        pass
                else:
                    print("Invalid option")
        else:
            print("Wrong password. Try again")


