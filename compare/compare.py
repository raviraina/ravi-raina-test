"""
Question B
The goal of this question is to write a software library that accepts 2 version string
as input and returns whether one is greater than, equal, or less than the other. As an
example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
"""

class versionCompare:

    # init params
    def __init__(self, v1, v2):

        if v1.isalpha() or v2.isalpha():
            raise ValueError('Must enter version as: "x.x.x"')

        self.v1_ind = v1.split('.')
        self.v2_ind = v2.split('.')

        # strip unnecessary end 0's (i.e 1.2.0 --> 1.2)
        while int(self.v1_ind[-1]) == 0:
            self.v1_ind.pop()
        while int(self.v2_ind[-1]) == 0:
            self.v2_ind.pop()
        
        # rejoin versions without 0s and find min length
        self.v1 = '.'.join(str(i) for i in self.v1_ind)
        self.v2 = '.'.join(str(i) for i in self.v2_ind)
        self.min_length = min(len(self.v1_ind), len(self.v2_ind))

    # compare to see if versions are equal
    def equal(self):
        if self.v1 == self.v2:
            return 'Versions are equal'
        else:
            return 'Versions are not equal'
    
    # compare to see which version is greater
    def greater(self):
        if self.v1 == self.v2:
            return 'Neither are greater than the other'

        for i in range(self.min_length):
            if int(self.v1_ind[i]) > int(self.v2_ind[i]):
                return f'{self.v1} is greater than {self.v2}'
            elif int(self.v1_ind[i]) < int(self.v2_ind[i]):
                return f'{self.v2} is greater than {self.v1}'

        # case where min length values are equal but one version is longer
        if self.min_length == len(self.v1_ind):
            return f'{self.v2} is greater than {self.v1}'
        else:
            return f'{self.v1} is greater than {self.v2}'
    
    # compare to see which version is less
    def less(self):
        if self.v1 == self.v2:
            return 'Neither are less than the other'

        for i in range(self.min_length):
            if int(self.v1_ind[i]) < int(self.v2_ind[i]):
                return f'{self.v1} is less than {self.v2}'
            elif int(self.v1_ind[i]) > int(self.v2_ind[i]):
                return f'{self.v2} is less than {self.v1}'

        # case where min length values are equal but one version is longer
        if self.min_length == len(self.v1_ind):
            return f'{self.v1} is less than {self.v2}'
        else:
            return f'{self.v2} is less than {self.v1}'

def main():
    r = versionCompare('1.3', '1.4').greater()
    print(r)

if __name__ == "__main__":
    main()
