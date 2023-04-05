from pymongo import MongoClient
from bson.objectid import ObjectId

class PersonModel_Livros:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_livros(self, titulo: str, autor: str, ano: int, preco: float) -> str:
        try:
            result = self.collection.insert_one({"Titulo": titulo, "Autor": autor, "Ano": ano, "Preco": preco})
            id_livros = str(result.inserted_id)
            print(f"Person {titulo} , {autor} , {ano} e {preco} created with id: {id_livros}")
            return id_livros
        except Exception as error:
            print(f"An error occurred while creating livro: {error}")
            return None

    def read_livros_by_id(self, id_livros: str) -> dict:
        try:
            person = self.collection.find_one({"_id": ObjectId(id_livros)})
            if person:
                print(f"Person found: {person}")
                return person
            else:
                print(f"No person found with id {id_livros}")
                return None
        except Exception as error:
            print(f"An error occurred while reading person: {error}")
            return None

    def update_livros(self, id_livros: str, titulo: str, autor: str, ano: int, preco: float) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(id_livros)}, {"$set": {"Titulo": titulo, "Autor": autor, "Ano": ano, "Preco": preco}})
            if result.modified_count:
                print(f"Person {id_livros} atualizou titulo {titulo} , autor {autor} , ano {ano} e preco {preco}")
            else:
                print(f"No person found with id {id_livros}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating person: {error}")
            return None

    def delete_livros(self, id_livros: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(id_livros)})
            if result.deleted_count:
                print(f"Person {id_livros} deleted")
            else:
                print(f"No person found with id {id_livros}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting person: {error}")
            return None