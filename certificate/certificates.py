

class cerf:
    def __init__(self,name,course,classes,assignment):
        self.name = name
        self.course = course
        self.classes = classes
        self.assignment = assignment

    def generate_certificate(self):
        dicts={}
        if self.classes.lower()=='yes' and self.assignment.lower()=='yes':
            dicts={'name':self.name,
                   'course':self.course}
            return dicts

            