"""Works but gives incorrect answer

TODO: #2 Code is too clunky. Extract variables.
TODO: #1 Answer is incorrect
"""
import sys
import math

class Cube:
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self) -> str:
        return "Cube("+str(self.side)+")"
    
    def on_the_surface_and_not_edge(self, x,y,z):
        """x,y,z circle if 0; else opposite"""

        if x<0 or y<0 or z<0:
            raise ValueError("Coordinates start from (0,0,0) hence can't be negative")
        planes = []
        if x==0 and (y>0 and z>0) :
            planes.append("yz")
        elif x==self.side and (y<self.side and z<self.side):
            planes.append("zy")
        elif y==0 and (x>0 and z>0):
            planes.append("xz")
        elif y==self.side and (x<self.side and z<self.side):
            planes.append("zx")
        elif z==0 and (x>0 and y>0):
            planes.append("xy")
        elif z==self.side and (x<self.side and y<self.side):
            planes.append("yx")
        else:
            return False
        if len(planes) == 1:
            return planes[0]
        else:
            return False

def is_3d_point(points: tuple):
    if not isinstance(points, tuple):
        raise TypeError("points must be tuples")
    elif not all( isinstance(point, (int,float)) for point in points ):
        raise TypeError("Use a real number")
    elif not len(points)==3:
        raise ValueError("3d distance so input coordinates with 3 points")
    else:
        return True


def distance_3d(point_1: tuple, point_2: tuple):
    all([is_3d_point(point_1), is_3d_point(point_2)])
    
    dist = 0
    for axis in range(len(('x', 'y', 'z'))):
        dist += abs(point_1[axis] - point_2[axis])**(2)
    
    dist = dist**(0.5)
    return dist

def midpoint_3d(point_1: tuple, point_2: tuple):
    all([is_3d_point(point_1), is_3d_point(point_2)])
    return ((point_1[0]+point_2[0])/2,
            (point_1[1]+point_2[1])/2,
            (point_1[2]+point_2[2])/2,)


cube_with_honey = Cube(10)


while True:
    try:
        honey_points_count = 3 # int(input("Enter no. of points of honey (integer): "))
        break
    except ValueError as v:
        print(v, file=sys.stderr)

honey_points = [(1,1,10), (2,1,10), (0,1,9)]

# print("""Enter the coordinates of the point one by one, in comma separated form.
# For example:
# 1. (0,0,0)
# 2. (10,10,10)""")
# for ii in range(honey_points_count): # input honey_point_coordinate (s)
#     while True:
#         try:
#             honey_point_coordinate = eval(input("Enter coordinate "+str(ii+1)+':'))
#             if is_3d_point(honey_point_coordinate):
#                 # the above function would throw error if false
#                 pass
#             if (not cube_with_honey.on_the_surface_and_not_edge(*honey_point_coordinate)):
#                 print("Point must be on the surface of the cube", file=sys.stderr)
#                 continue
#             elif ("xy" == cube_with_honey.on_the_surface_and_not_edge(*honey_point_coordinate)):
#                 print("It cannot be on the below surface", file=sys.stderr)
#                 continue
#             honey_points.append(honey_point_coordinate)
#             break
#         except Exception as e:
#             print( str(type(e))[8:-2] + ': ' + str(e) )


total_distance = 0
axis_mapping_dict = dict(zip('xyz', range(3)))

for jj in range(len(honey_points)-1):
    if cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj]) == cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]):
        # c is the arc
        print('here 1')
        print( distance_3d(honey_points[jj], honey_points[jj+1]) / 2*math.sin(math.radians(60/2)))
        c = (60/360) * (2*math.pi*( distance_3d(honey_points[jj], honey_points[jj+1]) / 2*math.sin(math.radians(60/2)) ) )
        
    elif (set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj])).intersection( (set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))))):
        # c is the shortest distance through surface (adjacent sides)
        print("here 2")
        
        common_axis = (set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj])).intersection( (set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))) )).pop()
        # print(common_axis)
        
        
        intersectional_axis = set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj])).intersection(set(
                                  cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))).pop()
        
        first_edgepoint = []
        second_edgepoint = []
        if cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]).startswith(
                (set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj]))
                - set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))).pop()):
            for nn in range(3):
                if nn == axis_mapping_dict[(set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj]))- set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))).pop()]:
                    first_edgepoint.append(0)

                else:
                    first_edgepoint.append(honey_points[jj][nn])
        else:
            for nn in range(3):
                if nn == axis_mapping_dict[intersectional_axis]:
                    first_edgepoint.append(cube_with_honey.side - honey_points[jj][nn])
                else:
                    first_edgepoint.append(honey_points[jj][nn])

        if cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj]).startswith(
                (set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))
                - set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj]))).pop()):
            for nn in range(3):
                if nn == axis_mapping_dict[(set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1]))- set(cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj]))).pop()]:
                    second_edgepoint.append(0)

                else:
                    second_edgepoint.append(honey_points[jj+1][nn])
        else:
            for nn in range(3):
                if nn == axis_mapping_dict[intersectional_axis]:
                    second_edgepoint.append(cube_with_honey.side - honey_points[jj+1][nn])
                else:
                    second_edgepoint.append(honey_points[jj+1][nn])
        
        first_edgepoint = tuple(first_edgepoint)
        second_edgepoint = tuple(second_edgepoint)




        edge_midpoint = midpoint_3d(first_edgepoint, second_edgepoint)

        c = distance_3d(honey_points[jj], edge_midpoint) + distance_3d(edge_midpoint, honey_points[jj+1])
    
    else:
        # c is the shortest dostamce between 2 points on opposite sides
        print("here 3")

        plane_1 = cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj])
        plane_2 = cube_with_honey.on_the_surface_and_not_edge(*honey_points[jj+1])
        print(plane_1)
        print(plane_2)
        print(set('xyz') - (set(plane_1).intersection(set(plane_2))))
        uninvolved_axis = (set('xyz') - (set(plane_1).intersection(set(plane_2)))).pop()
        uninvolved_planes = list( {'yx', 'xz', 'zx', 'yz', 'zy'} - { plane_1, plane_2} )
        lengths = []
        for plane in uninvolved_planes:

            inter_axis = set(plane).intersection(set(plane_1).intersection(set(plane_2))).pop()
            breadth_difference = abs(honey_points[jj][axis_mapping_dict[inter_axis]] - honey_points[jj+1][axis_mapping_dict[inter_axis]])
            
            run_through_axis = (set(plane_1) - set(plane)).pop()
            height_difference = (honey_points[jj][axis_mapping_dict[run_through_axis]]
                                 + cube_with_honey.side
                                 + honey_points[jj+1][axis_mapping_dict[run_through_axis]])
            lengths.append(math.sqrt(height_difference**2 + breadth_difference**2))
        c = min(lengths)
    
    print(c)
    total_distance += c
    

print("Total distance rounded to 2 decimal points:", round(total_distance, 2))
