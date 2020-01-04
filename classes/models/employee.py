class Employee:

    def __init__(self, name, mail, phone, zp, time):
        self.name = name
        self.mail = mail
        self.phone = phone
        self.salary = zp
        self.time = time

    def work(self):
        return 'I come to office.'

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary
