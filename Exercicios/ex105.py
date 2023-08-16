def notas(*args, sit=False):
    r = {}
    r['total'] = len(args)
    r['maior'] = max(args)
    r['menor'] = min(args)
    r['media'] = sum(args) / len(args)

    if sit:
        if r['media'] >= 7:
            r['situação'] ='Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
