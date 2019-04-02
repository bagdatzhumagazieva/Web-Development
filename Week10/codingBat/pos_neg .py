def pos_neg(a, b, negative):
  if negative:
    return a<0 and a*b>0
  else:
    return a*b<0
