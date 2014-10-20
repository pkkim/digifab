height = sin (54) * tan (acos (sin (54) * 2 / sqrt (3)));
// radius = height / (tan (asin (height)));
big_radius = 1 / (2 * sin (36));
small_radius = sqrt (pow (big_radius, 2) - (1/4));
//side_height = sqrt (3) / 2 * sin (acos (height * (1 - sin (54))));
//side_height = sqrt ((3/4) - pow((big_radius - small_radius), 2));
side_height = sqrt (3) / 2;
turn = 72;
rotation_axis = [0, 0, 1];

module wedge (x) {
    turn = 72;

    one = [1, 0, 0];
    top_points = [
	big_radius * [sin (54), cos (54), 0],
	big_radius * [sin (54), -cos (54), 0],
	[0, 0, 0],
	[0, 0, height]
    ];
    top_faces = [
	[3, 0, 1],
	[3, 2, 0],
	[3, 1, 2],
	[2, 1, 0]
    ];
    polyhedron (
	points = top_points,
	faces = top_faces
    );
}

module top (x) {
    echo (side_height);
    translate ([0, 0, side_height] / 2) {
	union () {
	    wedge (x);
	    rotate (a = turn, v = rotation_axis) { wedge (x); };
	    rotate (a = 2 * turn, v = rotation_axis) { wedge (x); };
	    rotate (a = 3 * turn, v = rotation_axis) { wedge (x); };
	    rotate (a = 4 * turn, v = rotation_axis) { wedge (x); };
	}
    }
}

module bottom (x) {
    rotate (a = turn/2, v = rotation_axis) {
	mirror ([0, 0, 1]) {
	    top (x);
	}
    }
}

hull () {
    top (2);
    bottom (2);
};

