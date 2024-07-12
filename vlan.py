# vlan_check.py

def check_vlan_range(vlan_number):
    normal_range = range(1, 1001)
    extended_range = range(1006, 4095)
    
    if vlan_number in normal_range:
        print(f"La VLAN {vlan_number} pertenece al rango normal.")
    elif vlan_number in extended_range:
        print(f"La VLAN {vlan_number} pertenece al rango extendido.")
    else:
        print(f"La VLAN {vlan_number} no pertenece ni al rango normal ni al extendido.")

def main():
    vlan_number = int(input("Ingrese el número de VLAN: "))
    check_vlan_range(vlan_number)

if __name__ == "__main__":
    main()
