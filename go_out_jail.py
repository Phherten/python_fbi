from models import MafiaMember, JailedMember


def go_out_jail(list_of_members, jailed_name, list_of_jailed):
    for jailed in list_of_jailed:
        if jailed.name == jailed_name:
            list_of_members.append(jailed)
            list_of_jailed.remove(jailed)
            jailed_boss = JailedMember.get_boss(jailed)
            jailed_senior_subordinate = JailedMember.get_senior_subordinate(jailed)


            print(f'Hemos soltado a {jailed.name}')
            print("||||                    |||||")
            if jailed_boss:
                MafiaMember.add_subordinates(jailed_boss, jailed.name)
            if jailed.equal_seniority:


                # Si el detenido tiene mismo cargo que otro, le buscamos
                for free_member in list_of_members:

                    if free_member.name == jailed.equal_seniority.name:
                        # tenemos al mismo cargo y recorremos los subordinados del preso
                        for sub in jailed.subordinates:
                            # si los subordinados del preso estan en los subordinatos del igual los borramos
                            if sub in free_member.subordinates:
                                MafiaMember.del_subordinates(free_member, sub)
            else:
                if jailed_boss and jailed_senior_subordinate:
                    MafiaMember.del_subordinates(jailed_boss, jailed_senior_subordinate.name)

                for subordinate in jailed.json_subordinates:
                    if subordinate.name != jailed_senior_subordinate.name:
                        MafiaMember.del_subordinates(jailed_senior_subordinate, subordinate.name)
                    MafiaMember.add_boss(subordinate, jailed.name)

            for member in list_of_members:
                print(MafiaMember.__str__(member))
    print("*******************************************************************************")
