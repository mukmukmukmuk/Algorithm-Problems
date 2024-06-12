def solution(g, p):
    answer = []
    music={}
    al={}
    for i in range(len(g)):
        if g[i] in music:
            music[g[i]]+=p[i]
        else: music[g[i]]=p[i]
        if g[i] not in al:
            al[g[i]]=[i]
        else: al[g[i]].append(i)
    for k,v in al.items():
        v.sort(key=lambda x: (-p[x],x))
    st=list(music.items())
    st.sort(key=lambda x: -x[1])
    
    for cur in st:
        answer.extend(al[cur[0]][:2])
            
    return answer