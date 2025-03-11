import math

# A Euclidean Vector in 3 dimensions.
# Why am I using 3-dimensional vectors in 2-dimensions?
# Because fuck you, that's why.
# Assumes a right-handed coordinate system.
class Vector3:
    #
    def __init__(self, x=0, y=0, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z

    # Negate all the Vector3's components.
    def invert(self) -> None:
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    # math dot SQUIRT.
    # Returns the (distance, length, bigness, etc.) of the vector.
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Can call if the need to compare two magnitudes arises.
    # i.e. if "magnitude_1 > magnitude2".
    def square_magnitude(self):
        return self.x**2 + self.y**2 + self.z**2

    # Transforms the Vector3 into a unit vector (of magnitude one).
    # I almost wrote "of magnitude zero," that would've been hilarious.
    def normalize(self):
        magnitude = self.magnitude()
        # Voodoo case where magnitude is negative?
        # AKA the complex plane returns from College Algebra.
        # Fuck "Gerolamo Cardano," I guess.
        if magnitude > 0:
            self.x = self.x / magnitude
            self.y = self.y / magnitude
            self.z = self.z / magnitude
