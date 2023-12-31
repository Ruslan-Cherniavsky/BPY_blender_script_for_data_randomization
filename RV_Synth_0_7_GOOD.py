import bpy
import random
import string
import numbers
import time
from bpy.types import Operator, AddonPreferences
from bpy.props import StringProperty, IntProperty, BoolProperty
from configparser import ConfigParser
import addon_utils
import os 


addon_utils.enable("RV Synth 0.7")

bl_info =  {
    "name" : "RV Synth 0.7",
    "author" : "Ruslan Cherniavsky",
    "version" : (1, 0),
    "blender" : (3, 2, 0),
    "location" : "View3d > Tool",
    "warnings" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
}


#-------------HENDLERS--------------

def random_rotation_cube_hendler(scene):
        
    x_rotation = 10
    y_rotation = 10
    z_rotation = 10

    x_location = 10  
    y_location = 10
    z_location = 10 
        
    object_name = 'Random Rotation Cube'
    change_position_cube(x_rotation, y_rotation, z_rotation, x_location, y_location, z_location, object_name)


def random_rotation_light_cube_hendler(scene):
        
    x_rotation = 35
    y_rotation = 35 
    z_rotation = 35 

    x_location = 2  
    y_location = 2
    z_location = 2 
        
    object_name = 'Random Rotation Light Cube'
    change_position_light_cube(x_rotation, y_rotation, z_rotation, x_location, y_location, z_location, object_name)

    
    

def random_text_hendler(scene):
    change_text() 

def random_fog_hendler(scene):
    random_fog() 

def random_light_point_hendler(scene):
    change_light_point() 

 
def random_background_frame_hendler(scene):
    change_random_background_frame()
    
    
def random_number_hendler(scene):
    change_number()
    
    
def random_upper_text_hendler(scene):
    change_text_upper()


def random_sky_texture_values_hendler(scene):
    print('W working - 1')

    random_sky_texture_values()
    
    
def file_path_hendler(scene):
    
    fp = bpy.context.scene.render.filepath
    current_values = 'VALUES_' + 'order_numb_' + str(bpy.context.scene.frame_current).zfill(5) + '_min_x_' + str(bpy.context.scene.render.border_min_x) + '_min_y_' + str(bpy.context.scene.render.border_min_y) + '_max_x_' + str(bpy.context.scene.render.border_max_x) + '_max_y_' + str(bpy.context.scene.render.border_max_y) + '_distance_' + str(bpy.data.objects["Camera Rig Distance"].location[1]) + '_frame_'
    

    if 'VALUES_' in fp:
        bpy.context.scene.render.filepath = fp.split('VALUES_')[0] + current_values
    else:
        bpy.context.scene.render.filepath =  fp + current_values



def camera_rig_center_hendler(scene):
    
    x_rotation_from = 0
    x_rotation_to =0
        
    y_rotation_from = 0
    y_rotation_to = 0
         
    z_rotation_from = rotation_from_default()
    z_rotation_to = rotation_to_default()
          
    x_location_from = 0 
    x_location_to = 0
           
    y_location_from = 0 
    y_location_to = 0
         
    z_location_from = 0
    z_location_to = 0
        
    object_name = 'Camera Rig Center'
        
    change_position_camera_rig(x_rotation_from, x_rotation_to, y_rotation_from, y_rotation_to, z_rotation_from, z_rotation_to, x_location_from, x_location_to, y_location_from, y_location_to, z_location_from, z_location_to, object_name)
    


def camera_rig_distance_hendler(scene):
    
    x_rotation_from = 0
    x_rotation_to =0
        
    y_rotation_from = 0
    y_rotation_to = 0
         
    z_rotation_from = 0
    z_rotation_to = 0
          
    x_location_from = 0 
    x_location_to = 0
          
    y_location_from = location_from_default()
    y_location_to = location_to_default()
         
    z_location_from = 0
    z_location_to = 0
        
    object_name = 'Camera Rig Distance'

    change_position_camera_rig_distance(x_rotation_from, x_rotation_to, y_rotation_from, y_rotation_to, z_rotation_from, z_rotation_to, x_location_from, x_location_to, y_location_from, y_location_to, z_location_from, z_location_to, object_name) 
        
#---------------- VALIDATIONS -----------------------------

