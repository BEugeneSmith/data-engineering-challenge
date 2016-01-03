#!/usr/bin/python3
from json import dumps
from sys import argv

class Recombine:

    def __init__(self,ds_str):
        self.ds = self.__parse_input(ds_str)
        self.ds_recombined = self.__recombine()
        self.json = self.__to_json()

    def __parse_input(self,ds_str):
        ''' returns parsed data structure from string input '''
        null = None
        return eval(ds_str)

    def __recombine(self):
        ''' returns recombined data structure if valid '''
        if all([type(x)==list for x in self.ds]) == True:
            return self.__recombine_list()
        elif all([type(x)==dict for x in self.ds]) ==True:
            return self.__recombine_dict()
        else:
            return 'unrecognized data structure'

    def __flatten(self,l):
        ''' returns unique flattened list of elements '''
        y = []
        for i in l:
            y += i
        return sorted(set(y))

    def __recombine_list(self):
        ''' returns recombined list '''
        recombined_list = {}
        ids = self.ds[0]
        vals = self.ds[1:len(self.ds)]

        for i in range(len(ids)):
            recombined_list[ids[i]] = list(map(lambda x: x[i],vals))

        return recombined_list

    def __recombine_dict(self):
        ''' returns recombined dictionary '''
        recombined_dict = {}
        ids = self.__flatten([list(x.keys()) for x in self.ds])

        for i in ids:
            recombined_dict[i] = []
            for j in self.ds:
                if i in j:
                    recombined_dict[i].append(j[i])
                else:
                    recombined_dict[i].append(None)


        return recombined_dict

    def __to_json(self):
        ''' return recombined data structure as json '''
        return dumps(self.ds_recombined,sort_keys=True)

if __name__ == '__main__':
    try:
        ds_rec = Recombine(argv[1])
        print(ds_rec.json)
    except:
        print('\tenter data structure for recombination')
