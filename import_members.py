import requests
from models import MafiaMember
from simple_functions import print_members_free


def import_members(url):
    # Busca el JSON con los mafiosos y los convierte en objetos de la clase MafiaMember
    response = requests.get(url)
    list_of_members = []
    for member in response.json().get('members', []):
        list_of_members.append(MafiaMember(**member))
        print_members_free(member)
    return list_of_members
