from objects import ELEMENTS_FOR_RENDER, INGREDIENTS, SLOTS
from items import Ingredient

hold = None
blocked = False

def setup():
    size(1500, 900)
    rectMode(CENTER)
    
    
def draw():
    global blocked, hold
    background(255)
    
    for element in ELEMENTS_FOR_RENDER:
        element.draw()
        for slot in SLOTS:
            if isinstance(element, Ingredient) and element.intersects(slot):
                element.slot = slot
                element.move_to_slot()

    if hold:
        hold.x = mouseX
        hold.y = mouseY
        
        
def mousePressed():
    global hold, blocked
    if blocked:
        return
    for ingredient in INGREDIENTS:
        if ingredient.cur_collision(mouseX, mouseY):
            hold = ingredient
            blocked = True


def mouseReleased():
    global blocked, hold
    hold = None
    blocked = False
