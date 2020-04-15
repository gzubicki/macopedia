class ToPack(object):
    maly = 0
    sredni = 0
    duzy =0
    zbiorczy = 0
    
    def packing(self, products: int ):
        maly = (1,2,3)
        sredni=(4,5,6)
        duzy=(7,8,9)

        kartony = [maly,sredni,duzy]
        names = {maly: 'maly', sredni: 'sredni', duzy: 'duzy'}

        self.maly = 0
        self.sredni =0
        self.duzy =0

        i = products
        
        if products > 0 and products < 100:
    
            for karton in reversed(kartony):
                for pojemnosc in reversed(karton):
                        if i <= 0:
                            break 
                        print('pojemnosc {}'.format(pojemnosc))
                        warunek =1
                        if i >= 10:
                            warunek = 2
                        # print('round  {} '.format(round(i / pojemnosc) ))
                        if i // pojemnosc >= warunek:
                            
                            cardboards = i // pojemnosc
                            exec('self.{} +={}'.format(names[karton], cardboards))
                            i = i -(cardboards * karton[-1])
                            print('dodaje poj {} sztuk {}, teraz i = {}'.format(pojemnosc, cardboards, i))
        else:
            raise NameError('value is not in 1-100')
        return self

def main():
    x = ToPack()
    x.packing(13) 
    print('mały {}'.format(x.maly))
    print('średni {}'.format(x.sredni))
    print('duży {}'.format(x.duzy))

if __name__ == "__main__":
    main()

