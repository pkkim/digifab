#!/usr/bin/python

from GeneratePolyhedronStl import Point
import sys
import math

class Bond:
    def __init__(self, atom1, atom2, count):
        self.atom1 = atom1
        self.atom2 = atom2
        self.count = count

    def __str__(self):
        return "({}, {}, {})".format(atom1, atom2, count)

    def toScad(self, resolution, totalScale, radiusScale):
        difference = self.atom2.pos - self.atom1.pos

        # Compute rotation of cylinder from one pointed upward to one pointed at
        # DIFFERENCE to be [0, b, c].
        # Taken from bit.ly/1ziiWyc
        length = difference.norm()
        b = math.degrees(math.acos(difference.z/length))
        if difference.x == 0:
            c = 90
        elif difference.x > 0:
            c = math.degrees(math.atan(difference.y/difference.x))
        else:
            c = math.degrees(math.atan(difference.y/difference.x)) + 180

        radius = radiusScale * self.count
        return (("translate ([{x}, {y}, {z}])"
                 "{{rotate ([0, {b}, {c}])"
                 "{{cylinder (h={length}, r={radius});}}}}")
                .format(x=self.atom1.pos.x*totalScale,
                        y=self.atom1.pos.y*totalScale,
                        z=self.atom1.pos.z*totalScale,
                        b=b, c=c,
                        length=length*totalScale,
                        radius=radius))

class Atom:
    def __init__(self, pos, element):
        self.pos = pos
        self.element = element

    def __str__(self):
        return "{}, position: {}".format(self.element, self.pos)

    def toScad(self, resolution, totalScale, size):
        """Returns SCAD representation of atom."""
        scaledPosition = self.pos.mult(totalScale)
        return (("translate ([{x}, {y}, {z}])"
                 "{{sphere (r={radius}, $fn={resolution});}}")
                .format(x=scaledPosition.x, y=scaledPosition.y,
                        z=scaledPosition.z, radius=size,
                        resolution=resolution))
                        

class Molecule:
    def __init__(self, atoms, bonds, name):
        self.atoms = atoms
        self.bonds = bonds
        self.name = name

    def __str__(self):
        return ("{}: Atoms ({}), Bonds ({})"
                .format(self.name, self.atoms, self.bonds))

#    def toScad(self):

def parseCountLine(line):
    words = line.split()
    atoms = int(words[0])
    bonds = int(words[1])
    return (atoms, bonds)

def parseAtomLine(line):
    words = line.split()
    assert (words[3].isalpha())
    return Atom(Point(float(words[0]),
                      float(words[1]),
                      float(words[2])),
                words[3])

def parseBondLine(line, atoms):
    words = line.split()
    return Bond(atoms[int(words[0])-1],
                atoms[int(words[1])-1],
                int(words[2]))

def parseFile(f):
    name = f.readline()

    atoms = []
    bonds = []

    line = ""
    while (not line.endswith("V2000")):
        line = f.readline().strip("\n\r")

    atomCount, bondCount = parseCountLine(line)

    for i in range(atomCount):
            atoms.append(parseAtomLine(f.readline()))

    for i in range(bondCount):
        bonds.append(parseBondLine(f.readline(), atoms))

    assert (f.readline().strip("\n\r") == "M  END")
    return Molecule(atoms, bonds, name)

if __name__=="__main__":
    filename = sys.argv[1]
    scale = 2
    resolution = 10
    
    with open(filename, "r") as file:
        mol = parseFile(file)

    print "union () {"
    for atom in mol.atoms:
        print atom.toScad(resolution, scale, 1)

    for bond in mol.bonds:
        print bond.toScad(resolution, scale, 0.3)

    print "}"
