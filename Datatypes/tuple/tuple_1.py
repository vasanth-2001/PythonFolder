# roll_number=(123,124,134,157,135)
# mixed_type=('subham',123,True,78.9)
# print("length of roll number : ",len(roll_number)," length of mixed_type : ",len(mixed_type))
# print(mixed_type[0])
# print(mixed_type[2])
# print(mixed_type[-3:-1])
# print(roll_number[-4:])

# roll=(123)
# print(roll,type(roll))

# rollNum=(123,)
# print(rollNum,type(rollNum))

employ_detail=('subham',123,'trainer')
(name,jobid,jobrole)=employ_detail
print(name)

employ_detail=('shubam','trainer','admin',123)
(name,*jobrole,jobid)=employ_detail   #unpacking   -- * will take two values
print(jobrole)
print(jobid)