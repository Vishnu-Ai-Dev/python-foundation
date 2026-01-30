#flatenning the matrix

'''matrix=[[1,2],[3,4],[6,7]]
flatten=[num for row in matrix for num in row]
print(flatten)'''

#flattening the matrix using conditions

'''matrix=[[1,2],[3,4],[5,6]]
flatten=[num for row in matrix for num in row if num>3]
print(flatten)'''

#squaring the numbers sin list

'''matrix=[[1,2,3],[6,7,8]]
square=[n*n for row in matrix for n in row]
print(square)'''

#using the condtional transformation in matrix

'''matrix=[[1,2,3],[8,9,10],[7,6,5]]
transformation=[n*2 if n>5 else n for row in matrix for n in row]
print(transformation)'''

#flattening the conditions micro task with condtions 

matrix=[[1,2,3],[4,5,6],[7,8,9]]
condition=[n*n for row in matrix for n in row if n%2==0 ]
print(condition)

