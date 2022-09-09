class MafiaMember:
    def __init__(self, name, seniority=0, subordinates=[], boss=""):
        self.name = name
        self.seniority = seniority
        self.subordinates = subordinates
        self.boss = boss

    def __str__(self):
        return f'{self.name}, {"a su cargo " + " y ".join(self.subordinates) + ", " if self.subordinates else ""}' \
               f'{"su jefe es " + self.boss if self.boss else "es el PADRINO"}'

    def get_name(self):
        return self.name

    def get_seniority(self):
        return self.seniority

    def get_boss(self):
        return self.boss

    def get_subordinates(self):
        return self.subordinates

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

    def get_senior_subordinate(self, member):
        # 1. Buscar los datos del subordinado
        # 2. Comparar los subordinados
        if self.boss == member.name:
            return self

    def clear_subordinates(self):
        self.subordinates.clear()


class JailedMember:
    def __init__(self, name, seniority, boss, list_of_members, subordinates=[]):
        self.list_of_members = list_of_members
        self.name = name
        self.seniority = seniority
        self.subordinates = subordinates
        self.json_subordinates = self.get_json_subordinates()
        self.senior_subordinate = self.get_senior_subordinate()
        self.boss = boss
        self.equal_seniority = self.get_equal_seniority()

    def get_json_subordinates(self):

        json_subordinates = []
        for subordinates in self.list_of_members:

            if subordinates.name in self.subordinates:
                json_subordinates.append(subordinates)
        return json_subordinates

    def get_senior_subordinate(self):
        if self.subordinates:
            self.json_subordinates.sort(key=lambda x: x.seniority, reverse=True)
            self.senior_subordinate = self.json_subordinates[0]
            return self.senior_subordinate

    def get_equal_seniority(self):
        for equal in self.list_of_members:
            if equal.seniority == self.seniority:
                return equal

    def get_boss(self):
        for boss in self.list_of_members:
            if boss.name == self.boss:
                return boss
