#pip install ogre-python==14.4.0
#brew install cmake assimp sdl2 freetype swig
from ogre import *

# Initialize OGRE
root = Root()
root.loadPlugin("RenderSystem_GL")  # Use OpenGL (or RenderSystem_Direct3D11 for Windows)
root.initialise(False)

# Create render window
window = root.createRenderWindow("MyWindow", 800, 600, False)

# Create scene manager
scene_mgr = root.createSceneManager("DefaultSceneManager")

# Create camera
camera = scene_mgr.createCamera("Camera")
camera.setPosition(Vector3(0, 0, 500))
camera.lookAt(Vector3(0, 0, 0))
viewport = window.addViewport(camera)
viewport.backgroundColour = (0, 0, 0, 1)

# Initialize resources
ResourceGroupManager.getSingleton().addResourceLocation("../media/models", "FileSystem")
ResourceGroupManager.getSingleton().initialiseAllResourceGroups()

# Create object
entity = scene_mgr.createEntity("Cube", "cube.mesh")
scene_mgr.getRootSceneNode().attachObject(entity)

# Main loop
while not root.hasEnded():
    root.renderOneFrame()

# Cleanup
root.shutdown()
