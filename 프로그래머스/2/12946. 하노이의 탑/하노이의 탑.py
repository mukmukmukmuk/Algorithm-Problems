answer = []
def solve(s,e,by,n):
    if n==0: return
    solve( s,by,e,n-1)
    answer.append([s,e])
    solve( by,e,s,n-1)
    
def solution(n):
    solve(1,3,2,n)
    return answer