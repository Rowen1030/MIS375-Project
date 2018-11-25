

class Annotation(object):
    
    def __init__(self,pos,target,title,desc):
        self.position = pos
        self.target = target
        self.title = title
        self.desc = desc

    #pos = a list of 3 coordinates
    def set_pos(self,pos):
        self.position = pos

    def set_target(self,target):
        self.target = target
    
    def set_title(self,title):
        self.title = title
    
    def set_desc(self,desc):
        self.desc = desc
    
    def get_pos(self):
        return self.position
    
    def get_target(self):
        return self.target

    def get_title(self):
        return self.title

    def get_desc(self):
        return self.desc

    #num refers to index count of annotation
    #generate final javascript to append into html file
    def generate_js(self,num):
        
       
        return '{\n let annotation' + str(num) + ' = new Potree.Annotation({ \n\t"cameraPosition:"[' + ','.join(str(x) for x in self.position) + '],"\n\ttitle": "' + self.title + '","\n\tcameraTarget": [' + ','.join(str(x) for x in self.target) + '], "\n\tdescription": "' + self.desc + '"\n\t}); \n\tsceneSG.annotations.add(annotation' + str(num) + ');\n }'
