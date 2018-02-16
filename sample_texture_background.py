import bpy, os, math, mathutils, sys, pdb
from PIL import Image

# camera.location = (7.4811, -6.5076, 5.3437) original camera position in blender
# (2.03913, -1.55791, 1.26075)
def render_resolution():
    bpy.context.scene.render.resolution_percentage = 100
    bpy.context.scene.render.resolution_x = 256
    bpy.context.scene.render.resolution_y = 256

def add_background(filepath):
    img = bpy.data.images.load(filepath)
    render_resolution()
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            space_data = area.spaces.active
            background = space_data.background_images.new()
            background.image = img
            space_data.show_background_images = True
            background.view_axis = 'CAMERA'
            break
    texture_name = os.path.splitext(filepath)[0]       
    texture = bpy.data.textures.new(texture_name, 'IMAGE')
    texture.image = img
    bpy.data.worlds['World'].active_texture = texture
    bpy.context.scene.world.texture_slots[0].use_map_horizon = True
    bpy.context.scene.world.use_sky_paper = True


def material_for_texture(fname):
    img = bpy.data.images.load(fname)

    tex = bpy.data.textures.new(fname, 'IMAGE')
    tex.image = img

    mat = bpy.data.materials.new(fname)
    mat.texture_slots.add()
    ts = mat.texture_slots[0]
    ts.texture = tex
    ts.texture_coords = 'ORCO'

    return mat


def point_camera_to_target(cam, object):
    # we want to point the camera towards the object.location(x,y,z), we rotate around the z-axis
    dx = object.location.x - cam.location.x
    dy = object.location.y - cam.location.y
    dz = object.location.z - cam.location.z
    xRad = (math.pi / 2.) + math.atan2(dz, math.sqrt(dy ** 2 + dx ** 2))
    zRad = math.atan2(dy, dx) - (math.pi / 2.)

    cam.rotation_euler = mathutils.Euler((xRad, 0, zRad), 'XYZ')


def rotate_camera_by_angle(camera, radians_angle, target_location):
    camera_location_rotation = mathutils.Matrix.Rotation(radians_angle, 4, 'Z')
    camera.location.rotate(camera_location_rotation)
    point_camera_to_target(camera, target_location)


def delete_and_add_correct_light_source(meshObjectPos):
    # deselect all
    bpy.ops.object.select_all(action='DESELECT')

    # selection % delete
    for obj in bpy.data.objects:
        if obj.type == 'LAMP':
            bpy.data.objects[obj.name].select = True
            bpy.ops.object.delete()

    # Add lamp object, type HEMI
    bpy.ops.object.lamp_add(type='HEMI', radius=1, view_align=False, location=(meshObjectPos.x, meshObjectPos.y, 10),
                            layers=(
                                True, False, False, False, False, False, False, False, False, False, False, False,
                                False,
                                False, False, False,
                                False, False, False, False))

def change_camera_location(camera_pos_index, camera_object, obj):
    if camera_pos_index == 1: # Default blender camera position 
        #camera_object.location = (2.03913, -1.55791, 1.26075)
        camera_object.location = (7.4811, -6.5076, 5.3437)
    elif camera_pos_index == 2:
        camera_object.location = (camera_object.location.x, camera_object.location.y, camera_object.location.z - 7)
    elif camera_pos_index == 3:
        camera_object.location = (camera_object.location.x, camera_object.location.y, camera_object.location.z + 7)
    else:
        camera_object.location = (obj.location.x + 5, obj.location.y + 5, 10)

def main(sys):
    bpy.context.scene.render.image_settings.file_format = 'JPEG'
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
  
    background_folder_path = argv[0]
    background_folder_full_path = os.path.abspath(background_folder_path)
    texture_folder_path = argv[1]
    texture_folder_full_path = os.path.abspath(texture_folder_path)
    saving_folder = argv[2]
    os.makedirs(saving_folder, exist_ok=True)
    camera = bpy.data.objects["Camera"]
    camera.rotation_mode = 'XYZ'

    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
            delete_and_add_correct_light_source(obj.location)
            bpy.context.scene.objects.active = obj

            degree = 150

            rotate_angle = math.radians(degree)
            number_of_frames = int(360 / degree)
            for background in os.listdir(background_folder_full_path):

                background_path = os.path.join(background_folder_full_path, background)
                add_background(background_path)
                background_name = os.path.splitext(background)[0]
                

                for file in os.listdir(texture_folder_full_path):
                    fname = os.path.join(texture_folder_full_path, file)
                    texture_name = os.path.splitext(file)[0]

                    if (texture_name == "white" and background_name != "black") or (background_name == "black" and texture_name != "white"):
                        continue
                    obj = bpy.context.active_object
                    mat = material_for_texture(fname)
                    if len(obj.data.materials) < 1:
                        obj.data.materials.append(mat)
                    else:
                        obj.data.materials[0] = mat
                    for camera_pos_index in range(1, 5):
                        change_camera_location(camera_pos_index, camera, obj)
                        
                        for x in range(1, number_of_frames):
                            rotate_camera_by_angle(camera, rotate_angle, obj)
                            bpy.context.scene.render.filepath = os.path.join(saving_folder,("%s/%s%s%sCameraPose%dFrame%d.jpeg") % (obj.name, obj.name, background_name, texture_name, camera_pos_index, x))
                            bpy.ops.render.render(write_still=True, use_viewport=True)

if __name__ == "__main__":
    main(sys)