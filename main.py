import requests
from models import MafiaMember, Jail


def main():
    list_of_members = []

    # Paso 1
    response = requests.get('https://run.mocky.io/v3/6d754a01-9529-47fe-a6ee-8037836b8333')
    for member in response.json().get('members', []):
        list_of_members.append(MafiaMember(**member))

    # Paso 2
    jail = Jail()
    for member in list_of_members:
        if member.name == 'Jhon':
            jail.got_to_jail(member)

    jail.get_out_jail('Jhon')

    print(list_of_members.("name"))


if __name__ == '__main__':
    main()
