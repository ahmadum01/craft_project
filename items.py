from shapes import Rectangle, Circle


class Ingredient(Rectangle):
    def __init__(self, type_, level, x, y, slot=None, **kwargs):
        super(Ingredient, self).__init__(x, y, w=100, h=100)
        self.type = type_
        self.level = level
        self.slot = slot
        
    def draw(self):
        super(Ingredient, self).draw()
        fill(255)
        textSize(20)
        textAlign(CENTER)
        text('Ingredient\n{}\n{}'.format(self.type, self.level), self.x, self.y, self.w, self.h)
        
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
    

    
