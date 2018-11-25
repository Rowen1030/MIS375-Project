
import os
import sys

"""
Script Purpose: Easily manage annotations for your interfaces
"""

#Constants
#Directory Information
maps_dir = "../interfaces/"


def get_maps():
    exclude = set(['libs','pointclouds'])
    maps_list = []
    for root, dirs, files in os.walk(maps_dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            if file[len(file)-5:len(file)] == '.html':
                maps_list.append(os.path.join(root,file))
        
    return maps_list
def main():
    maps_list = get_maps()
    print('\n')
    print('''  ___                    _        _             
 / _ \                  | |      | |            
/ /_\ \_ __  _ __   ___ | |_ __ _| |_ ___  _ __ 
|  _  | '_ \| '_ \ / _ \| __/ _` | __/ _ \| '__|
| | | | | | | | | | (_) | || (_| | || (_) | |   
\_| |_/_| |_|_| |_|\___/ \__\__,_|\__\___/|_|   ''')
    print('---------------------------------------------------------------------')
    print('Select a map to manage annotations for. Enter the Number Besides the Name\n')
    for map in maps_list:
        print(str(maps_list.index(map)) + '. ' + map)


main()