def validations():
    #-----randome text valodation -----------
    random_text_hendler_validation_1 = None
    random_text_hendler_validation_1 = None
    random_text_hendler_validation_3 = None
    random_text_hendler_validation_4 = None
    
    try:
        random_text_hendler_validation_1 = bpy.context.scene.objects.get('Random Word')
        random_text_hendler_validation_2 = bpy.context.scene.objects.get('Random Word.001')
        random_text_hendler_validation_3 = bpy.context.scene.objects.get('Random Word.002')
        random_text_hendler_validation_4 = bpy.context.scene.objects.get('Random Word.003')
    except:
         print("An exception occurred")

    
    if(random_text_hendler_validation_1):
        bpy.app.handlers.frame_change_post.append(random_text_hendler)
        print('-------------- Random text hendler -------- working!')
    else:
        print('-------------- Random text hendler -------- not wirking!')
    
    #-----randome upper text validation -----------
    random_upper_text_hendler_validation_1 = None
    random_upper_text_hendler_validation_2 = None
    random_upper_text_hendler_validation_3 = None
    random_upper_text_hendler_validation_4 = None
    
    
    try:
        random_upper_text_hendler_validation_1 = bpy.context.scene.objects.get('Random Upper Word')
        random_upper_text_hendler_validation_2 = bpy.context.scene.objects.get('Random Upper Word.001')
        random_upper_text_hendler_validation_3 = bpy.context.scene.objects.get('Random Upper Word.002')
        random_upper_text_hendler_validation_4 = bpy.context.scene.objects.get('Random Upper Word.003')
    except:
         print("An exception occurred")
         
         
    if (random_upper_text_hendler_validation_1 or random_upper_text_hendler_validation_2 or random_upper_text_hendler_validation_3 or random_upper_text_hendler_validation_4):
        bpy.app.handlers.frame_change_post.append(random_upper_text_hendler)
        print('-------------------- Random upper word hendler -------- working!')
    else:
        print('-------------------- Random upper word hendler -------- not working!')
    
    #-----randome number validation -----------
    
    random_number_hendler_validation_1 = None
    random_number_hendler_validation_2 = None
    random_number_hendler_validation_3 = None
    random_number_hendler_validation_4 = None
    
    try:
        random_number_hendler_validation_1 = bpy.context.scene.objects.get('Random Number')
        random_number_hendler_validation_2 = bpy.context.scene.objects.get('Random Number.001')
        random_number_hendler_validation_3 = bpy.context.scene.objects.get('Random Number.002')
        random_number_hendler_validation_4 = bpy.context.scene.objects.get('Random Number.003')
    except:
         print("An exception occurred")
    
    if (random_number_hendler_validation_1 or random_number_hendler_validation_2 or random_number_hendler_validation_3 or random_number_hendler_validation_4):
        bpy.app.handlers.frame_change_post.append(random_number_hendler)
        print('-------------------- Random Number hendler -------- working!')
    else:
        print('-------------------- Random Number hendler -------- not working!')
        
    #---- Random Rotation Cube Validation -----------
    
    random_rotation_cube_validation = None
    
    try: 
        random_rotation_cube_validation = bpy.context.scene.objects.get('Random Rotation Cube')
    except:
         print("An exception occurred")
    
    if (random_rotation_cube_validation):
        bpy.app.handlers.frame_change_post.append(random_rotation_cube_hendler)
        print('-------------------- Random Rotation Cube hendler -------- working!')
    else:
        print('-------------------- Random Rotation Cube hendler -------- not working!')


            
    #---- Random Rotation Light Cube Validation -----------
    
    random_rotation_cube_validation = None
    random_rotation_light_cube_validation = None
    try: 
        random_rotation_light_cube_validation = bpy.context.scene.objects.get('Random Rotation Light Cube')
    except:
         print("An exception occurred")
    
    if (random_rotation_light_cube_validation):
        bpy.app.handlers.frame_change_post.append(random_rotation_light_cube_hendler)
        print('-------------------- Random Rotation Cube hendler -------- working!')
    else:
        print('-------------------- Random Rotation Cube hendler -------- not working!')
        
        
    #------random camera rig center validation
    
    camera_rig_center_hendler_validation = None
    
    try:
        camera_rig_center_hendler_validation = bpy.context.scene.objects.get('Camera Rig Center')
    except:
         print("An exception occurred")

    if (camera_rig_center_hendler_validation):  
        print(camera_rig_center_hendler_validation)
        
        bpy.app.handlers.render_post.append(camera_rig_center_hendler)
        bpy.app.handlers.frame_change_pre.append(camera_rig_center_hendler)
        print("frame change post is appendet! --------  camera_rig_center_hendler ------ working! ")
        
    else:
        print(camera_rig_center_hendler_validation)
        print("frame change post is not appendet! --------  camera_rig_center_hendler ------ not working! ")
            
    #------randome camera distance validatin ---------
    
    camera_rig_distance_hendler_validation = None
    
    try:  
        camera_rig_distance_hendler_validation = bpy.context.scene.objects.get('Camera Rig Distance')
    except:
         print("An exception occurred")

    if (camera_rig_distance_hendler_validation):  
        print(camera_rig_distance_hendler_validation)
 
        bpy.app.handlers.render_post.append(camera_rig_distance_hendler)
        bpy.app.handlers.frame_change_pre.append(camera_rig_distance_hendler)
        
        print("frame change post is appendet! --------  camera_rig_distance_hendler ------ working! ")
    else:
        print(camera_rig_center_hendler_validation)
        print("frame change post is not appendet! --------  camera_rig_distance_hendler ------ not working! ")
            
    #-----random frame on background plate validation -----------
    
    background_random_validation = None
    
    
    try:
        background_random_validation = bpy.context.scene.objects.get('Random Background Plane')
    except:
         print("An exception occurred")
        

        
    if (background_random_validation):
        bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
        print('-------------------- Random background hendler -------- working!')
    else:
        print('-------------------- Random background hendler -------- not working!')

    sun_intensity = 0

    try:
        sun_intensity = bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_intensity
    except:
         print("An exception occurred")


    if sun_intensity == 0.30000001192092896:
        bpy.app.handlers.frame_change_post.append(random_sky_texture_values_hendler)
    else:
        print("An exception occurred")








validations()

#*********** These validations determine hendlers depending on the objects and their parameters by current project scene.
#*********** you can see hendlers status in blender's console ---> Windows ---> Togle System Console


#-------------PANELS--------------

class RANDOM_TEXT_PANEL(bpy.types.Panel):   
    bl_label = "Random Text"
    bl_idname ="PT_RANDOM_TEXT_PANEL"
    bl_space_type ='VIEW_3D'   
    bl_region_type = 'UI'
    bl_category = 'RV Synth 0.6'
    
    def draw(self, context):  
        layout = self.layout
      
        row = layout.row()
        row.operator("text.randomization_operator", icon= 'OUTLINER_DATA_FONT')
        
        row = layout.row()
        row.operator("text.randomization_operator_upper", icon= 'BOLD')
        
        row = layout.row()
        row.operator("text.randomization_number_operator", icon= 'IPO_SINE')
        
        
        
class RANDOM_OBJECTS_PANEL(bpy.types.Panel):
    bl_label = "Random Objects"
    bl_idname ="PT_RANDOM_OBJECTS_PANEL"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RV Synth 0.6'
    
    def draw(self, context):
        layout = self.layout
      
        row = layout.row()
        row.operator("mesh.add_cube", icon= 'MESH_CUBE')
        
        row = layout.row()
        row.operator("mesh.add_plane", icon= 'RESTRICT_VIEW_ON')

        row = layout.row()
        row.operator("mesh.add_light_point", icon= 'RESTRICT_VIEW_ON')


        row = layout.row()
        row.operator("mesh.add_fog", icon= 'RESTRICT_VIEW_ON')





        
 
        
