module dodecahedron (x) {
    phi = (1 + (sqrt (5)))/2;
    term_one = 1 / phi;
    term_two = phi;

    cube_points = [
	[1, 1, 1],
	[-1, 1, 1],
	[1, -1, 1],
	[-1, -1, 1],
	[1, 1, -1],
	[-1, 1, -1],
	[1, -1, -1,],
	[-1, -1, -1]
    ];

    noncube_points = [
	[0, term_one, term_two],
	[0, -term_one, (term_two)],
	[0, term_one, -(term_two)],
	[0, -term_one, -(term_two)],

	[term_one, (term_two), 0],
	[-term_one, (term_two), 0],
	[term_one, -(term_two), 0],
	[-term_one, -(term_two), 0],

	[term_two, 0, (term_one)],
	[-term_two, 0, (term_one)],
	[term_two, 0, -(term_one)],
	[-term_two, 0, -(term_one)],
    ];
    
    scale ([x, x, x]) {
union () {
	hull () {
	    cube (size=2, center=true);
	    polyhedron (
		points = noncube_points,
		faces = [
		    [0, 1, 2],
		    [3, 4, 5],
		    [6, 7, 8],
		    [9, 10, 11]
		]);
	}
    }
}
}

dodecahedron (3);