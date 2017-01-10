from solver import solver

def test_fb_solutions():
  points = [
    (57, 28, 81) #white
  ]
   
  rad = 50;
  
  assert solver(rad, points) ==  ["white"]