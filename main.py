import requests
from models import MafiaMember
from import_members import import_members


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

    equal_seniority = None
    subordinates = []
    subordinate_senior = None
    boss = None

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

    # Paso 4 Reagrupar a los subordinados
    for member in list_of_members:
        # Si han detenido a tu jefe
        if member.boss == nombre_detenido:
            # Si tu jefe tiene un mafioso del mismo nivel:
            if equal_seniority:
                # Añade al member el nombre del equal seniority
                MafiaMember.add_boss(member, equal_seniority.name)
                # Añade al equal seniority al member como subordinado
                MafiaMember.add_subordinates(equal_seniority, member.name)
            # Si el miembro es el subordinado senior
            elif member.name == subordinate_senior.name:

                # print(subordinates)
                # Añade al miembro el actual jefe de tu jefe
                MafiaMember.add_boss(member, boss.name if boss else None)
                # Añade al miembro el otro subordinado que tenga tu jefe
                MafiaMember.add_subordinates(member, subordinates[1].name)
                # Si el jefe del miembro tenía jefe le añade como subordinado
                if boss:
                    MafiaMember.add_subordinates(boss, member.name)
            # Añade al miembro como subordinado de su compañero senior
            else:
                MafiaMember.add_boss(member, subordinate_senior.name)

            # Iteramos otra vez los miembros para buscar al jefe
            for person in list_of_members:

                if person.name == member.boss and person.subordinates == member.name:
                    MafiaMember.del_subordinates(person, member.name)

    for members in list_of_members:
        subordinates = members.subordinates

        for i in subordinates:

            if i == nombre_detenido:
                MafiaMember.del_subordinates(members, nombre_detenido)

    for member in list_of_members:
        print(MafiaMember.__str__(member))

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

    '''print(equal_seniority)
    print(subordinate_senior)
    print(f'Subordinates {subordinates}')'''

    if equal_seniority:

        for member in list_of_members:
            if member == equal_seniority:
                MafiaMember.clear_subordinates(member)
        for member in list_of_members:
            if member.name == nombre_detenido:
                for sub in list_of_members:
                    if sub.name == member.boss:
                        MafiaMember.add_subordinates(sub,member.name)





    else:
        for member in list_of_members:

            if member.name == subordinate_senior.name:
                if member.name == subordinates[0]:
                    MafiaMember.del_subordinates(member, subordinates[1])

                else:

                    MafiaMember.del_subordinates(member, subordinates[0])

    for member in list_of_members:
        print(MafiaMember.__str__(member))

    '''print("Desean encarcelar a otro miembro Si o No")
    respuesta = input()
    if respuesta == "Si":
        main()'''


if __name__ == '__main__':
    main()
