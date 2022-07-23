class BaseShape(object):
    pass


class Rectangle(BaseShape):
    def __init__(self, x, y, w, h, **kwargs):
        super(Rectangle, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def cur_collision(self, cur_x, cur_y):
        return (self.x - self.w / 2 <= cur_x <= self.x + self.w / 2) \
            and (self.y - self.h / 2 <= cur_y <= self.y + self.h / 2)
    
        
    def draw(self):
        fill(0)
        rect(self.x, self.y, self.w, self.h)


class Circle(BaseShape):
    def __init__(self, x, y, r, **kwargs):
        super(Circle, self).__init__()
        self.x = x
        self.y = y
        self.r = r  # radius
        
    def cur_collision(self, cur_x, cur_y):
        return dis(cur_x, cur_y, self.x, self.y) <= self.r

    def draw(self):
        fill('#20fc03')
        ellipse(self.x, self.y, self.r * 2, self.r * 2)
