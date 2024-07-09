rand = ["apple","banana",35,"22.4",True,[1,2]]
rand.append("mango")         #adds element at the last 
rand.pop(4)                  # deletes the indexed element
print(rand.count("apple"))   #counts the number of ocurrence
rand[2] = "peach"            # updates the indexed element
print(rand)                  
print(type(rand))

fruits = {"apple","mango","banana","peach"} # a set of fruits
print(type(fruits))
fruits.add("guava")          #adds the element 
fruits.remove("mango")       #removes the element
more = ["pineapple"]         
fruits.update(more)          #updates the set with new elements
print(fruits)

dict1 ={
    "roll_no":1,
    "name":"rohan",
    "marks":22
}
dict1["roll_no"] = 2            #change the value of the key
dict1["subject"] = "maths"      #inserts new key value pair
dict1.update({"year":2004})     #updates the dictionary
print(dict1)
print(type(dict1))


