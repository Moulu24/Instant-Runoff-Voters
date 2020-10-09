
voters = [['Abelt Dessler', 'Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Frank Underwood', 'Gihren Zabi'], ['Brian J. Mason', 'Gihren Zabi', 'Abelt Dessler', 'Johan Liebert', 'Frank Underwood', 'Drake Luft'], ['Frank Underwood', 'Abelt Dessler', 'Johan Liebert', 'Drake Luft', 'Brian J. Mason', 'Gihren Zabi'], ['Drake Luft', 'Johan Liebert', 'Frank Underwood', 'Gihren Zabi', 'Abelt Dessler', 'Brian J. Mason'], ['Frank Underwood', 'Brian J. Mason', 'Drake Luft', 'Gihren Zabi', 'Johan Liebert', 'Abelt Dessler']]
def runoff(voters):
    l = []
    for i in voters :
        l.append(i[0])
    b = set(l)
    if len(b) == 1:
        return l[0]
    else : 
        maxi = l[0]
        for i in b:
            if l.count(i) > l.count(maxi):
                maxi = i
        mini = l[0]
        mi = [mini]
        for i in b:
            if l.count(i) < l.count(mini):
                mi = []
                mini = i
                mi.append(mini)
            elif l.count(i) == l.count(mini):
                mi.append(i)
        if mini == maxi :
            return None
        if l.count(maxi) > len(voters)/2 :
            return maxi
        else :
            for i in voters:
                for j in set(mi):
                    i.remove(j)
            m = 1
            return runoff(voters)