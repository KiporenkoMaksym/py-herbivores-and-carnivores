class Animal:

    alive = []

    def __init__(self, name:str, health=100, hidden=False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        if health > 0:
            Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> bool:
        self.hidden = not self.hidden
        return self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if (herbivore in Animal.alive
        and isinstance(herbivore, Herbivore)
        and not herbivore.hidden):
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.health = 0
                Animal.alive.remove(herbivore)
