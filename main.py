from import_members import import_members
from go_to_jail import go_to_jail
from go_out_jail import go_out_jail


def main():
    list_of_members = []
    list_of_jailed = []

    print('Estos son los miembros de la mafia:')
    list_of_members = import_members('https://run.mocky.io/v3/6d754a01-9529-47fe-a6ee-8037836b8333')
    print("******************************************************************************************************")
    print("¿A quien has detenido?:")
    jailed_name = input()

    go_to_jail(list_of_members, jailed_name, list_of_jailed)
    go_out_jail(list_of_members, jailed_name, list_of_jailed)


if __name__ == '__main__':
    main()
