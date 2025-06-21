
def listDuplicates(Dict):

    List = []

    for values in Dict.values():

        for v in range(1, len(values)):
            List.append(values[v])

    return List