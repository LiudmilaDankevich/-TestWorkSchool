from petstore_api import PetstorePet


def test_pet():
    pet_db = {
        "id": 8,
        "category": {
            "id": 8,
            "name": "Roy"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 8,
                "name": "Roy"
            }
        ],
        "status": "available"
    }
    add_pet = PetstorePet()
    add_pet.create_pet(pet_db)
    get_pet = PetstorePet()
    get_pet.get_pet(pet_db)
    del_pet = PetstorePet()
    del_pet.delete_pet(pet_db)
    add_pet_2 = PetstorePet()
    add_pet_2.create_pet(pet_db)




