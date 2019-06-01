import os
import re
import fileinput
import subprocess
from subprocess import check_output, CalledProcessError, STDOUT


def subnet_scanner():
        """subnet_scanner is the first step to using this script tool, this function prompts the user for a subnet which it will
        then scan for all connected IP addresses and write the data to a file(variable IP4host). This file is cleaned up as a
        string and reprinted for future use as a reference point to host IP addresses across other defined functions, it also
         also takes that clean file and adds a ":" to the end of each line and saves that as a new file name hostsprocessed.txt
         this new file is the subnet host OS documentation file in which the 3/CHECK (commitscan function) will append OS guesses
         and other OS related information pertaining to corresponding host IP Address."""
        # asking user for subnet
        ip_net = input("what is your IP subnet with slash notation? e.g. 192.168.0.0/24 - ")

        print("Beginning scan for IP addresses from all hosts in the subnet...")
        print("...")
        print("...")
        print("...")

        # using cmd prompt in python to get nmap K>I>S>S(my rump) keep it simple stupid
        all_host_scan = os.system("nmap -oN IP4host.txt -sP " + ip_net)

        # textfile produced by nmap below
        file = open("IP4host.txt")
        filelister = []

        # title
        print("your host IPs are:")
        # recompiling txt into string with only IP Addresses
        for line in file:
                ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
                ip = ' '.join(ip)
                # turning into list to remove whitespaces
                filelister.append(ip)
                continue
        # turning back into string so later can output to file
        while ('' in filelister):
                filelister.remove('')

        stringlist = "\n".join(filelister)
        print(stringlist)

        # writing string with IPs to file named below
        f = open("hosts.txt", "w+")
        f.write(stringlist)

        f.close()
        new_collum = []
        iPofSubnet = stringlist[0:6]
        for linex in open("hosts.txt"):
                if iPofSubnet in linex:
                        new_collum.append(linex)

        d = open("hostsprocessed.txt", "w+")
        d.write(stringlist)
        d.close()

        fileroar = "hostsprocessed.txt"
        for lino in fileinput.FileInput(fileroar, inplace=1):
                if iPofSubnet in lino:
                        lino = lino.rstrip()
                        lino = lino.replace(lino, lino + ":" + "\n")
                print(lino,)


def os_scanner():
        """os_scanner is a function that will present hosts.txt(created by subnet_scanner) and index each line for user input,
        the user will be given a prompt asking for the index corresponding to the host they would like to scan, user can now
        append that host OS on the main menu by using the 3/CHECK input"""
        with open("hosts.txt", "r") as f:

                IP_TABLE = f.readlines()

                maxi = 0
                for c, value in enumerate(IP_TABLE, 0):
                        print(c, value)
                        if maxi < c:
                                maxi = c
        answers = int(input(
                "Starting from 0(being the net address) which hostnumber/line in the hosts.txt file would u like to scan? {INTEGERS ONLY}- "))
        host_no = answers  # change this incrementally for each line/host you copy paste the function

        def proccess():

                IP4scan = (IP_TABLE[host_no])

                print("Performing Scan on " + IP4scan)
                print(IP4scan)
                os.system("nmap -oN host_temp" + str(host_no) + ".txt -O --osscan-guess " + IP4scan)

        while True:

                with open("hosts.txt", "r") as f:
                        iP_TABLE = f.readlines()
                        numberOfTotalsHosts = len(iP_TABLE)
                        int(numberOfTotalsHosts)
                f.close()
                if int(answers) > int(numberOfTotalsHosts):
                        print("invalid input. You don't have that many hosts.")
                        os_scanner()
                        break

                elif answers == answers:
                        proccess()
                        break

                else:
                        print("invalid input. numbers/integers only.")
                        os_scanner()
                        break


