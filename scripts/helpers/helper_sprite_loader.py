from typing import List, Tuple
import pygame


# A class for creating sprite lists or sprite dictionaries.
# TODO - Add some basic error checking.
class HelperSpriteLoader:
    data_path = "data/"

    # A method to create spritesheets.
    # TODO - Implement sprite sheets that have a height of greater than 1!
    # TODO - Maybe clean it up too, this shit looks like it's going to explode if I look at it wrong.
    @classmethod
    def load_sprite(cls, path: str, frame_size: Tuple, scale=1) -> List[pygame.Surface]:
        scaled_size = (frame_size[0] * scale, frame_size[1] * scale)
        full_path = cls.data_path + path

        spritesheet = pygame.image.load(full_path).convert_alpha()
        if scale != 1:
            spritesheet = pygame.transform.scale_by(spritesheet, scale)
        spritesheet_width, spritesheet_height = spritesheet.get_size()

        # Subtract one because we are zero indexed!
        horizontal_frames = (spritesheet_width // scaled_size[0]) - 1
        vertical_frames = (spritesheet_height // scaled_size[1]) - 1  # Implement this functionality later!

        # Build the sprite list from subsurfaces.
        sprite_list = []
        for x in range(0, horizontal_frames):
            # Get the x position based on the frame size and iteration.
            x_position = scaled_size[0] * x
            frame = cls.get_subsurface(spritesheet, (x_position, 0), scaled_size)
            sprite_list.append(frame)

        return sprite_list

    # Self-explanatory I guess.
    @classmethod
    def get_subsurface(cls, image: pygame.Surface, frame_position: Tuple, frame_size: Tuple) -> pygame.Surface:
        # Create a rectangle to cut subsurfaces from the parent surface at a specific position.
        cutter = pygame.Rect(frame_position, frame_size)
        subsurface = image.subsurface(cutter)
        return subsurface