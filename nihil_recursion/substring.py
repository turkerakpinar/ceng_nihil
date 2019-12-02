def helper_string(str,n):
    if  n == len(str) :
       return [str]
    else:
        return [str[:n]] + helper_string(str,n+1)
 
def substrings(str):
    if len(str) == 0:
        return []
    else:
        return helper_string(str,1) +substrings(str[1:])
