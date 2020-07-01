from mac import mac_changer


if __name__=="__main__":
    '''
    mc=mac_changer()
    
    mac = mc.get_mac("enp6s0")
    print("MAC Address:",mac,"")

    mc.change_mac("enp6s0",random_mac)'''
    mc=mac_changer()
    mc.show_interfaces()
    mc.options()