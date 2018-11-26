
import os
import sys
import re
from classes.Annotation import Annotation

"""
Script Purpose: Easily manage annotations for your interfaces
"""

#Constants
#Directory Information
maps_dir = "../../interfaces/"


def get_annotations(map_data):
    annotation_list = []
	for line in map_data:
		if line[0:28].strip('\t') == 'viewer.scene.annotations.add':
			pos_string = re.search('position:\[\d*,\d*,\*d*\], line).strip('position:[').strip(']').split(',')
			cam_pos_string = re.search('cameraPosition":\[\d*,\d*,\*d*\], line).strip('position:[').strip(']').split(',')
			cam_target_string = re.search('cameraTarget":\[\d*,\d*,\*d*\], line).strip('position:[').strip(']').split(',')
			
			anno = Annotation([int(x) for x in pos_string], [int(x) for x in cam_pos_string], re.search((?<="title":")(?s).*?(?="), line), re.search((?<="description":")(?s).*?(?="), line), [int(x) for x in cam_target_string_string])
			print(anno.generate_js)
	test = Annotation([0,0,0],[0,0,0],[1,1,1],'Title','Description')
    
	print(test.generate_js(1))


    return ''

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


    annotations_list = get_annotations(split_data)    
      


main()
