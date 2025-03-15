from typing import List, Tuple
import warnings
import pygame


# A class for creating sprite lists or sprite dictionaries.
class HelperSpriteLoader:
    data_path = "data/"

    #
    @classmethod
    def check_path(cls):
        pass

    # This is here to make sure I don't accidentally input the
    # wrong values when loading sprites (I've already done it once).
    @classmethod
    def check_frame_size(cls, image: pygame.Surface, frame_size: Tuple[int, int]) -> None:
        width, height = image.get_size()
        width_remainder = width % frame_size[0]
        height_remainder = height % frame_size[1]
        horizontal_frames = width // frame_size[0]
        vertical_frames = height // frame_size[1]

        # This totally misses the case where you have no remainder because the numbers
        # perfectly divide into each other, unfortunately there's probably no good way to detect that.
        # Alternatively, I could also require passing in an explicit number of frames to check against.
        if width_remainder != 0:
            frame_width = round(width / frame_size[0], 2)
            raise ValueError(f'Frame width: {frame_width} has to be a multiple of {frame_size[0]}!')
        elif height_remainder != 0:
            frame_height = round(height / frame_size[1], 2)
            raise ValueError(f'Frame height: {frame_height} has to be a multiple of {frame_size[1]}!')

        # This is a poor man's "solution" (stopgap), and by golly I'm the poorest motherfuckin' man.
        if horizontal_frames >= 15:
            warnings.warn(f'A suspiciously high number of Horizontal frames: {horizontal_frames}!')
        elif horizontal_frames <= 2:
            warnings.warn(f'A suspiciously low number of Horizontal frames: {horizontal_frames}!')
        if vertical_frames >= 10:
            warnings.warn(f'A suspiciously high number of Vertical frames: {vertical_frames}!')
        elif vertical_frames <= 0:  # If this case happens the world is ending, or I royally fucked up.
            warnings.warn(f'A suspiciously low number of Vertical frames: {vertical_frames}!')

    # A method to create spritesheets.
    # TODO - Implement sprite sheets that have a height of greater than 1!
    # Just do for y in range then nest for x in range, also change the return type to a Union
    # between a List and Dictionary for those fun state-based sprites!
    # TODO - Maybe clean it up too, this shit looks like it's going to explode if I look at it wrong.
    @classmethod
    def load_sprite(cls, path: str, frame_size: Tuple[int, int], scale=1) -> List[pygame.Surface]:
        scaled_size = (frame_size[0] * scale, frame_size[1] * scale)
        full_path = cls.data_path + path
        spritesheet = pygame.image.load(full_path).convert_alpha()

        if scale != 1:
            spritesheet = pygame.transform.scale_by(spritesheet, scale)
        spritesheet_width, spritesheet_height = spritesheet.get_size()

        cls.check_frame_size(spritesheet, scaled_size)

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
    def get_subsurface(cls, image: pygame.Surface, frame_position: Tuple[int, int], frame_size: Tuple[int, int]) -> pygame.Surface:
        # Create a rectangle to cut subsurfaces from the parent surface at a specific position.
        cutter = pygame.Rect(frame_position, frame_size)
        subsurface = image.subsurface(cutter)
        return subsurface