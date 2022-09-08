def print_members_free(member):
    # esta funcion imprime nombres y descripcion de una lista de mafiosos
    subordinate_list = member["subordinates"]
    print(
        f'{member.get("name")} esta libre y tiene un nivel '
        f'{member.get("seniority")} de antigüedad '
        f'{"le reporta a " + member.get("boss") if member.get("boss") else "no reporta a nadie porque es el jefe"} '
        f'{"y sus subordinados son " + " y ".join(subordinate_list) if subordinate_list else "y no tiene subordinados"}')


