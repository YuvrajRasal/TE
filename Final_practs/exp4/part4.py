class Employee:
    emp_list = {}
    manager = {}

    def __init__(self, fname, lname, eid, emp_type):
        self.emp_list[eid] = self

    def info(self, obj):
        return (obj.fname, obj.lname, obj.eid, obj.type)


class Manager(Employee):
    test = {}
    dev = {}
    man_emp = {}

    def __init__(self, fname, lname, eid):
        super().__init__(fname, lname, eid, 'Manager')
        Employee.manager[eid] = self
        self.eid = eid
        self.fname = fname
        self.lname = lname
        self.type = 'Manager'

    def add(self, obj):
        super().emp_list[obj.eid] = obj
        if obj.type == 'Developer':
            self.dev[obj.eid] = obj
        else:
            self.test[obj.eid] = obj
        self.man_emp[obj.eid] = obj

    def remove(self, eid, emp_type):
        if emp_type == 'Tester':
            del self.test[eid]
        else:
            del self.dev[eid]
        del self.man_emp[eid]
        del super().emp_list[eid]

    def display(self):
        print('List of all employees:')
        for eid, obj in super().emp_list.items():
            print(obj.info(obj))


manager1 = Manager('John', 'Doe', 1)

manager1.add(Employee('Alice', 'Smith', 2, 'Employee'))
manager1.add(Employee('Bob', 'Johnson', 3, 'Employee'))
manager1.add(Manager('Eva', 'Green', 4))
manager1.add(Employee('Charlie', 'Brown', 5, 'Employee'))

print('List of employees:')
manager1.display()
print()

manager1.remove(3, 'Employee')
print('List of employees after removing Bob:')
manager1.display()
