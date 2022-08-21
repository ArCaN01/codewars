def recoverSecret(triplets):
    r = []
    for i in range(len(triplets)):
        for l in range((len(triplets[i]))):
            r.append(triplets[i][l])


    r = set(r)
    r = list(r)


    while True:
        count = 0


        for i in range(len(triplets)):
            for l in  range(len(triplets[i]) - 1):
                first = triplets[i][l]
                second = triplets[i][l + 1]
                index_f = r.index(first)
                index_s = r.index(second)
                if index_f > index_s:
                    r[index_f], r[index_s] = r[index_s], r[index_f]
                    count =+ 1

        if count == 0:
            return ''.join(r)
