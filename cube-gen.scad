module Cube () {
polyhedron (
points = [
[0.5, 0.5, 0.0],
[-0.5, 0.5, 0.0],
[-0.5, -0.5, 0.0],
[0.5, -0.5, 0.0],
[0.5, 0.5, 1.0],
[0.5, -0.5, 1.0],
[-0.5, -0.5, 1.0],
[-0.5, 0.5, 1.0],
],
faces = [
[0, 3, 2, 1],
[4, 7, 6, 5],
[0, 1, 7, 4],
[0, 4, 5, 3],
[1, 2, 6, 7],
[3, 5, 6, 2],
]);
}

Cube ();
