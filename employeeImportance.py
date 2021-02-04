# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        '''
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        '''
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """

        d = {}
        # print(id)
        # print(employees)
        for i in range(len(employees)):
            d[employees[i].id] = employees[i]
        # print(d)
        def dfs(eid):
            # print("ID WE ARE FINDING " + str(eid))
            for sub in d[eid].subordinates:
                d[eid].importance += dfs(sub)
            return d[eid].importance
        return dfs(id)
        

#testing
emp = Employee(1, 5, [2,3])
emp2 = Employee(2, 3, [])
emp3 = Employee(3, 3, [])

print(emp.getImportance([emp, emp2, emp3], 1))