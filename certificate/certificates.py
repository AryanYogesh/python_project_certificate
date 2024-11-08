

class cerf:
    def __init__(self, name, course, all_classes, all_assignments):
        self.name = name
        self.course = course
        self.all_classes = all_classes
        self.all_assignments = all_assignments

    def generate_certificate(self):
        if self.all_classes == 'Yes' and self.all_assignments == 'Yes':
            return {'name': self.name, 'course': self.course}
        else:
            return {}
            