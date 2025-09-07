from SETTINGS import DEBUG, WINDOW
import pygame, time

class WindowManager(object):
    # ========================
    # INITIALIZATION
    # ========================
    def __init__(self, size=WINDOW['SIZE'], 
                 title=WINDOW['TITLE'], 
                 bg_color=WINDOW['BG_COLOR'], 
                 fps=WINDOW['FPS']):
        """Initialize window, FPS counter, and input states."""
        self.size = size
        self.title = title
        self.bg_color = bg_color
        self.fps = fps

        # Pygame window and clock
        pygame.display.set_caption(self.title)
        self.window = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        # FPS tracking
        self._frames = 0
        self._last_time = time.time()
        self.real_fps_value = 0

    # ========================
    # FPS MANAGEMENT
    # ========================
    def _count_real_fps(self):
        """Count and return the actual FPS value based on real time."""
        self._frames += 1
        current_time = time.time()
        if current_time - self._last_time >= 1:
            self.real_fps_value = self._frames
            self._frames = 0
            self._last_time = current_time
        return self.real_fps_value

    # ========================
    # EVENT & INPUT HANDLING
    # ========================
    def update(self):
        """Update FPS, events, and input states."""
        self.real_fps_value = self._count_real_fps()
        self.clock.tick(self.fps)

    # ========================
    # RENDERING
    # ========================
    def render(self):
        """Clear the screen with background color."""
        self.window.fill(self.bg_color)
        pygame.display.flip()