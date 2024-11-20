def bronKerbosch(p : set, x : set, r : set):

    if len(p) == 0 and len(x) == 0:
        self.cliquesMaximais.append(r)
        return
    
    for v in p:

        p_v = p.intersection(self.adj[v])
        x_v = x.intersection(self.adj[v])
        r_v = r.union(set(v))

        bronKerbosch(p_v, x_v, r_v)

        p.pop(v)
        x.add(v)
