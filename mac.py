import subprocess
import re
import random
'''
>>commands to Use
ifconfig eth0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up

'''
print( ''' \033[93m
____ __________ _  _   ____  ____  _  _  ___ _   _ 
| __ )___ /___  | || | | __ )|  _ \| || ||_ _| \ | |
|  _ \ |_ \  / /| || |_|  _ \| |_) | || |_| ||  \| |
| |_) |__) |/ / |__   _| |_) |  _ <|__   _| || |\  |
|____/____//_/     |_| |____/|_| \_\  |_||___|_| \_| \033[0m \033[91m
Mac Spoofer                       CODED BY BETABRAIN        \033[0m  \033[37m                                           

               [For Linux Users] \033[0m  
''')
class mac_changer:
    def __init__(self):
        self.mac = ""
        self.oldmac=""
        self.interfaces=[]
        self.interface_details={}
    
    def get_interfaces(self):
        ifs = subprocess.run(["ifconfig"],shell=False,capture_output=True)
        ifout=ifs.stdout.decode('utf-8')
        pattern=r'[a-z0-9]*:\s'
        regex=re.compile(pattern)
        interfaces=re.findall(regex,ifout)
        
        for i in interfaces:
            j=interfaces.index(i)
            interfaces[j]=i.split(":")[0]
        #ifouts=interfaces.group().split(" ")
        self.interfaces=interfaces
        return interfaces

    def get_mac(self, iface):
        output = subprocess.run(["ifconfig",iface],shell=False,capture_output=True)
        cmd_result = output.stdout.decode('utf-8')
        if len(cmd_result)==0:
            print("\033[91m Wrong Interface Name! Check Your Interface name!\033[0m")
        else:
            #print(cmd_result)
            pattern = r'ether\s[\da-zA-Z]{2}:[\da-zA-Z]{2}:[\da-zA-Z]{2}:[\da-zA-Z]{2}:[\da-zA-Z]{2}:[\da-zA-Z]{2}'
            regex = re.compile(pattern)
            search_result = regex.search(cmd_result)
            if search_result==None:
                return ""
            else:    
                current_mac = search_result.group().split(" ")[1]
                self.mac=current_mac
                return current_mac

    
    def show_interfaces(self):
        interface_names=self.get_interfaces()
        interface_detail={}
        for i in interface_names:
            interface_detail[i]=self.get_mac(i)
        self.interface_details=interface_detail
        print('INTERFACES IN YOUR MACHINE')
        print("++++++++++++++++++++++++++")
        i=0
        for key in interface_detail:
            i+=1
            print(i,") Name: \033[94m",key,"\033[0m Mac Address: \033[94m",interface_detail[key],"\033[0m")
        print("\n")
        
            
    def options(self):
        
        while True:
            choicei=int(input("Choose Interface: "))
            if(choicei == 1 or choicei == 2 or choicei == 3):
                break
            print("\033[91m Wrong Choice! choose the number corresponding to the interface.\033[0m")
        
        iface = self.interfaces[choicei-1]
        self.oldmac = self.interface_details[iface]
        print("1. Custom MAC Address\n2. Generate Random")
        while True:
            choice=int(input("Choice: "))
            if(choice == 1 or choice == 2):
                break
            print("\033[91m Wrong Choice! choose the number corresponding to the choice. \033[0m")
        if choice==1:
            print("\033[36m Research and find valid mac addresses!\033[0m")
            print("\033[95m[+] Current MAC Address is ",self.get_mac(iface),"\033[0m")
            while True:
                
                cust_mac=input("Enter New Mac Address:")
                print("Trying...")
                success=self.change_mac(iface,cust_mac)
                if success==1:
                    print("\033[92m[+] Updated MAC Address is",self.get_mac(iface),'\033[0m')
                    break
                print("\033[91m Invalid MAC Address! \033[0m")

        if choice==2:
            print("\033[95m[+] Current MAC Address is ",self.get_mac(iface),'\033[0m')
            while True:
                random_mac="%02x:%02x:%02x:%02x:%02x:%02x" % (
                                                    random.randint(0, 255),
                                                    random.randint(0, 255),
                                                    random.randint(0, 255),
                                                    random.randint(0, 255),
                                                    random.randint(0, 255),
                                                    random.randint(0, 255)
                                                    )
                
                success=self.change_mac(iface,random_mac)
                if success==1:
                    
                    print("\033[92m[+] Updated MAC Address is",self.get_mac(iface),'\033[92m')
                    break

    def change_mac(self,iface,new_mac):
        
        output = subprocess.run(["ifconfig",iface,"down"],shell=False,capture_output=True)
        #output.stderr.decode('utf-8')

        output = subprocess.run(["ifconfig",iface,"hw","ether",new_mac],shell=False,capture_output=True)
        #output.stderr.decode('utf-8')

        output = subprocess.run(["ifconfig",iface,"up"],shell=False,capture_output=True)
        #output.stderr.decode('utf-8')
        if self.get_mac(iface)==self.oldmac:
            return 0
        #print("[+] Updated MAC Address is",self.get_mac(iface))
        else:
            return 1
        #return self.get_mac(iface)
