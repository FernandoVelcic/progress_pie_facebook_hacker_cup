import numpy as np
 
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(x, y)
    if (phi < 0):
      phi = (2*np.pi + phi)
    return(rho, phi)
   
def pointInCircle(rad, p, rho, angle):
  if rho > rad:
    return False
  elif angle > p/50*np.pi: #Rotate
    return False
  else:
    return True

def solve(rad, p, x, y):
  point_pol = cart2pol(x,y)
  result =  pointInCircle(rad, p, point_pol[0], point_pol[1])
  
  return "black" if result is True else "white"

def solver(rad, points):
  #Move all points to (0, 0)
  moved_points = list(map(lambda p_x_y: (p_x_y[0], p_x_y[1]-rad, p_x_y[2]-rad), points))

  #Solve all points
  return list(map(lambda p_x_y: solve(rad, p_x_y[0], p_x_y[1], p_x_y[2]), moved_points))