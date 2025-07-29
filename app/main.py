class Animal:

    alive = []

    def __init__(self, name:str, health=100, hidden=False) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)

    def take_damage(self, damage):
        if self.health <= 0:
            return

        self.health -= damage
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def is_alive(self):
        return self.health > 0

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
            herbivore.take_damage(50)
