from objects import ELEMENTS_FOR_RENDER, INGREDIENTS, SLOTS
from items import Ingredient
from objects import crafting_button
import config
from tools import group_ingredients
from helpers import check_move_to_back

hold = None
blocked = False


def setup():
    size(config.screen_w, config.screen_h)
    # rectMode(CENTER)
    strokeWeight(5)
    # frameRate(100)
    
    
def draw():
    global blocked, hold
    background(255)
    
    for element in ELEMENTS_FOR_RENDER:
        element.draw()
        if element not in INGREDIENTS:
            continue
        for slot in SLOTS:
            if isinstance(element, Ingredient) and element.intersects(slot):
                element.slot = slot
                element.move_to_slot()

            elif not check_move_to_back(element):
                element.move_to_back()
                    

    if hold:
        hold.x = mouseX
        hold.y = mouseY
        
        
def mousePressed():
    global hold, blocked
    
    if crafting_button.cur_collision(mouseX, mouseY):
        crafting_button.run()
    
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

    
    
    
