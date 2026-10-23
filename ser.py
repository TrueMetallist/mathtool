def terms(tip, term):
    slug = []

    if tip == 'third':
            S = 1/3
            for i in range (2, int(term+1)):
                if (3*i) % 2 == 0:
                    S -= 1/(3*i)
                    slug.append(' - 1/'+str(3*i))
                else:
                    S += 1/(3*i)
                    slug.append(' + 1/'+str(3*i))
            res = ''
            for n in range(len(slug)):
                res += slug[n]
            print('S = 1/3', res)
            print('Слагаемых: ', int(term))
            print('Сумма ряда: ', round(S, 5))

    elif tip == 'sqplus':
                S = 0.5
                for i in range (2, int(term+1)):
                    if i % 2 == 0:
                        S -= 1/((i**2)+1)
                        slug.append(' - 1/('+str(i)+'^2'+'+1)')
                    else:
                        S += 1/((i**2)+1)
                        slug.append(' + 1/('+str(i)+'^2'+'+1)')
                res = ''
                for n in range(len(slug)):
                    res += slug[n]
                print('S = 1/(1^2+1)', res)
                print('Слагаемых: ', int(term))
                print('Сумма ряда: ', round(S, 5))
    trm = int(term)
    return res, trm, S

def epsil(tip, eps):
    slug = []

    if tip == 'third':
                i = 2
                S = 1/3
                while eps < 1/(3*i):
                    if (3*i) % 2 == 0:
                        S -= 1/(3*i)
                        slug.append(' - 1/'+str(3*i))
                    else:
                        S += 1/(3*i)
                        slug.append(' + 1/'+str(3*i))
                    i += 1
                res = ''
                for n in range(len(slug)):
                    res += slug[n]
                print('S = 1/3', res)
                print('Слагаемых: ', len(slug)+1)
                print('Сумма ряда: ', round(S, 5))

    elif tip == 'sqplus':
                i = 2
                S = 0.5
                while eps < 1/((i**2)+1):
                    if i % 2 == 0:
                        S -= 1/((i**2)+1)
                        slug.append(' - 1/('+str(i)+'^2'+'+1)')
                    else:
                        S += 1/((i**2)+1)
                        slug.append(' + 1/('+str(i)+'^2'+'+1)')
                    i += 1
                if i % 2 == 0:
                    S -= 1/((i**2)+1)
                    slug.append(' - 1/('+str(i)+'^2'+'+1)')
                else:
                    S += 1/((i**2)+1)
                    slug.append(' + 1/('+str(i)+'^2'+'+1)')
                res = ''
                for n in range(len(slug)):
                    res += slug[n]
                print('S = 1/(1^2+1)', res)
                print('Слагаемых: ', len(slug)+1)
                print('Сумма ряда: ', round(S, 5))
    slg = len(slug)
    return res, slg, S