class CAMERA_RIG_PANEL(bpy.types.Panel):
    bl_label = "Camera Rig"
    bl_idname ="PT_CAMERA_RIG_PANEL"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RV Synth 0.6'
    
    def draw(self, context):
        layout = self.layout
      
        row = layout.row()
        row.operator("mesh.add_camera_rig", icon= 'CAMERA_DATA')
        
        layout.label(text="Randomization status:")
        
        row = layout.row()
        row.operator("mash.start_camera_rig_randomization", icon= 'TRIA_RIGHT')
        row.operator("mash.stop_camera_rig_randomization", icon= 'CANCEL')
        
        
        # layout.label(text="Render Camera Rig:")
        # row = layout.row()
        # row.operator("mash.camera_rig_render", icon= 'RENDER_ANIMATION')
        
        
        layout.label(text="Render Camera Rig Region:")
        
        row = layout.row()
        row.operator("mash.camera_rig_render_use_regeon", icon= 'RENDER_ANIMATION')
        
        layout.label(text="Render Camera Rig Crop Region:")
        
        row = layout.row()
        row.operator("mash.camera_rig_render_crop_regeon", icon= 'RENDER_ANIMATION')
        

        layout.label(text="Render Selected Camera Image:")

        row = layout.row()
        row.operator("mash.camera_rig_render_image", icon= 'FILE_IMAGE')

        layout.label(text="Add Random Background HD Video:")

        row = layout.row()
        row.operator("mesh.add_plane_85", icon= 'RESTRICT_VIEW_ON')
        row.operator("mesh.add_plane_50", icon= 'RESTRICT_VIEW_ON')
        row.operator("mesh.add_plane_400", icon= 'RESTRICT_VIEW_ON')



class WORLD_LIGHTS(bpy.types.Panel):
    bl_label = "World Light"
    bl_idname ="PT_WORLD_LIGHT"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'RV Synth 0.6'
    
    def draw(self, context):
        layout = self.layout
      
        
        layout.label(text="Create World Light Randomization:")
        
        row = layout.row()
        row.operator("mesh.add_random_world_lights", icon= 'TRIA_RIGHT')
        row.operator("mesh.add_random_world_night_lights", icon= 'TRIA_RIGHT')




        

#-------------RANDOMIZATION LOGIC--------------
        

        
def change_text():

    if bpy.data.objects['Random Word'].name: 
        bpy.data.objects['Random Word'].data.body = random.choice(string.ascii_letters)
    if bpy.data.objects['Random Word.001'].name:    
        bpy.data.objects['Random Word.001'].data.body = random.choice(string.ascii_letters)
    if bpy.data.objects['Random Word.002'].name:
        bpy.data.objects['Random Word.002'].data.body = random.choice(string.ascii_letters)
    if bpy.data.objects['Random Word.003'].name:
        bpy.data.objects['Random Word.003'].data.body = random.choice(string.ascii_letters)
        #i+=1
        
        
def change_text_upper():

    if bpy.data.objects['Random Upper Word'].name: 
        bpy.data.objects['Random Upper Word'].data.body = random.choice(string.ascii_uppercase)
    if bpy.data.objects['Random Upper Word.001'].name:    
        bpy.data.objects['Random Upper Word.001'].data.body = random.choice(string.ascii_uppercase)
    if bpy.data.objects['Random Upper Word.002'].name:
        bpy.data.objects['Random Upper Word.002'].data.body = random.choice(string.ascii_uppercase)
    if bpy.data.objects['Random Upper Word.003'].name:
        bpy.data.objects['Random Upper Word.003'].data.body = random.choice(string.ascii_uppercase)
        #i+=1
         
        
def change_number():

    if bpy.data.objects['Random Number'].name: 
        bpy.data.objects['Random Number'].data.body = str(random.randint(0,9))
    if bpy.data.objects['Random Number.001'].name:
        bpy.data.objects['Random Number.001'].data.body = str(random.randint(0,9))
    if bpy.data.objects['Random Number.002'].name:
        bpy.data.objects['Random Number.002'].data.body = str(random.randint(0,9))
    if bpy.data.objects['Random Number.003'].name:
        bpy.data.objects['Random Number.003'].data.body = str(random.randint(0,9))



def random_sky_texture_values():
    if bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_intensity == 0.30000001192092896:
        bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_size = random.uniform(0, 1 * 0.0174533)
        bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_elevation = random.uniform(0, 75 * 0.0174533)
        bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_rotation = random.uniform(0, 360 * 0.0174533)
        bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].ozone_density = random.uniform(0, 10)



def change_light_point():
    if bpy.data.objects['Random Light Point'].name: 
        bpy.data.objects['Random Light Point'].data.energy = random.uniform(0, 100)
    if bpy.data.objects['Random Light Point.001'].name:
        bpy.data.objects['Random Light Point.001'].data.energy = random.uniform(0, 100)
    if bpy.data.objects['Random Light Point.002'].name:
        bpy.data.objects['Random Light Point.002'].data.energy = random.uniform(0, 100)
    if bpy.data.objects['Random Light Point.003'].name:
        bpy.data.objects['Random Light Point.003'].data.energy = random.uniform(0, 100)




        
def change_random_background_frame():
    if bpy.data.materials['Material For Random Videos'].name: 
        bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_offset = random.randint(0, bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration)

        

def change_position_cube(x_rotation=0, y_rotation=0, z_rotation =0, x_location=0, y_location=0, z_location=0, object_name = 'Empty'):
    
    if x_rotation != 0: 
        bpy.data.objects[object_name].rotation_euler[0] = random.uniform(0, x_rotation * 0.0174533)
    if y_rotation != 0: 
        bpy.data.objects[object_name].rotation_euler[1] = random.uniform(0, y_rotation * 0.0174533)
    if z_rotation != 0:
        bpy.data.objects[object_name].rotation_euler[2] = random.uniform(0, z_rotation * 0.0174533)
            
    if x_location != 0:
        bpy.data.objects[object_name].location[0] = random.uniform(0, x_location)
    if y_location != 0:
        bpy.data.objects[object_name].location[1] = random.uniform(0, y_location)
    if z_location != 0:
        bpy.data.objects[object_name].location[2] = random.uniform(0, z_location)




def change_position_light_cube(x_rotation=0, y_rotation=0, z_rotation =0, x_location=0, y_location=0, z_location=0, object_name = 'Empty'):
    
    if x_rotation != 0: 
        bpy.data.objects[object_name].rotation_euler[0] = random.uniform(- x_rotation * 0.0174533, x_rotation * 0.0174533)
    if y_rotation != 0: 
        bpy.data.objects[object_name].rotation_euler[1] = random.uniform(- y_rotation * 0.0174533, y_rotation * 0.0174533)
    if z_rotation != 0:
        bpy.data.objects[object_name].rotation_euler[2] = random.uniform(- z_rotation * 0.0174533, z_rotation * 0.0174533)
            
    if x_location != 0:
        bpy.data.objects[object_name].location[0] = random.uniform( - x_location, x_location)
    if y_location != 0:
        bpy.data.objects[object_name].location[1] = random.uniform( - y_location, y_location)
    if z_location != 0:
        bpy.data.objects[object_name].location[2] = random.uniform( - z_location, z_location)
    
 
        
