class MafiaMember:
    def __init__(self, name, seniority=0, subordinates=[], boss=""):
        self.name = name
        self.seniority = seniority
        self.subordinates = subordinates
        self.boss = boss

    def __str__(self):
        return f'{self.name}, {"a su cargo " + " y ".join(self.subordinates)+ ", " if self.subordinates else ""}' \
               f'{"su jefe es " + self.boss if self.boss else  ", es el Padrino"}'

    def get_boss(self):
        return self.boss

    def add_boss(self, name):
        if name:
            self.boss = name
        else:
            self.boss = None
        return self.boss

    def add_subordinates(self, name):
        self.subordinates.append(name)

    def del_subordinates(self, name):
        self.subordinates.remove(name)

    def get_subordinates(self):
        return self.subordinates

    def get_equal_member(self, member):
        # Cambiar nombre de variable element
        if self.seniority == member.seniority:
            return self
        return None

    # Cambiar nombre de metodo
    def get_senior_subordinate(self, member):
        # 1. Buscar los datos del subordinado
        # 2. Comparar los subordinados
        if self.boss == member.name:
            return self


    def add_new_boss(self, member):
        boss = self.get_equal_member(member)
        if boss:
            boss = self.get_next_boss(member)

        for element in self:
            if element.name in member.subordinates:
                element.boss = boss.name


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
