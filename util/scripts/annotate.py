
import os
import sys
import re
import readline
from classes.annotation import Annotation

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
            #print(line)
            pos_string = re.search('(?<=position:\[)(?s).*?(?=])',line).group(0).split(',')
            cam_pos_string = re.search('(?<=cameraPosition":\[)(?s).*?(?=])',line).group(0).split(',')
            cam_target_string = re.search('(?<=cameraTarget":\[)(?s).*?(?=])',line).group(0).split(',')
            anno = Annotation([float(x) for x in pos_string], [float(x) for x in cam_pos_string],[float(x) for x in cam_target_string], re.search('(?<="title":")(?s).*?(?=")', line).group(0), re.search('(?<="description":")(?s).*?(?=")', line).group(0),map_data.index(line))
            #print(anno.generate_js(1))
            annotation_list.append(anno)
    

    return annotation_list


def annotations_menu(annotations_list):
    print('---------------------------------------------------------------------\n')
    print('Enter 0 to add a new Annotation or Select an Annotation to Edit/Delete. Enter the Number Besides the Name\n')
    print('\t[0]\tAdd New Annotation')
    for anno in annotations_list:
        print('\t[' + str(annotations_list.index(anno)+1) + ']' + '\t' + anno.get_title()) 


def get_annotation():

    is_num=False

    anno_title = raw_input('Enter the title of your annotation: ')
    anno_desc = raw_input('Enter the description of your annotation: ')
    while not is_num:
        try:    
            anno_X = float(input('Enter the X value of your annotation position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')
    
    is_num=False
    while not is_num:
        try:    
            anno_Y = float(input('Enter the Y value of your annotation position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')

    is_num=False
    while not is_num:
        try:    
            anno_Z = float(input('Enter the Z value of your annotation position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')

    is_num=False
    while not is_num:
        try:    
            cam_X = float(input('Enter the X value of your Camera Position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')

    is_num=False
    while not is_num:
        try:    
            cam_Y = float(input('Enter the Y value of your Camera Position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')

    is_num=False
    while not is_num:
        try:    
            cam_Z = float(input('Enter the Z value of your Camera Position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')
    
   
    
    """ is_num=False
    while not is_num:
        try:    
            camTarg_X = float(input('Enter the X value of your Camera Target Position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')

    is_num=False
    while not is_num:
        try:    
            camTarg_Y = float(input('Enter the Y value of your Camera Target Position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n')

    is_num=False
    while not is_num:
        try:    
            camTarg_Z = float(input('Enter the Z value of your Camera Target Position: '))
            is_num = True
        except:
            print('Error: Invalid Number Choice\n') """

    return Annotation([anno_X,anno_Y,anno_Z],[cam_X,cam_Y,cam_Z],[anno_X,anno_Y,anno_Z],anno_title,anno_desc,5)


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
            if select_anno not in range(-1,len(annotations_list)+1):
                print('Error: Invalid Number Choice\n') 
        except:
            print('Error: Invalid Number Choice\n')

    if select_anno == 0:
        new_annotation = get_annotation()
        new_line = new_annotation.generate_js()
        split_data.insert(split_data.index("\t\t\tviewer.fitToScreen();")+1,new_line)
        new_file = '\n'.join([str(x) for x in split_data])
        with open(maps_list[select_map],'w') as map_file:
            map_file.write(new_file)
        print("Annotation added")
    elif select_anno == -1:
        quit()
    else:
        edit_annotation(annotations_list[select_anno-1],annotations_list,select_anno,maps_list,split_data)
        '''
        confirm = raw_input("Enter YES to DELETE this annotation. Any other input will cancel the operation: ")    
        if confirm in ['yes','YES','Yes']:
            split_data.pop(annotations_list[select_anno-1].get_index())
            new_file = '\n'.join([str(x) for x in split_data])
            with open(maps_list[select_map],'w') as map_file:
                map_file.write(new_file)
            print("Annotation deleted")
            
        else:
            quit()
            '''


def edit_menu(anno):
    print('----------------------------------------')
    print('Select a choice (-1 to cancel without Saving)')
    print('')
    print('[0] Delete')
    print('[1] Edit Title (Current: ' + anno.get_title() + ')')
    print('[2] Edit Description')
    print('[3] Edit Position (Current: ' + str(anno.get_pos()) + ')')
    print('[4] Edit Camera Position (Current: ' + str(anno.get_cpos()) + ')')
    print('[5] Save and Quit')
    print()


#Pass annotation class obj as parameter
#Recursive!
def edit_annotation(anno,annotations_list,select_anno,maps_list,split_data):
    edit_menu(anno)
    
    choice = str(raw_input("Enter Choice: "))
    while( choice not in ['-1','0','1','2','3','4','5']):
        print('Invalid Choice')
        edit_menu(anno)
        choice = str(raw_input("Enter Choice: "))
    
    if choice == '-1':
        print('quitting')
        quit()
    elif choice =='0':
        confirm = raw_input("Enter YES to DELETE this annotation. Any other input will cancel the operation: ")    
        if confirm in ['yes','YES','Yes']:
            split_data.pop(annotations_list[select_anno-1].get_index())
            new_file = '\n'.join([str(x) for x in split_data])
            with open(maps_list[select_map],'w') as map_file:
                map_file.write(new_file)
            print("Annotation deleted")
            
        else:
            quit()
    elif choice == '1':
        
        new_title = rlinput('Edit Title: ',anno.get_title())
        anno.set_title(new_title)
        edit_annotation(anno,annotations_list,select_anno,maps_list,split_data)
    elif choice == '2':
        
        new_title = rlinput('Edit Description: ',anno.get_desc())
        anno.set_title(new_title)
        edit_annotation(anno,annotations_list,select_anno,maps_list,split_data)
    elif choice == '3':
        is_num=False
        while not is_num:
            try:
                print('Current Position = ' + str(anno.get_pos()))    
                anno_X = float(input('Enter the X value of your annotation position: '))
                is_num = True
            except:
                print('Error: Invalid Number Choice\n')
        
        is_num=False
        while not is_num:
            try:
                print('Current Position = ' + str(anno.get_pos()))      
                anno_Y = float(input('Enter the Y value of your annotation position: '))
                is_num = True
            except:
                print('Error: Invalid Number Choice\n')

        is_num=False
        while not is_num:
            try:
                print('Current Position = ' + str(anno.get_pos()))     
                anno_Z = float(input('Enter the Z value of your annotation position: '))
                is_num = True
            except:
                print('Error: Invalid Number Choice\n')
        anno.set_pos([anno_X,anno_Y,anno_Z])
        anno.set_target([anno_X,anno_Y,anno_Z])
        edit_annotation(anno,annotations_list,select_anno,maps_list,split_data)
    elif choice =='4':
        is_num=False
        while not is_num:
            try:
                print('Current Camera Position = ' + str(anno.get_cpos))    
                cam_X = float(input('Enter the X value of your Camera Position: '))
                is_num = True
            except:
                print('Error: Invalid Number Choice\n')

        is_num=False
        while not is_num:
            try:
                print('Current Camera Position = ' + str(anno.get_cpos))    
                cam_Y = float(input('Enter the Y value of your Camera Position: '))
                is_num = True
            except:
                print('Error: Invalid Number Choice\n')

        is_num=False
        while not is_num:
            try:
                print('Current Camera Position = ' + str(anno.get_cpos))    
                cam_Z = float(input('Enter the Z value of your Camera Position: '))
                is_num = True
            except:
                print('Error: Invalid Number Choice\n')
        
        anno.set_cpos([cam_X,cam_Y,cam_Z])
        edit_annotation(anno,annotations_list,select_anno,maps_list,split_data)
    elif choice == '5':
        split_data[annotations_list[select_anno-1].get_index()] = anno.generate_js()
        new_file = '\n'.join([str(x) for x in split_data])
        with open(maps_list[select_map],'w') as map_file:
            map_file.write(new_file)
        print('Annotation Edited')




                

def rlinput(prompt, prefill=''):
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
      return raw_input(prompt)
    finally:
      readline.set_startup_hook()


main()


