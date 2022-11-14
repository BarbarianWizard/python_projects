def hello(): 
    print ("Hello, user!")


def pack(sandwich, apple, yogurt, twix):
    return [sandwich, apple, yogurt, twix]

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(pack("sandwich","apple","yogurt","twix"))
print(pack(0,1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["sandwich","apple","yogurt","twix"])