from shapes import Rectangle, Circle
from configs import images


class Ingredient(Rectangle):
    def __init__(self, type_, level, x, y, slot=None, **kwargs):
        super(Ingredient, self).__init__(x, y, w=70, h=70)
        self.type = type_
        self.level = level
        self.slot = slot    
        self.image_path = images[type_.lower()]
        
    def draw(self):
        super(Ingredient, self).draw(CENTER)
        fill(255)
        img = loadImage(self.image_path)
        imageMode(CENTER)
        image(img, self.x, self.y, self.w, self.h)
        fill(0)
        textSize(24)
        rectMode(CENTER)
        textAlign(CENTER)
        text(str(self.level) + "lvl", self.x, self.y + self.h/2, self.w, self.h)
        rectMode(CORNER)
        
    def move_to_slot(self):
        self.x = self.slot.x
        self.y = self.slot.y
    
    def intersects(self, slot):
        circle_distance_x = abs(slot.x - self.x)
        circle_distance_y = abs(slot.y - self.y)
        if circle_distance_x > self.w / 2 + slot.r or circle_distance_y > self.h / 2 + slot.r:
            return False
            return False
        if circle_distance_x <= self.w / 2:
            return True
        if circle_distance_y <= self.h / 2:
            return True
        corner_distance_sq = (circle_distance_x - self.w / 2) ** 2 + (circle_distance_y - self.h / 2) ** 2
        return corner_distance_sq <= (slot.r ** 2)
        
    def __repr__(self):
        return 'Ingredient {}, level {}'.format(self.type, self.level)


class Slot(Circle):
    def __init__(self, x, y, r=80, **kwargs):
        super(Slot, self).__init__(x, y, r, **kwargs)
    
    def __repr__(self):
        return 'Slot {}'.format(id(self))
    

class Inventory(Rectangle):
    def __init__(self, x, y, w, h, **kwargs):
        super(Inventory, self).__init__(x, y, w, h, **kwargs)
        
    

    
