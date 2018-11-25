

class Annotation():
    
    def __init__(self):
        self.position = [0,0,0]
        self.target = [0,0,0]
        self.title = ''
        self.desc = ''

    #pos = a list of 3 coordinates
    def set_pos(pos):
        self.position = pos

    def set_target(target)
        self.target = target
    
    def set_title(title):
        self.title = title
    
    def set_desc(desc):
        self.desc = desc
    
    def get_pos():
        return self.position
    
    def get_target():
        return self.target

    def get_title():
        return self.title

    def get_desc():
        return self.desc

    #num refers to index count of annotation
    def generate_js(num)