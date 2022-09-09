from models import MafiaMember, JailedMember


def go_to_jail(list_of_members, jailed_name, list_of_jailed):
    for jailed_member in list_of_members:

        if jailed_member.name == jailed_name:
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
                if jailed.name == jailed_name:
                    if jailed.equal_seniority:
                        for member in list_of_members:
                            if member.name in jailed.subordinates:
                                MafiaMember.add_boss(member, jailed.equal_seniority.name)
                                MafiaMember.add_subordinates(jailed.equal_seniority, member.name)

                        if jailed_boss:
                            MafiaMember.add_subordinates(jailed_boss, jailed.name)

                    else:

                        senior_subordinate = JailedMember.get_senior_subordinate(jailed)
                        if jailed_boss:
                            MafiaMember.del_subordinates(jailed_boss, jailed.name)
                            if senior_subordinate:
                                MafiaMember.add_subordinates(jailed_boss, senior_subordinate.name)

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

                print("*******************************************************************************")

