import math

phi = (1 + math.sqrt(5))/2
iphi = 1/phi


class Point:
    """A single vertex"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point (self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return Point (self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def mult(self, factor):
        factorFloat = float(factor)
        return Point (self.x * factorFloat,
                      self.y * factorFloat,
                      self.z * factorFloat)

    def norm(self):
        return math.sqrt( self.x**2 + self.y**2 + self.z**2)

    def stlStr(self):
        return ("[{}, {}, {}]"
                .format(self.x, self.y, self.z))

    def __str__(self):
        return ("[{}, {}, {}]"
                .format(self.x, self.y, self.z))
                                     
class Triangle:
    """A single triangle. Vertices are in clockwise order from outside."""
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    @staticmethod
    def fromPointList(points):
        print points
        assert len(points) == 3
        p1, p2, p3 = points
        return Triangle(p1, p2, p3)

    def normal(self):
        """Returns non-unit normal vector to triangle, using technique at
        http://math.stackexchange.com/questions/305642/how-to-find-surface-normal-of-a-triangle"""
        v = self.p2 - self.p1
        w = self.p3 - self.p1

        nX = (v.y * w.z) - (v.z * w.y)
        nY = (v.z * w.x) - (v.x * w.z)
        nZ = (v.x * w.y) - (v.y * w.x)

        return [nX, nY, nZ]

    def stlString(self):
        """Outputs a single "facet...endfacet" for STL format."""
        return (("facet normal {normal[0]:e}, {normal[1]:e}, {normal[2]:e}\n"
                "    outer loop\n"
                "        vertex {p1.x:e} {p1.y:e} {p1.z:e}\n"
                "        vertex {p2.x:e} {p2.y:e} {p2.z:e}\n"
                "        vertex {p3.x:e} {p3.y:e} {p3.z:e}\n"
                "    endloop\n"
                "endfacet\n")
                .format(normal=self.normal(),
                        p1=self.p1, p2=self.p2, p3=self.p3))

    def __str__(self):
        return ("(p1: {}, p2: {}, p3: {})"
                .format(p1.str(), p2.str(), p3.str()))

    @staticmethod
    def triangulate(vertices, indices):
        """Takes vertices of a polygon and splits polygon into triangles."""
        print indices
        assert (len(indices) > 2)
        length = len(indices)
        if length == 3:
            return [Triangle(vertices[indices[0]],
                             vertices[indices[1]],
                             vertices[indices[2]])]
        if length > 3:
            print range(length)[1:-1]
            return [Triangle (vertices[indices[0]],
                              vertices[indices[i]],
                              vertices[indices[i+1]])
                    for i in (range(length)[1:-1])]
        else:
            raise Error ("Need more than two indices.")

