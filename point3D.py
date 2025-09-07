from SETTINGS import DEBUG, POINT
import Debugger


class Point3D(Debugger.Debugger):
    def __init__(self, x, y, z):
        super().__init__(name='Point3D', enabled=DEBUG['POINT3D'])
        self.x = x
        self.y = y
        self.z = z

        self.show_debug_data('coordinates', x=self.x, y=self.y, z=self.z)
        
    
