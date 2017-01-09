from solver import solver

def test_fb_example():
  points = [
    (0, 55, 55),  #white
    (12, 55, 55), #white
    (13, 55, 55), #black
    (99, 99, 99), #white
    (87, 20, 40)  #black
  ]
   
  rad = 50;
  
  assert solver(rad, points) ==  ["white", "white", "black", "white", "black"]