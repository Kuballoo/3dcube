import SETTINGS

class Renderer:
    # ========================
    # INITIALIZATION
    # ========================
    def __init__(self, window):
        """Initialize the renderer with a window surface and font."""
        self.window = window

    # ========================
    # RENDERING
    # ========================
    def render_objects(self, objects):
        """Render objects (single object or list).  
        Each object must implement a `render(window)` method.
        """
        if isinstance(objects, list):
            for obj in objects:
                self.render_objects(obj)  # recursive rendering
        else:
            objects.render(self.window)