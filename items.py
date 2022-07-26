from shapes import Rectangle, Circle, BaseShape
from config import images


class Ingredient(Rectangle):
    def __init__(self, type, level, x, y, slot=None, **kwargs):
        super(Ingredient, self).__init__(x, y, w=70, h=70, **kwargs)
        self.type = type
        self.level = level
        self.slot = slot    
        self.image_path = images[type.lower()]
        self.default = {'x': x, 'y': y}
        
    def draw(self):
        fill(0)
        super(Ingredient, self).draw(CENTER)
        img = loadImage(self.image_path)
        imageMode(CENTER)
        image(img, self.x, self.y, self.w, self.h,)
        
        textSize(24)
        rectMode(CENTER)
        textAlign(CENTER)
        text(str(self.level) + "lvl", self.x, self.y + self.h/2, self.w, self.h)
        rectMode(CORNER)
        
    def move_to_slot(self):
        self.x = self.slot.x
        self.y = self.slot.y
    
    def move_to_back(self):
        self.x = self.default['x']
        self.y = self.default['y']
    
    
    def intersects(self, slot):
        circle_distance_x = abs(slot.x - self.x)
        circle_distance_y = abs(slot.y - self.y)
        if circle_distance_x > self.w / 2 + slot.r or circle_distance_y > self.h / 2 + slot.r:
            return False
        if circle_distance_x <= self.w / 2 or circle_distance_y <= self.h / 2:
            return True
        corner_distance_sq = (circle_distance_x - self.w / 2) ** 2 + (circle_distance_y - self.h / 2) ** 2
        return corner_distance_sq <= (slot.r ** 2)
        
    def __repr__(self):
        return 'Ingredient {}, level {}'.format(self.type, self.level)


class Slot(Circle):
    def __init__(self, x, y, r=65, **kwargs):
        super(Slot, self).__init__(x, y, r)
        self.items = []
        self.kwargs
    
    def __repr__(self):
        return 'Slot {}'.format(id(self))
    

class Inventory(Rectangle):
    def __init__(self, x, y, w, h, **kwargs):
        super(Inventory, self).__init__(x, y, w, h, **kwargs)
        self.slots = []
        
        
class Text(BaseShape):
    def __init__(self, x, y, w, h, text, text_size, **kwargs):
        super(Text, self).__init__(x, y, w, h, **kwargs)
        self.text = text
        self.text_size = text_size
        self.kwargs
        
    def draw(self):
        super(Text, self).draw()
        textSize(self.text_size)
        textAlign(CENTER)
        text(self.text, self.x, self.y, self.w, self.h)
        
        
class Button(Rectangle):
    def __init__(self, x, y, w, h, text, action, **kwargs):
        super(Button, self).__init__(x, y, w, h, **kwargs)
        self.text = text
        self.action = action
        self.default_color = '#7785a4'
        self.pressed_color = '#ff0400'
        self.current_color = self.default_color
        
    def draw(self):
        fill(self.current_color)
        super(Button, self).draw(CENTER)
        textSize(24)
        fill(0)
        rectMode(CENTER)
        textAlign(CENTER, CENTER)
        text(self.text, self.x, self.y - 2)
        rectMode(CORNER)

    def set_pressed_color(self):
        self.current_color = self.pressed_color
    
    def set_default_color(self):
        self.current_color = self.default_color
        
    def run(self, *args, **kwargs):
        self.action(*args, **kwargs)
            
