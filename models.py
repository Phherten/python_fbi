class Mafia:
    def __init__(self, members=[]):
        self.members = members

    def get_equal_member(self, member):
        # Cambiar nombre de variable element
        for element in self.members:
            if element.seniority == member.seniority:
                return element
        return None

    # Cambiar nombre de metodo
    def get_next_boos(self, member):
        # 1. Buscar los datos del subordinado
        # 2. Comparar los subordinados
        subordinates = []
        for element in self.members:
            for sub in member.subordinates:
                if sub == element.name:
                    subordinates.append(element)

        subordinates.sort(key=lambda x: x.seniority, reverse=True)
        return subordinates[0]

    def add_new_boss(self, member):
        boss = self.get_equal_member(member)
        if boss:
            boss = self.get_next_boos(member)

        for element in self.members:
            if element.name in member.subordinates:
                element.boss = boss.name


class MafiaMember:
    def __init__(self, name, seniority=0, subordinates=[], boss=""):
        self.name = name
        self.seniority = seniority
        self.subordinates = subordinates
        self.boss = boss

    def __str__(self):
        return f'{self.name} - {self.seniority} - {self.subordinates} - {self.boss}'

    def get_subordinates(self):
        return self.subordinates

    def add_subordinate(self, name):
        self.subordinates.append(name)
        return self.subordinates

    def delete_subordinate(self, name):
        self.subordinates.remove(name)
        return self.subordinates


class Jail:
    def __init__(self, members=[]):
        self.members = members

    def got_to_jail(self, member):
        self.members.append(member)

    def get_out_jail(self, name):
        for index, member in enumerate(self.members):
            if member.name == name:
                self.members.pop(index)

        return self.members