def change_position_camera_rig(x_rotation_from=0, x_rotation_to=0, y_rotation_from=0, y_rotation_to=0, z_rotation_from =0, z_rotation_to=0, x_location_from=0, x_location_to=0, y_location_from=0, y_location_to=0, z_location_from=0, z_location_to=0, object_name='Empty'):
   
    if x_rotation_from != 0 or x_rotation_to != 0: 
        bpy.data.objects[object_name].rotation_euler[0] = random.uniform(x_rotation_from * 0.0174533, x_rotation_to * 0.0174533)
            
    if y_rotation_from != 0 or y_rotation_to != 0: 
        bpy.data.objects[object_name].rotation_euler[1] = random.uniform(y_rotation_from * 0.0174533, y_rotation_to * 0.0174533)
            
    if z_rotation_from != 0 or z_rotation_to != 0:
        bpy.data.objects[object_name].rotation_euler[2] = random.uniform(z_rotation_from * 0.0174533, z_rotation_to * 0.0174533)
            
    if x_location_from != 0 or x_location_to != 0:
        bpy.data.objects[object_name].location[0] = random.uniform(x_location_from, x_location_to)
    if y_location_from != 0 or y_location_to != 0:
        bpy.data.objects[object_name].location[1] = random.uniform(y_location_from, y_location_to)
    if z_location_from != 0 or z_location_to != 0:
        bpy.data.objects[object_name].location[2] = random.uniform(z_location_from, z_location_to)

    

def change_position_camera_rig_distance(x_rotation_from=0, x_rotation_to=0, y_rotation_from=0, y_rotation_to=0, z_rotation_from =0, z_rotation_to=0, x_location_from=0, x_location_to=0, y_location_from=0, y_location_to=0, z_location_from=0, z_location_to=0, object_name='Empty'):
     
    if x_rotation_from != 0 or x_rotation_to != 0: 
        bpy.data.objects[object_name].rotation_euler[0] = random.uniform(x_rotation_from * 0.0174533, x_rotation_to * 0.0174533)
    if y_rotation_from != 0 or y_rotation_to != 0: 
        bpy.data.objects[object_name].rotation_euler[1] = random.uniform(y_rotation_from * 0.0174533, y_rotation_to * 0.0174533)
    if z_rotation_from != 0 or z_rotation_to != 0:
        bpy.data.objects[object_name].rotation_euler[2] = random.uniform(z_rotation_from * 0.0174533, z_rotation_to * 0.0174533)
        
    if x_location_from != 0 or x_location_to != 0:
        bpy.data.objects[object_name].location[0] = random.uniform(x_location_from, x_location_to)
    
    if y_location_from != 0 or y_location_to != 0:
        random_distance_y = random.uniform(y_location_from, y_location_to)
        bpy.data.objects[object_name].location[1] = random_distance_y
        
    if z_location_from != 0 or z_location_to != 0:
        random_distance_z = random.uniform(z_location_from, z_location_to)
        bpy.data.objects[object_name].location[2] = random_distance_z


def random_fog():
    
    if bpy.data.objects['Random Fog']: 
        print('works!!!!!!!!!!!!__________________!!!!!!!!!!!!!!!!!!!')

      
        

#-------------OPERATORS--------------
        

class TEXT_RANDOMIZATOR(bpy.types.Operator):    
    bl_label = "Add Random Letter"    
    bl_idname ="text.randomization_operator"
    
    def execute(self, context):
        
        font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
        font_curve.body = "a"
        font_obj = bpy.data.objects.new(name="Random Word", object_data=font_curve)
        bpy.context.scene.collection.objects.link(font_obj)
        
        bpy.app.handlers.frame_change_post.append(random_text_hendler)
        return {'FINISHED'}
    



class TEXT_RANDOMIZATOR_UPPER(bpy.types.Operator):
    bl_label = "Add Random Upper Letter"    
    bl_idname ="text.randomization_operator_upper"
    
    def execute(self, context): 
        
        font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
        font_curve.body = "A"
        font_obj = bpy.data.objects.new(name="Random Upper Word", object_data=font_curve)
        bpy.context.scene.collection.objects.link(font_obj)
        
        bpy.app.handlers.frame_change_post.append(random_upper_text_hendler)
        return {'FINISHED'}
    
    
    
class NUMBER_RANDOMIZATOR(bpy.types.Operator):
    bl_label = "Add Random Number"
    bl_idname ="text.randomization_number_operator"
    
    def execute(self, context):
        
        font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
        font_curve.body = str(random.randint(0,9))
        font_obj = bpy.data.objects.new(name="Random Number", object_data=font_curve)
        bpy.context.scene.collection.objects.link(font_obj)
        
        bpy.app.handlers.frame_change_post.append(random_number_hendler)
        return {'FINISHED'}
    
    
    
class RANDOM_ROTATION_CUBE(bpy.types.Operator):
    bl_label = "Add Random Rotation Cube"
    bl_idname ="mesh.add_cube"
       
    def execute(self, context):       
        bpy.ops.object.empty_add(type='CUBE', align='WORLD') 
        
        object_name = 'Random Rotation Cube'
         
        obj = bpy.context.object
        obj.name = object_name 
        
        bpy.app.handlers.frame_change_post.append(random_rotation_cube_hendler)
        
        return {'FINISHED'}
    

    
class RENDER_CAMERA_RIG_USE_REGEON(bpy.types.Operator):    
    bl_label = "Render Regeon"    
    bl_idname ="mash.camera_rig_render_use_regeon"
    
    def execute(self, context):
        
        bpy.data.scenes["Scene"].render.use_border = True
        bpy.data.scenes["Scene"].render.use_crop_to_border =False
        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_post.append(file_path_hendler)
        bpy.ops.render.animated_render_border_render()
        print('FINISH RENDER!')
        
        return {'FINISHED'}
    
    
class RENDER_IMAGE_CAMERA_RIG(bpy.types.Operator):    
    bl_label = "Render Image"    
    bl_idname ="mash.camera_rig_render_image"
    
    def execute(self, context):        
        bpy.app.handlers.frame_change_pre.clear()
        bpy.ops.render.renderqueue(mode='SELECTED') 
        print('FINISH RENDER!')

        return {'FINISHED'}
    
    

