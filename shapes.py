class BaseShape(object):
    def __init__(self, x, y, w, h, **kwargs):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.kwargs = kwargs
        
    def draw(self):
        if self.kwargs.get('fill'):
            fill(self.kwargs['fill'])


class Rectangle(BaseShape):
    def __init__(self, x, y, w, h, r=0, **kwargs):
        super(Rectangle, self).__init__(x, y, w, h, **kwargs)
        self.r = r
        self.kwargs = kwargs
    
    def cur_collision(self, cur_x, cur_y):
        return (self.x - self.w / 2 <= cur_x <= self.x + self.w / 2) \
            and (self.y - self.h / 2 <= cur_y <= self.y + self.h / 2)
    
        
    def draw(self, center=None):
        super(Rectangle, self).draw()
        if center == CENTER:
            rectMode(CENTER)
    
        rect(self.x, self.y, self.w, self.h, self.r)
        rectMode(CORNER)


class Circle(BaseShape):
    def __init__(self, x, y, r, **kwargs):
        super(Circle, self).__init__(x, y, r * 2, r * 2, **kwargs)
        self.r = r  # radius
        self.kwargs = kwargs
        
    def cur_collision(self, cur_x, cur_y):
        return dis(cur_x, cur_y, self.x, self.y) <= self.r

    def draw(self):
        super(Circle, self).draw()
        fill('#20fc03')
        ellipse(self.x, self.y, self.r * 2, self.r * 2)
