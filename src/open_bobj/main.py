import sys

import bpy


if len(sys.argv) < 5:
    raise ValueError("Please provide the path to the OBJ file as an argument.")


# Remove the default cube, camera and light
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type='LIGHT')
bpy.ops.object.delete()
bpy.ops.object.select_by_type(type='CAMERA')
bpy.ops.object.delete()


for i in range(4, len(sys.argv)):
    obj_file_path = sys.argv[i]

    # Import the OBJ file
    bpy.ops.import_scene.obj(filepath=obj_file_path)
    # Update the scene to reflect the changes
    bpy.context.view_layer.update()