class RENDER_CAMERA_RIG_CROP(bpy.types.Operator):    
    bl_label = "Render Crop Regeon"    
    bl_idname ="mash.camera_rig_render_crop_regeon"
    
    def execute(self, context):
          
        bpy.data.scenes["Scene"].render.use_border = True
        bpy.data.scenes["Scene"].render.use_crop_to_border =True
        bpy.app.handlers.frame_change_pre.clear()
        bpy.app.handlers.frame_change_post.append(file_path_hendler)
        bpy.ops.render.animated_render_border_render()
        print('FINISH RENDER!')
        
        return {'FINISHED'}
    
    

class RENDER_CAMERA_RIG(bpy.types.Operator):    
    bl_label = "Render"    
    bl_idname ="mash.camera_rig_render"
    
    def execute(self, context):
          
        bpy.data.scenes["Scene"].render.use_crop_to_border = False
        bpy.data.scenes["Scene"].render.use_border = False
        bpy.app.handlers.frame_change_pre.clear()
        #bpy.app.handlers.frame_change_post.clear()
        bpy.app.handlers.frame_change_post.append(file_path_hendler)        
        bpy.ops.render.render(animation=True, use_viewport=True)

        print('FINISH RENDER!')
    
        return {'FINISHED'}
    


class START_RIG_RANDOMIZATION(bpy.types.Operator):    
    bl_label = "START"    
    bl_idname ="mash.start_camera_rig_randomization"
    
    def execute(self, context):
        
        bpy.app.handlers.frame_change_pre.append(camera_rig_center_hendler)
        bpy.app.handlers.frame_change_pre.append(camera_rig_distance_hendler)    
        bpy.app.handlers.frame_change_post.append(file_path_hendler)        
  
        
        return {'FINISHED'}


    
class STOP_RIG_RANDOMIZATION(bpy.types.Operator):    
    bl_label = "STOP"    
    bl_idname ="mash.stop_camera_rig_randomization"
    
    def execute(self, context):
    
        bpy.app.handlers.frame_change_pre.clear()     
        
        return {'FINISHED'}



class WORLD_LIGHTS_ADD(bpy.types.Operator):
    bl_label = "Day"
    bl_idname ="mesh.add_random_world_lights"
           
    def execute(self, context):


        sky_texture = bpy.context.scene.world.node_tree.nodes.new("ShaderNodeTexSky")
        bg = bpy.context.scene.world.node_tree.nodes["Background"]
        bpy.context.scene.world.node_tree.links.new(bg.inputs["Color"], sky_texture.outputs["Color"])
        sky_texture.sky_type = 'NISHITA' 
        bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sun_intensity = 0.30000001192092896
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 0.3
        # bpy.data.worlds["World"].node_tree.nodes["Sky Texture"].sky_type 
        print('created')
        bpy.app.handlers.frame_change_post.append(random_sky_texture_values_hendler)

        return {'FINISHED'}


class LIGHT_POINT_ADD(bpy.types.Operator):
    bl_label = "Add Random Light Point"
    bl_idname ="mesh.add_light_point"
           
    def execute(self, context):

        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(1.06297, -1.73384, 0.0359983), scale=(1, 1, 1))
        bpy.context.object.name = 'Random Light Point' 

        bpy.app.handlers.frame_change_post.append(random_light_point_hendler)

        return {'FINISHED'}




class FOG_ADD(bpy.types.Operator):
    bl_label = "Add Fog"
    bl_idname ="mesh.add_fog"
           
    def execute(self, context):

        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(-0, -0, 0), scale=(3, 3, 3))

        #bpy.ops.mesh.primitive_cube_add(size=2)
        bpy.context.object.name = 'Random Fog' 

        cube = bpy.context.active_object
        mat = bpy.data.materials.new(name="PrincipleVolumeMaterial")
        cube.data.materials.append(mat)
        mat.use_nodes = True

        bpy.context.active_object.data.materials[0].node_tree.nodes["Principled BSDF"].inputs[19].default_value = 0


        # Get the material for the object you want to remove the node from
        obj = bpy.context.object
        mat = obj.data.materials[0]

        # Get the node tree for the material
        ntree = mat.node_tree

        # Get the Material Output Surface node
        output_node = ntree.nodes.get("Material Output")


        # Create a principled volume shader
        volume_shader = mat.node_tree.nodes.new(type='ShaderNodeVolumePrincipled')

        # Connect the shader to the material output
        output_node = mat.node_tree.nodes.get('Material Output')
        mat.node_tree.links.new(volume_shader.outputs[0], output_node.inputs[1])

        bpy.context.active_object.data.materials[0].node_tree.nodes["Principled Volume"].inputs[2].default_value = 0.01
        bpy.context.active_object.data.materials[0].node_tree.nodes["Principled Volume"].inputs[4].default_value = -0.981818
        bpy.context.active_object.data.materials[0].node_tree.nodes["Principled Volume"].inputs[6].default_value = 0
        bpy.context.active_object.data.materials[0].node_tree.nodes["Principled Volume"].inputs[8].default_value = 0

       

        #bpy.app.handlers.frame_change_post.append(random_fog_hendler)

        return {'FINISHED'}



#mesh.add_light_point


class WORLD_NIGHT_LIGHTS_ADD(bpy.types.Operator):
    bl_label = "Night"
    bl_idname ="mesh.add_random_world_night_lights"
           
    def execute(self, context):

        if bpy.context.scene.objects.get('Random Rotation Light Cube'):
            return {'FINISHED'}
        else:
            bpy.ops.object.empty_add(type='CUBE', align='WORLD') 
            bpy.context.object.name = 'Random Rotation Light Cube' 

            bpy.context.object.scale[0] = 10
            bpy.context.object.scale[1] = 10
            bpy.context.object.scale[2] = 10
            objects = bpy.data.objects

            random_rotation_cube = objects['Random Rotation Light Cube']


            bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(-1, 0, 1), scale=(1, 1, 1))
            bpy.context.object.name = 'Random Cube Spot Left Top'

            bpy.context.object.rotation_euler[0] = 0 * 0.0174533
            bpy.context.object.rotation_euler[1] = - 45 * 0.0174533
            bpy.context.object.rotation_euler[2] = 0 * 0.0174533
            bpy.context.object.data.energy = 10000
            bpy.context.object.data.color = (1, 0.646623, 0.265359)

            random_cube_spot_left_top = objects['Random Cube Spot Left Top']

            bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(1, 0, 1), scale=(1, 1, 1))
            bpy.context.object.name = 'Random Cube Spot Right Top'

            bpy.context.object.rotation_euler[0] = 0 * 0.0174533
            bpy.context.object.rotation_euler[1] = 45 * 0.0174533
            bpy.context.object.rotation_euler[2] = 0 * 0.0174533
            bpy.context.object.data.energy = 10000
            bpy.context.object.data.color = (1, 0.646623, 0.265359)

            random_cube_spot_right_top = objects['Random Cube Spot Right Top']







            random_cube_spot_left_top.parent = random_rotation_cube
            random_cube_spot_right_top.parent = random_rotation_cube


            bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 0

            bpy.app.handlers.frame_change_post.append(random_rotation_light_cube_hendler)
        
        return {'FINISHED'}


