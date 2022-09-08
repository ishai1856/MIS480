# Ishai Lingan
# MIS480 - Parts Scan List
# Dr. Chris den Heijer
# 9/4/2022

import uuid
import pprint


class home:
    def __init__(self, e, u, a, c, st, z, sq, p, ss, mn):
        self.entry = e
        self.serial = u
        self.model = a
        self.temp = c
        self.uptime = st
        self.power = z
        self.bandwa = sq
        self.bandwb = p
        self.startsvc = ss
        self.brand = mn

    def addhome(self):
        add_dict = {
            'entry_no': self.entry,
            'serial': self.serial,
            'model': self.model,
            'temp': self.temp,
            'uptime': self.uptime,
            'power': self.power,
            'bandwa': self.bandwa,
            'bandwb': self.bandwb,
            "startsvc": self.startsvc,
            "brand": self.brand
        }
        return add_dict


def getzip():
    myzip = 0
    while len(str(myzip)) != 5:
        try:
            #    if 5 < len(str(myzip)) or len(str(myzip)) > 5:
            myzip = int(input('Input 5 digit zip code:\n'))
            if len(str(myzip)) != 5:
                print('There is an error with your input. Please give only 5 digits\n')
            else:
                pass
        except ValueError:
            print('There is an error with your input. Please use an integer value only,'
                  ' and only give the five digit version.\n'
                  )
    return myzip


def getprice():
    myprice = 0
    while myprice == 0:
        try:
            myprice = int(input('Please enter the price in dollars\n$'))
        except ValueError:
            print('There is an error with your input. Please use an integer value only.\n')
    return myprice


def getsqft():
    mysqft = 0
    while mysqft == 0:
        try:
            mysqft = int(input('Please enter the square feet, rounded to the closest foot\n'))
        except ValueError:
            print('There is an error with your input. Please use an integer value only.\n')
    return mysqft


def showrecs():
    print('Current Records')
    print(pprint.pformat(homedict, width=128, sort_dicts=False).replace('{', '').replace('}', ''))
    return


def getsalestatus():
    mysalestatus = None
    while mysalestatus == None:
        print(
            'Please enter Sales Status'
            '\n[1] Sold'
            '\n[2] Available'
            '\n[3] Under Contract'
        )
        try:
            ss_choice = int(input())
            if 0 < ss_choice < 4:
                if ss_choice == 1:
                    mysalestatus = 'sold'
                if ss_choice == 2:
                    mysalestatus = 'available'
                if ss_choice == 3:
                    mysalestatus = 'under contract'
            else:
                print('Invalid Value, only integers from 1-3 are valid. ')
                continue
            print('Status Selected:', mysalestatus)
            return mysalestatus
        except ValueError:
            print('Invalid Value, integers from 1-3 are valid.\n')
            continue



def getupd():
    myupd = None
    while myupd == None:
        # try:
        print('Update Record Selected.')
        myupd = int(input('Please enter the entry number of your record to update\n'))
        myupdkey = input('Please enter the key you would like to update\n')
        myupdval = input('Please enter the value you would like to update\n')
        homedict[myupd][myupdkey] = myupdval
        return


if __name__ == "__main__":
    homedict = {}
    print('\nWelcome to the Home Inventory Program.')
    while True:
        print(
            '\nTo proceed, please make a selection from the following menu:'
            '\n[1] Add a new record'
            '\n[2] Update an existing record'
            '\n[3] Remove an existing record'
            '\n[4] View records'
            '\n[5] Save current working records to a text file'
            '\n[6] Quit'
        )
        try:
            choice = int(input('Enter your selection number and hit enter:\n'))
        except ValueError:
            print('Sorry, Please select by number using only an integer value (digit)')
            continue
        try:
            if 0 < choice < 7:
                if choice == 1:
                    print('Add new record selected.')
                    newuuid = uuid.uuid4().hex[:8]
                    newentryno = len(homedict)
                    print('Unique id assigned to entry', newentryno, 'is ' + newuuid)
                    newaddr = input('Please enter the street address:\n')
                    newcity = input('Please enter the city:\n')
                    newstate = input('Please enter the state:\n')
                    newsqft = getsqft()
                    newsalestatus = getsalestatus()
                    newzipcode = getzip()
                    newprice = getprice()
                    newModelname = input('Please enter the model name:\n')
                    newhome = home(newentryno, newuuid, newaddr, newcity, newstate, newzipcode, newsqft, newprice,
                                   newsalestatus, newModelname)
                    newdict = newhome.addhome()
                    homedict[newentryno] = newdict
                    print('New Record Added! Continuing to Main Menu.\n')
                if choice == 2:
                    print('Update record selected.')
                    showrecs()
                    getupd()
                if choice == 3:
                    print('Remove record selected.')
                    showrecs()
                    homedict.pop(int(input('Enter number of Record to remove\n')), None)
                if choice == 4:
                    showrecs()
                if choice == 5:
                    myfile = open('homes.txt', 'w')
                    for i in range(len(homedict)):
                        out_str = pprint.pformat(homedict, width=128, sort_dicts=False).replace('{', '').replace('}', '')
                    myfile.write(out_str)
                    myfile.close()
                    print('Output complete to homes.txt')
                elif choice == 6:
                    exit()
            else:
                print('Invalid Selection Number. Valid options are 1-7')
                continue
        except KeyboardInterrupt:
            print('There is an error with your input, please try again')
            continue
