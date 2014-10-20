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

    def __str__(self):
        return ("({}, {}, {})"
                .format(self.x, self.y, self.z))
                                     
class Triangle:
    """A single triangle. Vertices are in clockwise order from outside."""
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

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
        return [Triangle (vertices[indices[i]],
                          vertices[indices[i+1]],
                          vertices[indices[k]])
                for i in range(length) for k in range(length)
                if ((k == (i + 2)) or (i+2 == length and k == 0))]

class PlatonicSolid:
    """A platonic solid, consisting of some triangles."""
    Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron = range (5)

    def generate(self, shape, scale):
        triangles = []
    
        if shape == PlatonicSolid.Tetrahedron:
            vertices = []
            faces = []
            name = "Tetrahedron"
        elif shape == PlatonicSolid.Cube:
            vertices = [Point(0.5, 0.5, 0),
                        Point(-0.5, 0.5, 0),
                        Point(-0.5, -0.5, 0),
                        Point(0.5, -0.5, 0),
                        Point(0.5, 0.5, 1),
                        Point(0.5, -0.5, 1),
                        Point(-0.5, -0.5, 1),
                        Point(-0.5, 0.5, 1)]
            faces = [[0, 1, 2, 3],
                     [4, 5, 6, 7],
                     [0, 4, 7, 1],
                     [0, 3, 5, 4],
                     [1, 7, 6, 2],
                     [3, 2, 6, 5]]
            name = "Cube"
        elif shape == PlatonicSolid.Octahedron:
            vertices = [Point(0.5, 0.5, 0),
                        Point(-0.5, 0.5, 0),
                        Point(-0.5, -0.5, 0),
                        Point(0.5, -0.5, 0),
                        Point(0, 0, sqrt(2)/2),
                        Point(0, 0, -sqrt(2)/2)]
	    faces = [[0, 1, 4],
                     [1, 2, 4],
                     [2, 3, 4],
                     [3, 0, 4],
                     [0, 3, 5],
                     [3, 2, 5],
                     [2, 1, 5],
                     [1, 0, 5]]
        elif shape == PlatonicSolid.Dodecahedron:
            vertices = []
            faces = []
            name = "Dodecahedron"
        elif shape == PlatonicSolid.Icosahedron:
            vertices = []
            faces = []
            name = "Icosahedron"
        else:
            raise ValueError("Shape must be a Tetrahedron, Cube, Octahedron,"
                             "Dodecahedron, or Icosahedron "
                             "(int values 0 through 4)")

        for face in faces:
            print face
            triangles += Triangle.triangulate(vertices, face)

        output = "solid {}\n".format(name)
        for triangle in triangles:
            output += triangle.stlString()
        output += "endsolid {}".format(name)
        return output