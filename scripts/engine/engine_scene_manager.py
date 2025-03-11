from scripts.scenes.test_scene import SceneTestScene
from scripts.engine.engine_base import EngineBase


#
class EngineSceneManager(EngineBase):
    def __init__(self, engine):
        super().__init__(engine)
        self.scenes = {'test': SceneTestScene}
        self.current_scene = SceneTestScene(self.engine)

    #
    def change_scene(self, scene) -> None:
        self.current_scene = self.scenes[scene](self.engine)
