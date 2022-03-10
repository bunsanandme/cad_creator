import open3d as o3d
import numpy as np
import pyvista as pv
import pandas as pd
from io import StringIO
from math import trunc


def convert_xyz_to_array(filename, scale=10):
    file_text = open(filename, encoding="cp1251").read().replace(' ', ',')
    point_cloud = np.loadtxt(StringIO(file_text), skiprows=1, delimiter=',', usecols=(1, 2, 3))
    ijk = np.loadtxt(StringIO(file_text), skiprows=1, delimiter=',', usecols=(4, 5, 6))
    # print(point_names)
    origin_data = np.floor(point_cloud)
    visualisation_data = origin_data / scale
    return [origin_data, ijk, visualisation_data]


def lines_from_points(points):
    """Given an array of points, make a line set"""
    poly = pv.PolyData()
    poly.points = points
    cells = np.full((len(points) - 1, 3), 2, dtype=np.int_)
    cells[:, 1] = np.arange(0, len(points) - 1, dtype=np.int_)
    cells[:, 2] = np.arange(1, len(points), dtype=np.int_)
    cells = np.append(cells, [2, len(points), 0])
    print(cells)
    poly.lines = cells
    return poly


if __name__ == "__main__":
    origin_data = convert_xyz_to_array('T:\\my\\WORK\\cad_creator\\test_data\\data.xyz', 15)[2][:]
    polydata = pv.PolyData(origin_data)
    pl = pv.Plotter()
    lines = np.array([[2, j, j+1] for j in range(0, 7)])
    lines = np.append(lines, [2, 7, 0])
    lines = np.append(lines, [[2, j, j + 1] for j in range(9, 15)])
    lines = np.append(lines, [2, 15, 9])
    lines = np.append(lines, [[2, j, j + 1] for j in range(17,20)])
    lines = np.append(lines, [2, 20, 17])
    lines = np.append(lines, [[2, j, j + 1] for j in range(23, 41)])
    lines = np.append(lines, [2, 41, 23])

    polydata.lines = lines
    pl.add_mesh(polydata)
    pl.show()

