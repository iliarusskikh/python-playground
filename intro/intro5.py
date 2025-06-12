#finding common elements

set_a = {1,2,3,4}
set_b = {7,2,9,4}
common = set_a & set_a #{2,4}

#dictionary comprehensions

user_scores = {name: score for name,score in zip(users,scores)}

#list compr
squares = [i*i for i in range(10)]