# node_tree.nodes["Background"].inputs[1].default_value

class RANDOM_BACKGROUNDS_85(bpy.types.Operator):

    bl_label = "Cam 85"
    bl_idname ="mesh.add_plane_85"
    
    random_to: bpy.props.IntProperty(name= "Random to", default= 1) 
       
    def execute(self, context):
        
        random_to = self.random_to      

        try:
            random_plane_validation_prop = bpy.context.scene.objects.get('Random Background Plane 85')
        except:
            random_plane_validation_prop = None

        if (random_plane_validation_prop):
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            return {'FINISHED'}

        
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(-0.2, 300, -17.9), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 85.8 * 0.0174533
        bpy.context.object.scale[0] = 1.78 * 32.2
        bpy.context.object.scale[1] = 1 * 32.9
        bpy.context.object.scale[2] = 0

        objects = bpy.data.objects
        camera_rig_distance = objects['Camera Rig Distance']

        bpy.context.object.name = 'Random Background Plane 85'

        random_background_plane = objects['Random Background Plane 85']

        random_background_plane.parent = camera_rig_distance

        try:
            mat_validation = bpy.data.materials['Material For Random Videos'] 
        except:
            mat_validation = None
            
        if(mat_validation == None):
            mat = bpy.data.materials.new(name="Material For Random Videos")
        elif (mat_validation): 
            mat = mat_validation
            bpy.context.active_object.data.materials.append(mat)
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            
            return {'FINISHED'}


            
        
        bpy.context.active_object.data.materials.append(mat)
        bpy.context.object.active_material.use_nodes = True

        image_node = mat.node_tree.nodes.new('ShaderNodeTexImage')
        mat.node_tree.links.new(image_node.outputs['Color'], mat.node_tree.nodes['Emission'].inputs['Base Color'], verify_limits=True)
        
        bpy.ops.image.new(name="TestImg", width=1920, height=1080)
        mat = bpy.context.view_layer.objects.active.active_material
        tex = bpy.data.images.get('TestImg')
        image_node.image = tex
        bpy.data.images["TestImg"].source = 'MOVIE'
        bpy.data.materials["Material For Random Videos"].node_tree.nodes["Image Texture"].image_user.use_auto_refresh = True
        
        bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
    
        bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
     
        return {'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)




class RANDOM_BACKGROUNDS_50(bpy.types.Operator):
    bl_label = "Cam 50"
    bl_idname ="mesh.add_plane_50"
    
    random_to: bpy.props.IntProperty(name= "Random to", default= 1) 
       
    def execute(self, context):
        
        random_to = self.random_to      
        random_plane_validation_prop = bpy.context.scene.objects.get('Random Background Plane 50')

        if (random_plane_validation_prop):
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            return {'FINISHED'}

        
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(-0.2, 300, -17.9), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 85.8 * 0.0174533
        bpy.context.object.scale[0] = 1.78 * 32.2
        bpy.context.object.scale[1] = 1 * 32.9
        bpy.context.object.scale[2] = 0

        objects = bpy.data.objects
        camera_rig_distance = objects['Camera Rig Distance']

        bpy.context.object.name = 'Random Background Plane 50'

        random_background_plane = objects['Random Background Plane 50']

        random_background_plane.parent = camera_rig_distance

        try:
            mat_validation = bpy.data.materials['Material For Random Videos'] 
        except:
            mat_validation = None
            
        if(mat_validation == None):
            mat = bpy.data.materials.new(name="Material For Random Videos")
        elif (mat_validation): 
            mat = mat_validation
            bpy.context.active_object.data.materials.append(mat)
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            
            return {'FINISHED'}
            
        
        bpy.context.active_object.data.materials.append(mat)
        bpy.context.object.active_material.use_nodes = True

        image_node = mat.node_tree.nodes.new('ShaderNodeTexImage')
        mat.node_tree.links.new(image_node.outputs['Color'], mat.node_tree.nodes['Emission'].inputs['Base Color'], verify_limits=True)
        
        
        bpy.ops.image.new(name="TestImg", width=1920, height=1080)
        mat = bpy.context.view_layer.objects.active.active_material
        tex = bpy.data.images.get('TestImg')
        image_node.image = tex        
        bpy.data.images["TestImg"].source = 'MOVIE'
        bpy.data.materials["Material For Random Videos"].node_tree.nodes["Image Texture"].image_user.use_auto_refresh = True
        
        bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
    
        bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
     
        return {'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)


    

class RANDOM_BACKGROUNDS_400(bpy.types.Operator):
    bl_label = "Cam 400"
    bl_idname ="mesh.add_plane_400"
    
    random_to: bpy.props.IntProperty(name= "Random to", default= 1) 
       
    def execute(self, context):
        
        random_to = self.random_to      
        random_plane_validation_prop = bpy.context.scene.objects.get('Random Background Plane 400')

        if (random_plane_validation_prop):
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            return {'FINISHED'}

        
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(-0.2, 300, -17.9), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 85.8 * 0.0174533
        bpy.context.object.scale[0] = 1.78 * 32.2
        bpy.context.object.scale[1] = 1 * 32.9
        bpy.context.object.scale[2] = 0

        objects = bpy.data.objects
        camera_rig_distance = objects['Camera Rig Distance']

        bpy.context.object.name = 'Random Background Plane 400'

        random_background_plane = objects['Random Background Plane 400']

        random_background_plane.parent = camera_rig_distance
        
    
        try:
            mat_validation = bpy.data.materials['Material For Random Videos'] 
        except:
            mat_validation = None
            
        if(mat_validation == None):
            mat = bpy.data.materials.new(name="Material For Random Videos")
        elif (mat_validation): 
            mat = mat_validation
            bpy.context.active_object.data.materials.append(mat)
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            
            return {'FINISHED'}
            
        
        bpy.context.active_object.data.materials.append(mat)
        bpy.context.object.active_material.use_nodes = True

        image_node = mat.node_tree.nodes.new('ShaderNodeTexImage')
        mat.node_tree.links.new(image_node.outputs['Color'], mat.node_tree.nodes['Emission'].inputs['Base Color'], verify_limits=True)
        
        
        bpy.ops.image.new(name="TestImg", width=1920, height=1080)
        mat = bpy.context.view_layer.objects.active.active_material
        tex = bpy.data.images.get('TestImg')
        image_node.image = tex        
        bpy.data.images["TestImg"].source = 'MOVIE'
        bpy.data.materials["Material For Random Videos"].node_tree.nodes["Image Texture"].image_user.use_auto_refresh = True
        
        bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
    
        bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
     
        return {'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)




class RANDOM_BACKGROUNDS(bpy.types.Operator):
    bl_label = "Add Random Video Plane HD"
    bl_idname ="mesh.add_plane"
    
    random_to: bpy.props.IntProperty(name= "Random to", default= 1) 
       
    def execute(self, context):
        
        random_to = self.random_to      
        
        random_plane_validation_prop = bpy.context.scene.objects.get('Random Background Plane')

        if (random_plane_validation_prop):
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            return {'FINISHED'}
        
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        bpy.context.object.rotation_euler[0] = 90 * 0.0174533
        bpy.context.object.scale[0] = 1.78
        bpy.context.object.scale[1] = 1
        bpy.context.object.scale[2] = 0
        
        bpy.context.object.name = 'Random Background Plane'
    
        try:
            mat_validation = bpy.data.materials['Material For Random Videos'] 
        except:
            mat_validation = None
            
        if(mat_validation == None):
            mat = bpy.data.materials.new(name="Material For Random Videos")
        elif (mat_validation): 
            mat = mat_validation
            bpy.context.active_object.data.materials.append(mat)
            bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
            bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
            
            return {'FINISHED'}
            
        
        bpy.context.active_object.data.materials.append(mat)
        bpy.context.object.active_material.use_nodes = True

        image_node = mat.node_tree.nodes.new('ShaderNodeTexImage')
        mat.node_tree.links.new(image_node.outputs['Color'], mat.node_tree.nodes['Principled BSDF'].inputs['Base Color'], verify_limits=True)
        
        
        bpy.ops.image.new(name="TestImg", width=1920, height=1080)
        mat = bpy.context.view_layer.objects.active.active_material
        tex = bpy.data.images.get('TestImg')
        image_node.image = tex        
        bpy.data.images["TestImg"].source = 'MOVIE'
        bpy.data.materials["Material For Random Videos"].node_tree.nodes["Image Texture"].image_user.use_auto_refresh = True
        
        bpy.data.materials['Material For Random Videos'].node_tree.nodes['Image Texture'].image_user.frame_duration = random_to
    
        bpy.app.handlers.frame_change_post.append(random_background_frame_hendler)
     
        return {'FINISHED'}
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)


#-------cam rig validations -------- 
    
def rotation_from_default():
    cam_rig_validation_prop = None
    try:
        cam_rig_validation_prop = bpy.context.scene.objects.get('Camera Rig Center')
    except:
         print("An exception occurred")
    if(cam_rig_validation_prop):
        return bpy.context.scene['cam_rig_rotation_from']
    else:
        return -30
    
    
def rotation_to_default():
    cam_rig_validation_prop = None
    try:
        cam_rig_validation_prop = bpy.context.scene.objects.get('Camera Rig Center')
    except: 
         print("An exception occurred")
    if(cam_rig_validation_prop):
        return bpy.context.scene['cam_rig_rotation_to']
    else:
        return 30
    
    
def location_from_default():
    cam_rig_validation_prop = None
    try:
        cam_rig_validation_prop = bpy.context.scene.objects.get('Camera Rig Center')
    except:
         print("An exception occurred")
    if(cam_rig_validation_prop):
        return bpy.context.scene['cam_rig_distance_from']
    else:
        return -30
    
    
def location_to_default():
    cam_rig_validation_prop = None
    try:
        cam_rig_validation_prop = bpy.context.scene.objects.get('Camera Rig Center')
    except:
         print("An exception occurred")
    if(cam_rig_validation_prop):
        return bpy.context.scene['cam_rig_distance_to']
    else:
        return -300

 
class CAMERA_RIG_ADD(bpy.types.Operator):
    bl_label = "Add Rig"
    bl_idname ="mesh.add_camera_rig"
    
    z_rotation_from: bpy.props.IntProperty(name= "Rotation Z range from", default= rotation_from_default())
    z_rotation_to: bpy.props.IntProperty(name= "Rotation Z range to", default= rotation_to_default())

    y_location_from: bpy.props.IntProperty(name= "Distance Y range from", default= location_from_default())
    y_location_to: bpy.props.IntProperty(name= "Distance Y range to", default= location_to_default()) 
    
    def execute(self, context):  
        
        z_rotation_from = self.z_rotation_from
        z_rotation_to = self.z_rotation_to
        
        y_location_from = self.y_location_from
        y_location_to = self.y_location_to
  
        context.scene.cam_rig_rotation_from = z_rotation_from
        context.scene.cam_rig_rotation_to = z_rotation_to 
        context.scene.cam_rig_distance_from = y_location_from
        context.scene.cam_rig_distance_to = y_location_to
        
        cam_rig_validation_prop = bpy.context.scene.objects.get('Camera Rig Center')
        
        if (cam_rig_validation_prop):
            print(cam_rig_validation_prop)
            return {'FINISHED'}
        
        
        bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=(-0, -0, -0), scale=(1, 1, 1)) 
        object_name2 = 'Camera Rig Center'
        bpy.context.object.name = object_name2 
        bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=(-0, -80, -0), scale=(1, 1, 1))
        object_name = "Camera Rig Distance"
        
        obj = bpy.context.object
        obj.name = object_name 
        
        #-------camera 85
        
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(90 * 0.0174533, 0, 0), scale=(1, 1, 1))
        
        camera_name = 'Camera 85'
        
        obj = bpy.context.object
        obj.name = camera_name
        
        bpy.context.object.data.lens = 85
        bpy.context.object.data.sensor_width = 32.33
        bpy.context.object.data.clip_end = 90000
        bpy.context.object.location[2] = 4.323
        bpy.context.object.location[0] = -0.185
        bpy.context.object.rotation_euler[0] = 85.8 * 0.0174533
        bpy.context.object.data.name = "Camera 85"
        
         #-------camera 50
         
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(90 * 0.0174533, 0, 0), scale=(1, 1, 1))
        
        camera_name = 'Camera 50'
        
        obj = bpy.context.object
        obj.name = camera_name
        
        bpy.context.object.data.lens = 50
        bpy.context.object.data.sensor_width = 32.33
        bpy.context.object.data.clip_end = 90000
        bpy.context.object.location[2] = 2.46438
        bpy.context.object.rotation_euler[0] = 82.91 * 0.0174533
        bpy.context.object.data.name = "Camera 50"
        
        #---------camera 400
        
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(90 * 0.0174533, 0, 0), scale=(1, 1, 1))
        
        camera_name = 'Camera 400'
        
        obj = bpy.context.object
        obj.name = camera_name
        
        bpy.context.object.data.lens = 400
        bpy.context.object.data.sensor_width = 32.33
        bpy.context.object.data.clip_end = 90000
        bpy.context.object.location[2] = 4.328
        bpy.context.object.location[0] = -0.185
        bpy.context.object.rotation_euler[0] = 89.114 * 0.0174533
        bpy.context.object.data.name = "Camera 400"
        
        #---------append

        objects = bpy.data.objects
        rig_center = objects['Camera Rig Center']
        camera_rig = objects['Camera Rig Distance']
        camera_85 = objects['Camera 85']
        camera_50 = objects['Camera 50']
        camera_400 = objects['Camera 400']
        camera_rig.parent = rig_center
        camera_85.parent = camera_rig
        camera_50.parent = camera_rig
        camera_400.parent = camera_rig
        
        bpy.app.handlers.frame_change_pre.append(camera_rig_center_hendler)
        bpy.app.handlers.render_post.append(camera_rig_center_hendler)
        print("------- --------  camera_rig_distance_hendler ------ working! ---- ***WARNING** if you delete Camera Rig Center Null Object, this handler will continue work untill you restart blender, or RV synth script.")
        bpy.app.handlers.frame_change_pre.append(camera_rig_distance_hendler)
        bpy.app.handlers.render_post.append(camera_rig_distance_hendler)
        print("------- --------  camera_rig_distance_hendler ------ working! ---- ***WARNING** if you delete Camera Rig Distance Null Object, this handler will continue work untill you restart blender, or RV synth script.")  
    
        return {'FINISHED'}
    
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
#Addon Preferences

