#ül08
#aksel ratt
#08.03.22

class auto:
    #atribuudid
    mark='teadmata'
    aasta=0
    hind='teadmata'
    
    #meetodid
    def lisamark(self,a):
        self.mark=a
        
    def lisaaasta(self,b):
        self.aasta=b
        
    def lisahind(self,c):
        self.hind=c
        
    def kuva(self):
        print('mark: {} \naasta: {} \nhind:{}'.format(self.mark, self.aasta,self.hind))
        
auto()
auto.lisamark('mersu')
auto.lisaasta('2000')
auto.lisahind('3000')
auto.kuva()

print()