class PlatonicSolid:
    """A platonic solid."""
    Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron = range (5)

    def generateData(self, shape, scale):
        if shape == PlatonicSolid.Tetrahedron:
            unscaledVertices = [Point(-math.sqrt(3)/2.0, -0.5, 0),
                        Point(math.sqrt(3)/2, -0.5, 0),
                        Point(0, 1.0, 0),
                        Point(0, 0, math.sqrt(2))]
            vertices = map(lambda p: p.mult(scale/math.sqrt(3)),
                           unscaledVertices)
            faces = [[0, 2, 1],
                     [0, 3, 2],
                     [0, 1, 3],
                     [1, 2, 3]]
            name = "Tetrahedron"
        elif shape == PlatonicSolid.Cube:
            unscaledVertices = [Point(0.5, 0.5, 0),
                                Point(-0.5, 0.5, 0),
                                Point(-0.5, -0.5, 0),
                                Point(0.5, -0.5, 0),
                                Point(0.5, 0.5, 1),
                                Point(0.5, -0.5, 1),
                                Point(-0.5, -0.5, 1),
                                Point(-0.5, 0.5, 1)]
            vertices = map(lambda p: p.mult(scale), unscaledVertices)
            faces = [[0, 3, 2, 1],
                     [4, 7, 6, 5],
                     [0, 1, 7, 4],
                     [0, 4, 5, 3],
                     [1, 2, 6, 7],
                     [3, 5, 6, 2]]
            name = "Cube"
        elif shape == PlatonicSolid.Octahedron:
            unscaledVertices = [Point(0.5, 0.5, 0),
                                Point(-0.5, 0.5, 0),
                                Point(-0.5, -0.5, 0),
                                Point(0.5, -0.5, 0),
                                Point(0, 0, math.sqrt(2)/2.0),
                                Point(0, 0, -math.sqrt(2)/2.0)]
            vertices = map(lambda p: p.mult(scale/math.sqrt(3)),
                           unscaledVertices)
            faces = [[0, 1, 4],
                     [1, 2, 4],
                     [2, 3, 4],
                     [3, 0, 4],
                     [0, 3, 5],
                     [3, 2, 5],
                     [2, 1, 5],
                     [1, 0, 5]]
            name = "Octahedron"
        elif shape == PlatonicSolid.Dodecahedron:
            unscaledVertices = [Point(0, -iphi, phi),
                        Point(1.0, -1.0, 1.0),
                        Point(iphi, -phi, 0),
                        Point(-iphi, -phi, 0),
                        Point(-1.0, -1.0, 1.0),
                        Point(0, iphi, phi),
                        Point(phi, 0, iphi),
                        Point(1.0, -1.0, -1.0),
                        Point(-1.0, -1.0, -1.0),
                        Point(-phi, 0, iphi),
                        Point(1.0, 1.0, 1.0),
                        Point(phi, 0, -iphi),
                        Point(0, -iphi, -phi),
                        Point(-phi, 0, -iphi),
                        Point(-1.0, 1.0, 1.0),
                        Point(iphi, phi, 0),
                        Point(1.0, 1.0, -1.0),
                        Point(0, iphi, -phi),
                        Point(-1.0, 1.0, -1.0),
                        Point(-iphi, phi, 0)]
            vertices = map(lambda p: p.mult(scale/(2/phi)),
                           unscaledVertices)
            faces = [[0, 4, 3, 2, 1],
                     [0, 1, 6, 10, 5],
                     [0, 5, 14, 9, 4],
                     [4, 9, 13, 8, 3],
                     [3, 8, 12, 7, 2],
                     [2, 6, 11, 6, 1],
                     [8, 13, 18, 17, 12],
                     [7, 12, 17, 16, 11],
                     [6, 11, 16, 15, 10],
                     [5, 10, 15, 19, 14],
                     [9, 14, 19, 18, 13],
                     [15, 16, 17, 18, 19]]
            name = "Dodecahedron"
        elif shape == PlatonicSolid.Icosahedron:
            unscaledVertices = [Point(-1.0, 0, -phi),
                        Point(0, -phi, -1.0),
                        Point(1.0, 0, -phi),
                        Point(-phi, -1.0, 0),
                        Point(phi, -1.0, 0),
                        Point(0, phi, -1.0),
                        Point(0, -phi, 1.0),
                        Point(phi, 1.0, 0),
                        Point(-phi, 1.0, 0),
                        Point(-1.0, 0, phi),
                        Point(1.0, 0, phi),
                        Point(0, phi, 1.0)]
            vertices = map(lambda p: p.mult(scale/2),
                           unscaledVertices)
            faces = [[0, 2, 1],
                     [0, 1, 3],
                     [1, 2, 4],
                     [2, 0, 5],
                     [5, 0, 8],
                     [0, 3, 8],
                     [3, 1, 6],
                     [1, 4, 6],
                     [4, 2, 7],
                     [2, 5, 7],
                     [6, 4, 10],
                     [4, 7, 10],
                     [7, 5, 11],
                     [5, 8, 11],
                     [8, 3, 9],
                     [3, 6, 9],
                     [6, 10, 9],
                     [7, 11, 10],
                     [8, 9, 11],
                     [9, 10, 11]]
            name = "Icosahedron"
        else:
            raise ValueError("Shape must be a Tetrahedron, Cube, Octahedron,"
                             "Dodecahedron, or Icosahedron "
                             "(int values 0 through 4)")
        
        return (vertices, faces, name)

    def generateScad(self, shape, scale):
        vertices, faces, name = self.generateData(shape, scale)

        output = ("module {} () {{\n"
                  "polyhedron (\n"
                  "points = [\n").format(name)
        
        for vertex in vertices:
            output += Point.stlStr(vertex) + ",\n"

        output += ("],\n"
                   "faces = [\n")

        for face in faces:
            output += str(face) + ",\n"

        output += ("]);\n"
                   "}}\n"
                   "\n"
                   "{} ();".format(name))
        return output
    
    def generateStl(self, shape, scale):
        vertices, faces, name = self.generateData(shape, scale)

        triangles = []
        for face in faces:
            triangles += Triangle.triangulate(vertices, face)

        output = "solid {}\n".format(name)
        for triangle in triangles:
            output += triangle.stlString()
        output += "endsolid {}".format(name)
        return output
