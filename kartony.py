from math import ceil, floor

class ToPack(object):
    '''cardboards object '''
    maly = 0
    sredni = 0
    duzy = 0
    zbiorczy = 0
    
    def packing(self, products: int ):
        ''' method to calculate required cardboards and types'''
        maly = (1,2,3)
        sredni=(4,5,6)
        duzy=(7,8,9)

        kartony = [maly,sredni,duzy]
        names = {maly: 'maly', sredni: 'sredni', duzy: 'duzy'}

        self.maly = 0
        self.sredni = 0
        self.duzy = 0
        self.zbiorczy = 0

        i = products
        
        if products > 0 and products < 100:

            # loop over cardboard types
            for karton in reversed(kartony):
                # loop over cardboard sizes
                for pojemnosc in reversed(karton):
                        if i <= 0:
                            break 
                        warunek =1
                        if i >= 10:
                            warunek = 2
                        if roundafter85(i, pojemnosc, products) >= warunek or pojemnosc <= i ==1 < products:
                        
                            cardboards = 1 if pojemnosc==1 else roundafter85(i, pojemnosc, products)
                            exec('self.{} +={}'.format(names[karton], cardboards))
                            i = i -(cardboards * karton[-1])
                            break
                if products >=10:
                    cardboards = self.maly + self.sredni + self.duzy
                    self.zbiorczy = ceil(cardboards/4)
        else:
            raise NameError('value is not in 1-100')
        return self


def roundafter85(i: float, pojemnosc: int, products: int):
    x = i/pojemnosc
    after_dot = x - int(x)
    
    if products >= 10 and after_dot >= 0.75  and i >= 6:
        return ceil(x)
    return floor(x)

def main():
    x = ToPack()
    x.packing(13) 
    print('mały {}'.format(x.maly))
    print('średni {}'.format(x.sredni))
    print('duży {}'.format(x.duzy))

if __name__ == "__main__":
    main()

