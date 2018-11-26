
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
        if re.match('viewer.scene.annotations.add',line.strip('\t')):
            print(line)
            pos_string = re.search('position:\[\d*,\d*,\d*\]', line).group(0).strip('position:[').strip(']').split(',')
            cam_pos_string = re.search('cameraPosition":\[\d*,\d*,\d*\]', line).group(0).strip('cameraPosition":[').strip(']').split(',')
            cam_target_string = re.search('cameraTarget":\[\d*,\d*,\d*\]', line).group(0).strip('cameraTarget":[').strip(']').split(',')
            anno = Annotation([int(x) for x in pos_string], [int(x) for x in cam_pos_string],[int(x) for x in cam_target_string], re.search('(?<="title":")(?s).*?(?=")', line).group(0), re.search('(?<="description":")(?s).*?(?=")', line).group(0),map_data.index(line))
            print(anno.generate_js(1))
            annotation_list.append(anno)
    

    return annotation_list

def annotations_menu(annotations_list):
    print('---------------------------------------------------------------------\n')
    print('Enter 0 to add a new Annotation or Select an Annotation to Delete. Enter the Number Besides the Name\n')
    print('\t[0]\tAdd New Annotation')
    for anno in annotations_list:
        print('\t[' + str(annotations_list.index(anno)+1) + ']' + '\t' + anno.get_title()) 

def get_annotation():
    
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

    #print(split_data)


    annotations_list = get_annotations(split_data)

    #Generate List of Annotations
    select_anno = -2
    while(select_anno not in range(-1,len(annotations_list)+1)):
        try:    
            annotations_menu(annotations_list)
            select_anno = int(input("Enter Selection (-1 to quit): " ))
            if select_anno not in range(-1,len(annotations_list)):
                print('Error: Invalid Number Choice\n') 
        except:
            print('Error: Invalid Number Choice\n')

    if select_anno = 0:
        new_annotation = get_annotation()
main()
