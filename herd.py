from dinosaurs import Dinosaur
class Herd:
    def __init__(self):
        self.Dinosaur = []
        self.create_herd()
    def create_herd(self):
        dino1 = Dinosaur("Jax", 25)
        dino2 = Dinosaur("Luka", 25)
        dino3 = Dinosaur("Frankie", 25)
        self.Dinosaur.append(dino1)
        self.Dinosaur.append(dino2)
        self.Dinosaur.append(dino3)
