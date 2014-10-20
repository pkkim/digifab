module myOctahedron (x) {
    scale ([x, x, x]) {
	polyhedron (
	    points = [
		// middle points, counterclockwise
		[0.5, 0.5, 0],
		[-0.5, 0.5, 0],
		[-0.5, -0.5, 0],
		[0.5, -0.5, 0],
		// top and bottom
		[0, 0, sqrt(2)/2],
		[0, 0, -sqrt(2)/2],
	    ],
	    faces = [
		[0, 1, 4],
		[1, 2, 4],
		[2, 3, 4],
		[3, 0, 4],
		[0, 3, 5],
		[3, 2, 5],
		[2, 1, 5],
		[1, 0, 5]
	    ]);
    }
}

myOctahedron(1);