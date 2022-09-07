import requests
from models import MafiaMember, Jail
from functions import print_members_free


def main():
    list_of_members = []
    list_of_jailed = []

    # Paso 1 Importartodo el grupo de mafiosos e imprimirlos

    print('Estos son los miembros de la mafia:')
    response = requests.get('https://run.mocky.io/v3/6d754a01-9529-47fe-a6ee-8037836b8333')
    for member in response.json().get('members', []):
        list_of_members.append(MafiaMember(**member))
        print_members_free(member)
    print("///////////////////////////////////////")
    print("Escribe el nombre del detenido:")
    nombre_detenido = input()
    # Paso 2 encarcelar a Un miembro
    jail = Jail()
    next_boss = None
    subordinates = []
    subordinate = None
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
                        subordinate = subordinates[0]
            print(f'El quivalente a {nombre_detenido} es {next_boss}')
            print(subordinates)
            print(f'El jefe de {nombre_detenido} es {boss}')

    # Paso 3 imprimir a la gente encarcelada
    print("Estos mafiosos que estan encarcelados:")
    for i in list_of_jailed:
        print(f'*{i.name}')

    print("|||||||||||||||||||||||||||||||||||||||||||")

    # Paso 4 Reagrupar a los subordinados
    for member in list_of_members:
        if member.boss == nombre_detenido:
            if next_boss:
                MafiaMember.add_boss(member, next_boss.name)
                MafiaMember.add_subordinates(next_boss, member.name)
            elif member.name == subordinate.name:
                #print(subordinates)

                MafiaMember.add_boss(member, boss)
                MafiaMember.add_subordinates(member, subordinates[1].name)
            else:
                MafiaMember.add_boss(member, subordinate.name)
        for boss in list_of_members:

            if boss.name == member.boss and boss.subordinates == member.name:
                MafiaMember.del_subordinates(boss, member.name)

    for members in list_of_members:
        subordinates = members.subordinates
        for i in subordinates:

            if i == nombre_detenido:
                MafiaMember.del_subordinates(members,nombre_detenido)

    for member in list_of_members:
        print(MafiaMember.__str__(member))

    # Paso 5 Soltar a Jhon
    for member in list_of_jailed:
        if member.name == nombre_detenido:
            jail.get_out_jail(member)
            list_of_members.append(member)
            list_of_jailed.remove(member)
            print(f'Hemos soltado a {member.name}')
            print("||||                    |||||")

    # Paso 6 Volver al antiguo organigrama

    for member in list_of_members:
        print(MafiaMember.__str__(member))


if __name__ == '__main__':
    main()
