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