#----------------------------------addon render q -----------------------------------







def register():
    
    validations()

    bpy.utils.register_class(CAMERA_RIG_ADD)
    bpy.types.Scene.cam_rig_distance_from = bpy.props.IntProperty(
    name='Camera rig distance from value',
    )
    bpy.types.Scene.cam_rig_distance_to = bpy.props.IntProperty(
    name='Camera rig distance to value',
    )
    bpy.types.Scene.cam_rig_rotation_from = bpy.props.IntProperty(
    name='Camera rig rotation from value',
    )
    bpy.types.Scene.cam_rig_rotation_to = bpy.props.IntProperty(
    name='Camera rig rotation to value',
    )
    bpy.utils.register_class(START_RIG_RANDOMIZATION)
    bpy.utils.register_class(RENDER_IMAGE_CAMERA_RIG)
    bpy.utils.register_class(STOP_RIG_RANDOMIZATION)
    bpy.utils.register_class(RANDOM_TEXT_PANEL)
    bpy.utils.register_class(RANDOM_OBJECTS_PANEL)
    bpy.utils.register_class(TEXT_RANDOMIZATOR)
    bpy.utils.register_class(TEXT_RANDOMIZATOR_UPPER)
    bpy.utils.register_class(NUMBER_RANDOMIZATOR)
    bpy.utils.register_class(RANDOM_ROTATION_CUBE)
    bpy.utils.register_class(RANDOM_BACKGROUNDS_85)
    bpy.utils.register_class(RANDOM_BACKGROUNDS_50)
    bpy.utils.register_class(RANDOM_BACKGROUNDS_400)
    bpy.utils.register_class(CAMERA_RIG_PANEL)
    bpy.utils.register_class(RENDER_CAMERA_RIG_USE_REGEON)
    bpy.utils.register_class(RENDER_CAMERA_RIG_CROP)
    bpy.utils.register_class(RENDER_CAMERA_RIG)
    bpy.utils.register_class(WORLD_LIGHTS)
    bpy.utils.register_class(WORLD_LIGHTS_ADD)
    bpy.utils.register_class(WORLD_NIGHT_LIGHTS_ADD)
    bpy.utils.register_class(RANDOM_BACKGROUNDS)
    bpy.utils.register_class(LIGHT_POINT_ADD)
    bpy.utils.register_class(FOG_ADD)

    
