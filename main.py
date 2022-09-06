import requests
from models import MafiaMember, Jail, Mafia
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
        # print_members_free(member)

    # Paso 2 encarcelar a Jhon
    jail = Jail()
    for member in list_of_members:
        if member.name == 'Jhon':
            jail.got_to_jail(member)
            list_of_members.remove(member)
            list_of_jailed.append(member)
            print(f'Hemos encarcelado a {member.name}')
            print("||||||||||||||||||||||||||||||||||||||")

    # Paso 3 imprimir a la gente encarcelada
    print("Estos mafiosos estan encarcelados:")
    for i in list_of_jailed:
        print(f'*{i.name}')

    print("|||||||||||||||||||||||||||||||||||||||||||")

    # print(f'esta gente esta en la carcel{" y ".join(jail.members)}')

    # Paso 4 Reagrupar a los subordinados de Jhon
    for member in list_of_members:
        if member.boss == "Jhon":
            MafiaMember.add_boss(member, name="Pablo")
    for member in list_of_members:
        print(MafiaMember.__str__(member))

    # Paso 5 Soltar a Jhon
    for member in list_of_jailed:
        if member.name == 'Jhon':
            jail.get_out_jail(member)
            list_of_members.append(member)
            list_of_jailed.remove(member)
            print(f'Hemos soltado a {member.name}')
            print("||||                    |||||")

    for member in list_of_members:
        if member.name == 'Jhon':
            subordinates = MafiaMember.get_subordinates(member)
    for member in list_of_members:
        for i in subordinates:
            if i == member.name:
                MafiaMember.add_boss(member, name="Jhon")

    # Paso 6 Volver al antiguo organigrama

    for member in list_of_members:
        print(MafiaMember.__str__(member))


if __name__ == '__main__':
    main()
