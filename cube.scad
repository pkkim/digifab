module myCube (x) {
    scale ([x, x, x]) {
	polyhedron (
	    points = [
		// bottom points, clockwise
		[0.5, 0.5, 0],
		[-0.5, 0.5, 0],
		[-0.5, -0.5, 0],
		[0.5, -0.5, 0],
		// top points, clockwise
		[0.5, 0.5, 1],
		[0.5, -0.5, 1],
		[-0.5, -0.5, 1],
		[-0.5, 0.5, 1]
	    ],
	    faces = [
		[0, 1, 2, 3],
		[4, 5, 6, 7],
		[0, 4, 7, 1],
		[0, 3, 5, 4],
		[1, 7, 6, 2],
		[3, 2, 6, 5]
	    ]);
    }
}

myCube(1);