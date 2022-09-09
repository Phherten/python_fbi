import requests
from models import MafiaMember, JailedMember
from import_members import import_members


def go_to_jail(list_of_members, nombre_detenido, list_of_jailed):
    # Detenemos al preso y creamos un objeto de la Clase JailedMember
    for jailed_member in list_of_members:
        if jailed_member.name == nombre_detenido:
            list_of_members.remove(jailed_member)
            list_of_jailed.append(
                JailedMember(MafiaMember.get_name(jailed_member), MafiaMember.get_seniority(jailed_member),
                             MafiaMember.get_boss(jailed_member), list_of_members,
                             subordinates=MafiaMember.get_subordinates(jailed_member)))

            print(f'Hemos encarcelado a {jailed_member.name}')
            print("||||||||||||||||||||||||||||||||||||||")

        # Elegimos si el detenido tiene un miembro de igual nivel o hay q nombrar a un subordinado

    for jailed in list_of_jailed:
        # Si tiene un miembro del mismo nivel: a sus subordinados le añadimos como jefe el mafioso de mismo nivel
        jailed_boss = JailedMember.get_boss(jailed)
        if jailed.name == nombre_detenido:
            if jailed.equal_seniority:
                for member in list_of_members:
                    if member.name in jailed.subordinates:
                        MafiaMember.add_boss(member, jailed.equal_seniority.name)
                        MafiaMember.add_subordinates(jailed.equal_seniority, member.name)

                MafiaMember.del_subordinates(jailed_boss, jailed.name)

            else:

                senior_subordinate = JailedMember.get_senior_subordinate(jailed)

                for subordinate in jailed.json_subordinates:

                    if subordinate.name == senior_subordinate.name:
                        if jailed_boss:
                            MafiaMember.add_boss(senior_subordinate, jailed_boss.name)
                        else:
                            MafiaMember.add_boss(senior_subordinate, "")

                    else:
                        MafiaMember.add_boss(subordinate, senior_subordinate.name)
                        MafiaMember.add_subordinates(senior_subordinate, subordinate.name)

    for member in list_of_members:
        print(MafiaMember.__str__(member))


def main():
    list_of_members = []
    list_of_jailed = []

    # Paso 1 Importartodo el grupo de mafiosos e imprimirlos

    print('Estos son los miembros de la mafia:')
    list_of_members = import_members('https://run.mocky.io/v3/6d754a01-9529-47fe-a6ee-8037836b8333')

    print("///////////////////////////////////////")
    print("Escribe el nombre del detenido:")
    nombre_detenido = input()

    # Paso 2 encarcelar a Un miembro

    go_to_jail(list_of_members, nombre_detenido, list_of_jailed)



    # Paso 5 Soltar al preso

    for member in list_of_jailed:
        if member.name == nombre_detenido:
            list_of_members.append(member)
            list_of_jailed.remove(member)
            print("*******************************************")
            print(f'Hemos soltado a {member.name}')
            print("||||                    |||||")

    subordinates = []
    for member in list_of_members:
        if member.name == nombre_detenido:
            for sub in member.subordinates:
                subordinates.append(sub)

    # Paso 6 Volver al antiguo organigrama
    # Volver a nombrar al antiguo Jefe
    for member in list_of_members:
        if member.name == nombre_detenido:
            ex_subordinates = member.subordinates
            for i in ex_subordinates:
                for x in list_of_members:
                    if x.name == i:
                        MafiaMember.add_boss(x, member.name)

    # Devolver subordinados a sus puestos

    print(equal_seniority)
    print(subordinate_senior)
    print(f'Subordinates {subordinates}')

    if equal_seniority:

        for member in list_of_members:
            if member == equal_seniority:
                MafiaMember.clear_subordinates(member)
        for member in list_of_members:
            if member.name == nombre_detenido:
                for sub in list_of_members:
                    if sub.name == member.boss:
                        MafiaMember.add_subordinates(sub, member.name)





    else:
        for member in list_of_members:

            if member.name == subordinate_senior.name:
                if member.name == subordinates[0]:
                    MafiaMember.del_subordinates(member, subordinates[1])

                else:

                    MafiaMember.del_subordinates(member, subordinates[0])

    for member in list_of_members:
        print(MafiaMember.__str__(member))

    print("Desean encarcelar a otro miembro Si o No")
    respuesta = input()
    if respuesta == "Si":
        main()'''


if __name__ == '__main__':
    main()
