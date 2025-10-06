class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets that belong to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner after validating it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)
