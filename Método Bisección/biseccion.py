import math

def f(c):
  g = 9.81
  m = 68.1
  t = 10
  v = 40
  return (g*m/c)*(1-math.exp(-(c/m)*t))-v



def biseccion(x1,x2,e,f):             
  if f(x1)*f(x2) > 0:
    print('x1 y x2 no tiene sentido')                   
    return

                          
  an = x2
  anmenos1 = x1
  error = abs(an - anmenos1)
  
  
  while error > e:

    a = (x1+x2)/2
    if f(a)*f(x1) > 0:
      x1 = a
    elif f(a)*f(x2) < 0:
      x2 = a
    anmenos1 = a
  return a
   
print(biseccion(0.1,90,0.1,f))
