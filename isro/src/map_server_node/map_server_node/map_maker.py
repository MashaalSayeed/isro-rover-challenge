from enum import IntEnum
from dataclasses import dataclass
from typing import Tuple
from geometry_msgs.msg import Pose

import numpy as np


RED = (255, 0, 0)
YELLOW = (220, 220, 0)
GREEN = (0, 255, 0)
BLUE = (50, 164, 168)
GRAY = (150, 150, 150)
ORANGE = (205, 100, 0)
DARKORANGE = (204, 99, 0)
PURPLE = (255, 0, 255)
DARKPURPLE = (119, 50, 168)
WHITE = (255,255,255)

class ObjectType(IntEnum):
  SmallObstacle = 1
  BigObstacle = 2
  SmallCrater = 3
  BigCrater = 4
  Waypoint = 5
  StartPoint = 6
  FinalPoint = 7
  Final = 8
  Tube = 9

@dataclass
class Object:
  tag: ObjectType
  cost: int
  color: Tuple[int, int, int]
  width: int = None
  height: int = None
  radius: int = None

class AddObject:
  pose: Pose
  tag: int


object_map = {
  ObjectType.SmallObstacle: Object(ObjectType.SmallObstacle, 15, YELLOW, width=15, height=15),
  ObjectType.BigObstacle: Object(ObjectType.BigObstacle, 60, GREEN, width=30, height=30),
  ObjectType.SmallCrater: Object(ObjectType.SmallCrater, 20, PURPLE, radius=10),
  ObjectType.BigCrater: Object(ObjectType.BigCrater, 60, DARKPURPLE, radius=20),
  ObjectType.Waypoint: Object(ObjectType.Waypoint, -10, GRAY, width=110, height=110),
  ObjectType.StartPoint: Object(ObjectType.StartPoint, 0, ORANGE, width=120, height=120),
  ObjectType.FinalPoint: Object(ObjectType.FinalPoint, -10, DARKORANGE, radius=75),
  ObjectType.Final: Object(ObjectType.Final, -10, BLUE, width=10, height=20),
  ObjectType.Tube: Object(ObjectType.Tube, -10, RED, width=8, height=12)
}

# color_map = {
#   YELLOW: "A1",
#   GREEN: "A2",
#   PURPLE: "B1",
#   DARKPURPLE: "B2",
#   GRAY: ObjectType.Waypoint,
#   ORANGE: "SP",
#   DARKORANGE: "FP",
#   BLUE: ObjectType.Final,
#   RED: "T"
# }

def add_object(map: np.array, obj1: AddObject):
  width, height = map.shape
  center_x = int(obj1.pose.position.x * 100)
  center_y = -int(obj1.pose.position.y * 100)
  if obj1.tag == 0:
    return
  
  obj = object_map[obj1.tag]
  xx = np.mgrid[:width]
  yy = np.mgrid[:width]

  def draw_circle(obj: Object, center_x, center_y):
    radius = obj.radius or obj.width
    circle = (xx - center_x) ** 2 + (yy - center_y) ** 2 < radius ** 2
    map[circle] = obj.tag

  def draw_square(obj: Object, center_x, center_y):
    square = np.logical_and((xx - center_x) > 0, (xx - center_x) < obj.width) & np.logical_and((yy - center_y) > 0, (yy - center_y) < obj.height)
    map[square] = obj.tag

  draw_circle(obj, center_x, center_y)

  return map


def make_costmap(map: np.array):
  width, height = map.shape
  costmap = [0] * (width * height)
  for i in range(height):
    for j in range(width):
      if map[j][i] == 0:
        continue
  
      obj = object_map[int(map[j][i])]
      costmap[i*width + j] = 100#obj.cost
    
  return costmap