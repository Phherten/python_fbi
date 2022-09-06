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
    def get_next_boss(self, member):
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
        return f'{self.name} tiene nivel {self.seniority} de antigüedad,' \
               f'{" y ".join(self.subordinates) + " son sus subordinados" if self.subordinates else " "}' \
               f'{"y su jefe actual es " + self.boss if self.boss else " y es el jefe"}'

    def get_boss(self):
        return self.boss

    def add_boss(self, name):
        self.boss = name
        return self.boss

    def get_subordinates(self):
        return self.subordinates


class Jail:
    def __init__(self, members=[]):
        self.members = members

    def get_members_jail(self):
        return self.members

    def got_to_jail(self, member):
        self.members.append(member)

    def get_out_jail(self, name):
        for index, member in enumerate(self.members):
            if member.name == name:
                self.members.pop(index)

        return self.members
