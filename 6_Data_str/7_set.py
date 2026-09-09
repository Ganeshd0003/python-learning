# NOTE we cannot access set with indexing

my_set = {"aa","ww","mm"}
print(my_set)

# add initial items
my_set.add("cc")
print(my_set)

# add 10 more items
my_set.update(["bb","dd","ee","ff","gg","hh","ii","jj"])
print(my_set)

sorted(my_set)
print(my_set)

my_set.pop()
my_set.pop()
print(sorted(my_set))

my_set.remove("aa")
my_set.discard("aaa")
print(sorted(my_set))


print(type(my_set))