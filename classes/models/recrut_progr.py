from .employee import Employee


class Recruiter(Employee):

    def work(self):
        s = super().work()
        s = s[:-1]
        return s + ' and start hiring.'

    def __str__(self):
        return 'Dolzhnost: ' + self.name
     

class Programer(Employee):

    def work(self):
        s = super().work()
        s = s[:-1]
        return s + ' and start coding.'

    def __str__(self):
        return 'Position: ' + self.name
