import open3d as o3d
import numpy as np
import pyvista as pv
import pandas as pd
from io import StringIO


def convert_xyz_to_array(filename, scale=10):
    file_text = open(filename, encoding="cp1251").read().replace(' ', ',')
    point_cloud = np.loadtxt(StringIO(file_text), skiprows=1, delimiter=',', usecols=(1, 2, 3))
    ijk = np.loadtxt(StringIO(file_text), skiprows=1, delimiter=',', usecols=(4, 5, 6))
    # print(point_names)
    origin_data = np.around(point_cloud, decimals=3)
    visualisation_data = origin_data / scale
    return [origin_data, ijk, visualisation_data]


def plotting(data, flag='p'):
    pl = pv.Plotter()
    pl.add_mesh(data)
    pl.show()


def lod_mesh_export(mesh, lods, extension, path):
    mesh_lods = {}
    for i in lods:
        mesh_lod = mesh.simplify_quadric_decimation(i)
        o3d.io.write_triangle_mesh(path + "lod_" + str(i) + extension, mesh_lod)
        mesh_lods[i] = mesh_lod
    print("generation of " + str(i) + " LoD successful")
    return mesh_lods


if __name__ == "__main__":
    origin_data = convert_xyz_to_array('T:\\my\\WORK\\cad_creator\\test_data\\data.xyz', 15)
    polydata = o3d.geometry.PointCloud()
    polydata.points = o3d.utility.Vector3dVector(origin_data[2])
    polydata.normals = o3d.utility.Vector3dVector(origin_data[1])

    poisson_mesh = \
        o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(polydata, depth=8, width=0, scale=1.1,
                                                                  linear_fit=False)[0]
    bbox = polydata.get_axis_aligned_bounding_box()
    p_mesh_crop = poisson_mesh.crop(bbox)

    o3d.io.write_triangle_mesh("p_mesh_c.ply", p_mesh_crop)

    reader = pv.get_reader("p_mesh_c.ply")
    mesh = reader.read()
    mesh.plot()
    # lines = np.array([[2, j, j+1] for j in range(0, 126)])
    # print(lines.shape)
    # polydata.lines = lines
    # plotting(polydata)
