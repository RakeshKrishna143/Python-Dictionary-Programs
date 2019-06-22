dylan = { "name" : "Dylan Rhodes", 
          "assignment" : [77, 82, 23, 39], 
          "test" : [78, 77], 
          "lab" : [80, 80] 
        } 
jack = { "name":"Jack Frost", 
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       } 
def get_avg(l):
    return sum(l)/len(l)
def tot_avg(i):
    a=get_avg(i['assignment'])
    t=get_avg(i['test'])
    l=get_avg(i['lab'])
    return a*.1 + t*.7 + l*.2

def grade(avg_mark):
    if avg_mark>=90:
        return 'A'
    elif avg_mark >=80:
        return 'B'
    elif avg_mark>=70:
        return 'C'
    elif avg_mark>=60:
        return 'D'
    elif avg_mark>=55:
        return 'E'
    else:
        return 'F'
        
cls_res = []
student=[dylan,jack]
for i in student:
    print(tot_avg(i))
    cls_res.append(tot_avg(i))
    print(grade(tot_avg(i)))
print(cls_res)
print(get_avg(cls_res))
print(grade(get_avg(cls_res)))
    
