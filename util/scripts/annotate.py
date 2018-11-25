
import os
import sys

"""
Script Purpose: Easily manage annotations for your interfaces
"""

#Constants
#Directory Information
maps_dir = "../interfaces/"


def get_annotations(map_data):


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
    select_map = -1
    print(''' 
      ___                    _        _             
     / _ \                  | |      | |            
    / /_\ \_ __  _ __   ___ | |_ __ _| |_ ___  _ __ 
    |  _  | '_ \| '_ \ / _ \| __/ _` | __/ _ \| '__|
    | | | | | | | | | | (_) | || (_| | || (_) | |   
    \_| |_/_| |_|_| |_|\___/ \__\__,_|\__\___/|_|   ''')
    
    print('\n')
    
    print('---------------------------------------------------------------------\n')
    print('Select a map to manage annotations for. Enter the Number Besides the Name\n')
    for map in maps_list:
        print('\t[' + str(maps_list.index(map)) + '].\t' + map)
    print('\n---------------------------------------------------------------------\n')

    while(select_map not in range(0,len(maps_list))):
        try:
            select_map = int(input('\tEnter Number: '))
            if select_map not in range(0,len(maps_list)):
                print('Error: Invalid Number Choice\n')
        except:
            print('Error: Invalid Number Choice\n')
    with open(maps_list[select_map],'r') as map_file:
        map_data = map_file.read()

    #Parse and read file to setup scenes
    split_data = map_data.split('\n')

    print(split_data)

    if '\tviewer.setScene(sceneSG);' not in split_data:
        split_data.insert(split_data.index('\t\tviewer.loadGUI(() => {'),'\t\tlet sceneSG = new Potree.Scene();')
        split_data.insert(split_data.index('\t\tviewer.loadGUI(() => {'),'\t\tlet sceneLion = new Potree.Scene();')
        split_data.insert(split_data.index('\t\tviewer.loadGUI(() => {'),'\t\tviewer.setScene(sceneSG);')

    annotations_list = get_annotations(split_data)    
      


main()
