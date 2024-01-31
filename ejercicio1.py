x=[1, 2, 3, 3, 5, 5, 5, 6, 6, 7, 8, 9]


def slow_find_pair_sums(x,n):
   pairs=set()
   for i in range(len(x)):
    for j in range(len(x)):
      if i != j:
        if x[i]+x[j]==n:
          if  x[i] < x[j]:
              pairs.add((x[i],x[j]))
          else:
            pairs.add((x[i],x[j]))
    return pairs 
           
slow_find_pair_sums(x,10)