def commitscan():
        """commitscan is a function that is supposed to be run after the user has run a 2/SCAN (os_scanner function) so that
        the host scanned can be appended in a nice format to a txt file named "hostsprocessed.txt" this file can be used for
        guessing network subnet hosts corresponding Operating Systems, this function can be edited easily to return other details
        besides Operating System guesses."""
        def fileExists(file):
                try:
                        f = open(file, 'r')
                        f.close()
                except FileNotFoundError:
                        return False
                return True

        def isLineEmpty(line):
                return len(line.strip()) < 1

        def removeEmptyLines(file):
                lines = []
                if not fileExists(file):
                        print("{} does not exist ".format(file))
                        return
                out = open(file, 'r')
                lines = out.readlines()
                out.close()
                out = open(file, 'w')
                t = []
                for line in lines:
                        if not isLineEmpty(line):
                                t.append(line)
                out.writelines(t)
                out.close()

        with open("hosts.txt", "r") as f:
                IP_TABLE = f.readlines()

        maxi = 0
        for c, value in enumerate(IP_TABLE, 0):
                print(c, value)
                if maxi < c:
                        maxi = c
        host_no = int(input(
                "Starting from 0(being the net address) which line in the hostnumber/hosts.txt file do u want to check and append scan results? {INTEGERS ONLY}- "))  # change this incrementally for each line/host you copy paste the function
        xix = []
        yiy = []
        ziz = []
        tit = []

        for line in open("host_temp" + str(host_no) + ".txt"):
                if "Running" in line:
                        xix.append(line)
                        continue

        for line2 in open("host_temp" + str(host_no) + ".txt"):
                if "Aggressive OS guesses:" in line2:
                        yiy.append(line2)
                        continue

        for line3 in open("host_temp" + str(host_no) + ".txt"):
                if "OS CPE:" in line3:
                        ziz.append(line3)
                        continue

        for line4 in open("host_temp" + str(host_no) + ".txt"):
                if "Warning" in line4:
                        tit.append(line4)
                        continue

        one_lines = (xix + yiy + ziz + tit)

        print(one_lines)

        while ('' in one_lines):
                one_lines.remove('')

        stringlist = "\n".join(one_lines)
        print(stringlist)

        IP_addrez = open("hosts.txt", "r")
        ip_addrez = IP_addrez.readlines()
        IP_addrez.close()
        new_string = ip_addrez[host_no].strip("\n")
        user_tells = ''.join((new_string, ":"))


        IP_address = []
        for linex in open("hostsprocessed.txt"):
                if user_tells in linex:
                        IP_address.append(linex)
        while ('' in IP_address):
                IP_address.remove('')

        IPlist = "\n".join(IP_address)
        print(IPlist)
        fileroar = "hostsprocessed.txt"
        for lino in fileinput.FileInput(fileroar, inplace=1):
                if IPlist in lino:
                        lino = lino.rstrip()
                        lino = lino.replace(lino, lino+'\n' + stringlist + '\n')
                print (lino,)
        removeEmptyLines("hostsprocessed.txt")



def main_menu():
        """This is the main menu which serves as a guide to understanding and properly using this tool, it provides a step by step
        view of the process as well as script 3/ DETAILS which include a guide on running the script. There are defined functions
        within thin one such as CheckMore which are used to prompt the user to do repeated actions but always give the option to
        also return to the main menu."""
        def CheckMore():
                print("\n \n CHECK COMPLETE: Your file - 'hostsprocessed.txt' has been appended with OS info.")
                print("Return to main menu or check more hosts?\n")
                answer = input("[1/MAIN] | [2/MORE] - ")
                while True:
                        if answer == "main":
                                main_menu()
                                break
                        elif answer == "more":
                                commitscan()
                                CheckMore()
                                break
                        elif answer == "1":
                                answer = "main"

                        elif answer == "2":
                                answer = "more"
                        else:
                                print("invalid input - Please try again")
                                CheckMore()
                                break

        def OSmore():
                print("\n \n SCAN COMPLETE:")
                print("Return to main menu or scan more hosts?\n")
                answer = input("[1/MAIN] | [2/MORE] - ").lower()
                while True:
                        if answer == "main":
                                main_menu()
                                break
                        elif answer == "more":
                                os_scanner()
                                OSmore()
                                break
                        elif answer == "1":
                                answer = "main"

                        elif answer == "2":
                                answer = "more"
                        else:
                                print("invalid input - Please try again")
                                OSmore()
                                break

        mainmenu = input(
                "[1/SUB] | [2/SCAN] | [3/CHECK] | {4/DETAILS] type number or word - ").lower()
        while True:
                if mainmenu == "sub":
                        subnet_scanner()
                        print("...")
                        print("scan complete returning to main menu.")
                        print("\n")
                        main_menu()
                        break

                elif mainmenu == "scan":
                        os_scanner()
                        OSmore()
                        break


                elif mainmenu == "check":
                        commitscan()
                        CheckMore()
                        break

                elif mainmenu == "details":
                        print("GUIDE:")
                        print("SUB - Scan your subnet first.")
                        print("SCAN - Secondly scan each host individually.")
                        print("CHECK - Thirdly create Operating System Guess summary in hostprocessed.txt file for each \n"
                              " host (this is where we can compare hosts)")
                        print("[")
                        main_menu()
                        break

                elif mainmenu == "1":
                        mainmenu = "sub"

                elif mainmenu == "2":
                        mainmenu = "scan"
                elif mainmenu == "3":
                        mainmenu = "check"
                elif mainmenu == "4":
                        mainmenu = "details"

                else:
                        print("invalid input - Please try again.")
                        main_menu()

                        break

print("Welcome to OS Guesser_0.1[uber_alpha]")
print("\n")
print("Description")
print("This script will collate OS specific details about hosts in a particular subnet. {WARNING} one subnet at a time.")
print("After running - To view a different subnet you must delete all host_temp.txt files, or use [SCAN] proccess,\n"
      " for more details use [4/DETAILS] in main menu .")
print("After being created hosts.txt file can be used to take reference of lines(hostnumber) correlated to ip address")

print("\n")
print("To begin - start with producing your host files by selecting SUB")
main_menu()








