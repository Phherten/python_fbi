from models import Jail


def jail_member(list_of_members, nombre_detenido):
    jail = Jail()
    next_boss = None
    subordinates = []
    subordinate_senior = None
    boss = None

    for member in list_of_members:
        if member.name == nombre_detenido:
            jail.got_to_jail(member)
            list_of_members.remove(member)
            list_of_jailed.append(member)
            boss = MafiaMember.get_boss(member)
            print(f'Hemos encarcelado a {member.name}')
            print("||||||||||||||||||||||||||||||||||||||")
            for i in list_of_members:
                if MafiaMember.get_equal_member(i, member):
                    next_boss = MafiaMember.get_equal_member(i, member)
                else:
                    if MafiaMember.get_next_boss(i, member):
                        subordinates.append(MafiaMember.get_next_boss(i, member))
                        subordinates.sort(key=lambda x: x.seniority, reverse=True)
                        subordinate_senior = subordinates[0]

            print(f'El quivalente a {nombre_detenido} es {next_boss}')
            print(subordinate_senior.name)
            print(f'El jefe de {nombre_detenido} es {boss}')
