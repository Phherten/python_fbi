from models import MafiaMember


def get_in_jail(equal_seniority, subordinates, subordinate_senior, boss, list_of_members, list_of_jailed,
                nombre_detenido):
    # Recibe el nombre del detenido y calcula quien es su jefe, si tiene un compañero de igual nivel y quienes son
    # sus subordinados
    for member in list_of_members:
        if member.name == nombre_detenido:
            list_of_members.remove(member)
            list_of_jailed.append(member)
            boss = MafiaMember.get_boss(member)
            print(f'Hemos encarcelado a {member.name}')
            print("||||||||||||||||||||||||||||||||||||||")
            for propous in list_of_members:
                if MafiaMember.get_equal_member(propous, member):
                    equal_seniority = MafiaMember.get_equal_member(propous, member)
                else:
                    if MafiaMember.get_senior_subordinate(propous, member):
                        subordinates.append(MafiaMember.get_senior_subordinate(propous, member))
                        subordinates.sort(key=lambda x: x.seniority, reverse=True)
                        subordinate_senior = subordinates[0]

            # print(f'El quivalente a {nombre_detenido} es {equal_seniority}')
            # print(subordinate_senior.name if subordinate_senior else "no tiene subordinados")
            # print(f'El jefe de {nombre_detenido} es {boss}')

    # Comparamos la variable boss que tiene el nombre y traemos el objeto entero.
    for member in list_of_members:
        if member.name == boss:
            boss = member

    return equal_seniority, subordinates, subordinate_senior, boss, list_of_members, list_of_jailed, nombre_detenido
