from pymongo import MongoClient
from database import Database
from model import PersonModel_Livros

db = Database(database="relatorio_05_parte2", collection="livros")
client = MongoClient("<mongodb_uri>")
db_client = client["<database_name>"]
person_model = PersonModel_Livros(db)

_id = person_model.create_livros("A comida", "Zé cambo", 2011, 29.99)
book = person_model.read_livros_by_id(_id)
person_model.update_livros(_id, "Espelho", "Cran", 2001, 39.99)

_id_2 = person_model.create_livros("Folha de inverno", "Grinth", 2013, 59.89)


