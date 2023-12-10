def maskify(cc):
    for i in cc:
        if len(cc) > 4:
            x = cc[:-4]
            m =  "#" * len(x)
            return cc.replace(x, m)
    return cc