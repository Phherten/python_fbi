from models import MafiaMember

def reorganized(list_of_members, nombre_detenido,next_boss,subordinates,subordinate)
    for member in list_of_members:
        if member.boss == nombre_detenido:
            if next_boss:
                MafiaMember.add_boss(member, next_boss.name)
                MafiaMember.add_subordinates(next_boss, member.name)
            elif member.name == subordinate.name:
                # print(subordinates)

                MafiaMember.add_boss(member, boss.name)
                MafiaMember.add_subordinates(member, subordinates[1].name)
                print(subordinates[0].name)
                # MafiaMember.add_subordinates(boss, subordinates[0].name)
            else:
                MafiaMember.add_boss(member, subordinate.name)
        for boss in list_of_members:

            if boss.name == member.boss and boss.subordinates == member.name:
                MafiaMember.del_subordinates(boss, member.name)

    for members in list_of_members:
        subordinates = members.subordinates
        for i in subordinates:

            if i == nombre_detenido:
                MafiaMember.del_subordinates(members, nombre_detenido)

    for member in list_of_members:
        print(MafiaMember.__str__(member))