def unregister():
    bpy.app.handlers.frame_change_pre.clear()
    bpy.app.handlers.frame_change_post.clear()
    
    del bpy.types.Scene.cam_rig_distance_from
    del bpy.types.Scene.cam_rig_distance_to
    del bpy.types.Scene.cam_rig_rotation_from
    del bpy.types.Scene.cam_rig_rotation_to
    bpy.utils.unregister_class(RANDOM_TEXT_PANEL)
    bpy.utils.unregister_class(RANDOM_OBJECTS_PANEL)
    bpy.utils.unregister_class(TEXT_RANDOMIZATOR)
    bpy.utils.unregister_class(NUMBER_RANDOMIZATOR)
    bpy.utils.unregister_class(RANDOM_ROTATION_CUBE)
    bpy.utils.unregister_class(TEXT_RANDOMIZATOR_UPPER)
    bpy.utils.unregister_class(CAMERA_RIG_ADD)
    bpy.utils.unregister_class(CAMERA_RIG_PANEL)
    bpy.utils.unregister_class(RENDER_CAMERA_RIG_USE_REGEON)
    bpy.utils.unregister_class(RENDER_CAMERA_RIG_CROP)
    bpy.utils.unregister_class(RENDER_CAMERA_RIG)
    bpy.utils.unregister_class(WORLD_LIGHTS)
    bpy.utils.unregister_class(WORLD_LIGHTS_ADD)
    bpy.utils.unregister_class(WORLD_NIGHT_LIGHTS_ADD)
    bpy.utils.unregister_class(LIGHT_POINT_ADD)
    bpy.utils.unregister_class(FOG_ADD)



    bpy.app.handlers.frame_change_post.clear()

    
if __name__== "__main__":
    register()

#unregister()