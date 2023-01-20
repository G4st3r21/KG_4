from Math.Vector3F import Vector3F
from ObjReader.ObjReader import read
from RenderEngine.Camera import Camera
from RenderEngine.RenderEngine import render_new

camera: Camera = Camera(
    Vector3F(0.0, 0.0, 100.0),
    Vector3F(0.0, 0.0, 0.0),
    1.0, 1920 / 1080, 0.01, 100
)

with open("obj/WrapSkull.obj", "r") as model:
    obj_file_content = [string.strip() for string in model.readlines()]
main_model = read(obj_file_content)

render_new(None, camera, main_model, 1920, 1280)
