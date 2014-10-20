module myTetrahedron (x) {
    scale ([x, x, x]) {
    polyhedron (
	points = [
	    [-sqrt(3)/2, -0.5, 0],
	    [sqrt(3)/2, -0.5, 0],
	    [0, 1, 0],
	    [0, 0, sqrt(2)]
	],
	faces = [
	    [0, 2, 1],
	    [0, 3, 2],
	    [0, 1, 3],
	    [1, 2, 3]
	]);
    }
}

myTetrahedron(1);

