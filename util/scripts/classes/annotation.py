

class Annotation(object):
    
    def __init__(self,pos,cpos,target,title,desc,index):
        self.position = pos
        self.cpos = cpos
        self.target = target
        self.title = title
        self.desc = desc
        self.index = index

    #pos = a list of 3 coordinates
    def set_pos(self,pos):
        self.position = pos

    def set_cpos(self,cpos):
        self.cpos=cpos

    def set_target(self,target):
        self.target = target
    
    def set_title(self,title):
        self.title = title
    
    def set_desc(self,desc):
        self.desc = desc

    def set_index(self,index):
        self.index = index
    
    def get_pos(self):
        return self.position
    
    def get_target(self):
        return self.target

    def get_cpos(self):
        return self.cpos

    def get_title(self):
        return self.title

    def get_desc(self):
        return self.desc
    
    def get_index(self):
        return self.index

    #num refers to index count of annotation
    #generate final javascript to append into html file
    def generate_js(self,num):
        
       

        return 'viewer.scene.annotations.add(new Potree.Annotation({position:[' + ','.join(str(x) for x in self.position) + '],"cameraPosition":[' + ','.join(str(x) for x in self.cpos) + '], "title":"' + self.title + '", "description":"' + self.desc + '", "cameraTarget":[' + ','.join(str(x) for x in self.target) + ']}));'

