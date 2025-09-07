import pygame
import window_manager, renderer


class Engine(object):
    # ========================
    # INITIALIZATION
    # ========================
    def __init__(self):
        """Initialize the engine with a WindowManager and set running state."""
        self.window = window_manager.WindowManager()
        self.renderer = renderer.Renderer(self.window.window)
        self.running = True

    # ========================
    # EVENT HANDLING
    # ========================
    def handle_events(self):
        """Process system and user events (quit, keys, etc.)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # ========================
    # MAIN LOOP
    # ========================
    def run(self):
        """Run the main engine loop: handle events, update, and render."""
        while self.running:
            self.handle_events()
            self.window.update()   # FPS + input update
            self.window.render()
