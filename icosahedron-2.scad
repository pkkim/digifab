module myIcosahedron (x) {
    phi = (1 + sqrt (5)) / 2;
    scale ([x, x, x]) {
	hull () {
	    polyhedron (
		points = [
		    [phi, 1, 0],
		    [0, phi, 1],
		    [1, 0, phi]
		],
		faces = [
		    [0, 1, 2]
		]);

	    polyhedron (
		points = [
		    [-phi, 1, 0],
		    [0, -phi, 1],
		    [1, 0, -phi]
		],
		faces = [
		    [0, 1, 2]
		]);

	    polyhedron (
		points = [
		    [phi, -1, 0],
		    [0, phi, -1],
		    [-1, 0, phi],
		],
		faces = [
		    [0, 1, 2]
		]);

	    polyhedron (
		points = [
		    [-phi, -1, 0],
		    [0, -phi, -1],
		    [-1, 0, -phi]
		],
		faces = [
		    [0, 1, 2]
		]);
	};
    }
}

myIcosahedron (2);