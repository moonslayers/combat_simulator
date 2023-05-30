import random

class Combatiente:
  def __init__(self):
    self.fisico={}
    self.mental={}
    self.nofisico={}
    self.psico={}
    self.hemo=[]
    self.fatiga='Fresco'
    self.fatigan=0
    self.estado="normal"
    self.first=0
    self.ataque=0
    self.defensa=0
    self.counter=0
  def setFisico(self,fue,agil,peso,res,const,armor):
    self.fisico['fue']=fue
    self.fisico['agi']=agil
    self.fisico['peso']=peso+armor*4
    self.fisico['res']=res
    self.fisico['cons']=const
    self.fisico['arm']=armor
    self.sangre=70*peso
    self.sangrept=random.randrange(10,16)+const/2
    self.sangrePe=70*peso
    self.armor=armor/2*1000+500
    self.armorlost=[]
  def setMental(self,refle,exp,estil,vision,tecnica):
    self.tecnica=tecnica
    self.mental['ref']=refle
    self.mental['exp']=exp
    self.mental['est']=estil
    self.mental['vis']=vision
  def setNofisico(self,inte,sab,ast,pac,aut):
    self.nofisico['int']=inte
    self.nofisico['ast']=ast
    self.nofisico['sab']=sab
    self.nofisico['pac']=pac
    self.nofisico['aut']=aut
  def setPsico(self,mor,conf,cone,ada,conc):
    self.psico['mor']=mor
    self.psico['conf']=conf
    self.psico['cone']=cone
    self.psico['ada']=ada
    self.psico['conc']=conc
  def setRandom(self):
    self.setFisico(random.randrange(1,11),random.randrange(1,11),random.randrange(50,101),random.randrange(1,11),random.randrange(1,11),random.randrange(1,10))
    self.setNofisico(random.randrange(1,11),random.randrange(1,11),random.randrange(1,11),random.randrange(1,11),random.randrange(1,11))
    self.setPsico(random.randrange(1,11),random.randrange(1,11),random.randrange(1,11),random.randrange(1,11),random.randrange(1,11))
    tecnicas=["Espada","Dos espadas","Espada y escudo","Espada larga","Hacha y escudo", "Lanza y escudo"]
    self.setMental(random.randrange(1,11),random.randrange(1,11),random.randrange(1,6),random.randrange(1,11),random.choice(tecnicas))
  def printf(self):
    print("Atributos")
    print(self.fisico)
    print(self.mental)
    print(self.psico)
    print(self.nofisico)
    print("Variables")
    print("Volumen sanguinieo: ",self.sangre)
    print("Pt limite sanguinieo: ",self.sangrept)
    print("tecnica:",self.tecnica)
    print("fatiga: ",self.fatiga)
    print("armor: ",self.armor)


class Combate:
  def __init__(self, c1:Combatiente,c2:Combatiente,verbose=False):
    self.cs=[]
    self.cs.append(c1)
    self.cs.append(c2)
    self.asaltos=0
    self.ganador=''
    self.rand=4
    self.dblood=40
    self.darmor=30
    self.verbose=verbose

  def setCs(self,c1,c2):
    self.cs[0]=c1
    self.cs[1]=c2
    
  def whofirst(self):
    t=0
    lt=range(self.rand)
    tm=[0,0]
    for c in self.cs:
      tm[t]=c.mental["est"]*2+c.mental['exp'] + sum(random.choices(lt,k=2))
      +(c.fisico['agi']*10-c.fisico['peso']) + sum(random.choices(lt,k=2))
      +c.psico['conf'] + c.psico['mor'] + c.psico['ada']*self.asaltos/10  + sum(random.choices(lt,k=3))
      +c.nofisico['sab']+ c.nofisico['ast'] - c.nofisico['pac'] + sum(random.choices(lt,k=3))
      t=t+1
    self.asaltos+=1
    if tm[0]>tm[1]:
      if self.verbose: print("c1 ataca a c2 [",tm[0],",",tm[1],"]")
      self.cs[0].first+=1
      self.ataque(0)
    elif tm[1]>tm[0]:
      if self.verbose: print("c2 ataca a c1 [",tm[1],",",tm[0],"]")
      self.cs[1].first+=1
      self.ataque(1)
    else:
      p= random.randrange(2)
      self.cs[p].first+=1
      self.ataque(p)

  def ataque(self,c):
    c1=self.cs[c]
    lt=range(self.rand)
    if c==1:
      i=0
    elif c==0:
      i=1
    
    if c1.estado=="mareos":
      mareos1=20
      if self.verbose: print("c",c+1," ataca mareado")
    else:
      mareos1=0

    c2=self.cs[i]
    ataque=c1.fisico['fue']*2 + (c1.fisico['agi']*10-c1.fisico['peso']) + sum(random.choices(lt,k=3)) -(c1.fatigan-1)*2
    +c1.nofisico['int'] + c1.nofisico['ast'] + c1.nofisico['aut'] + sum(random.choices(lt,k=3)) -(c1.fatigan-3)*3
    +c1.psico['conf']+c1.psico['conc'] + sum(random.choices(lt,k=2)) -(c1.fatigan)*2
    +c1.mental['exp']+c1.mental['vis'] + sum(random.choices(lt,k=2)) -(c1.fatigan-2)*2 -mareos1

    if c2.estado=="mareos":
      mareos=20
      if self.verbose: print("c",i+1," defiende mareado")
    else:
      mareos=0

    defensa=c2.fisico['fue']*2 + (c2.fisico['agi']*10-c2.fisico['peso'])  + sum(random.choices(lt,k=3)) -(c2.fatigan-1)*2
    +c2.nofisico['sab'] + random.randrange(4) -(c2.fatigan-3)
    +c2.psico['ada']*self.asaltos/10 +c2.psico['conc']+ c2.psico['cone']+ sum(random.choices(lt,k=3)) -(c2.fatigan)*3
    +c2.mental['ref']*2+c2.mental['vis']+c2.mental['exp'] + sum(random.choices(lt,k=3))-(c2.fatigan-2)*3 - mareos

    if c1.estado=="desmayo":
      ataque=0
      if self.verbose: print("c",c+1," esta desmayado...")


    if c2.estado=="desmayo":
      defensa=0
      if self.verbose: print("c",i+1," esta desmayado...")

    if ataque> defensa:
      if self.verbose: print("Ataque existoso de c",c+1," [",ataque,",",defensa,"]")
      self.cs[c].ataque+=1
      self.daño(c,(ataque-defensa))
    else:
      self.cs[i].defensa+=1
      if self.verbose: print("Defensa existosa de c",i+1," [",defensa,",",ataque,"]")

    if c2.estado!="desmayo":
      if self.verbose: print("c",i+1," desea contraatacar...")
      self.counter(i)
  
  def counter(self,i):
    c=0 if i==1 else 1
    c1=self.cs[i]
    c2=self.cs[c]
    lt=range(self.rand)
    counter=c1.fisico['agi']*1-c1.fisico['peso']/10+ sum(random.choices(lt,k=2)) -(c1.fatigan-1)
    +c1.nofisico['ast']+c1.nofisico['int']+c1.nofisico['sab']+c1.nofisico['pac']+c1.nofisico['aut']+ sum(random.choices(lt,k=5)) -(c1.fatigan-3)*5
    +c1.mental['ref']+c1.mental['exp']-c1.mental['est']*2+ sum(random.choices(lt,k=3)) -(c1.fatigan-2)*3
    +c1.psico['conc']+ random.randrange(4) -(c1.fatigan)*1

    cdef=c2.fisico['agi']*1-c2.fisico['peso']/10+ sum(random.choices(lt,k=2)) -(c2.fatigan-1)
    +c2.nofisico['ast']+c2.nofisico['sab']+c2.nofisico['pac']+c2.nofisico['aut']+ sum(random.choices(lt,k=4)) -(c2.fatigan-3)*4
    +c2.mental['exp']-c2.mental['est']*2+c2.mental['vis']+ sum(random.choices(lt,k=3)) -(c2.fatigan-2)*3
    +c2.psico['conc']+c2.psico['ada']*self.asaltos/10+ sum(random.choices(lt,k=2)) -(c2.fatigan)*2

    if counter>cdef:
      self.cs[i].counter+=1
      if self.verbose: print("...contraataque exitoso. [",counter,",",cdef,"]")
      self.daño(i,(counter-cdef))
    else:
      if self.verbose: print("...contraataque fallido.[",counter,",",cdef,"]")


  def daño(self,c,atq):
    c1=self.cs[c]
    lt=range(self.rand)
    i=0 if c==1 else 1
    c2=self.cs[i]
    daño=(c1.fisico['fue']+c1.mental['exp']+ sum(random.choices(lt,k=2)))*35 + atq*5

    if daño > c2.armor:
      fu=daño-c2.armor
      if self.verbose: print("c",c+1," perfora la armadura a c",i+1)
      self.hemorragia(fu,i)
    elif daño <= c2.armor:
      if self.verbose: print("c",c+1," daña la resistente armadura de c",i+1)
      fu=c2.armor-daño
    
    if self.verbose: print("daño: ",daño," armadura:",c2.armor)
    if self.verbose:print("armadura reducida en: ",(daño)*self.darmor/100 )
    self.cs[i].armor= self.cs[i].armor- (daño)*self.darmor/100
    self.cs[i].armorlost.append(daño*self.darmor/100)

  def hemorragia(self,fu,i):
    if 0< fu <500:
      self.cs[i].hemo.append(random.randrange(6))
      if self.verbose: print("Ha hecho un daño superficial")
    elif 500<=fu<1000:
      self.cs[i].hemo.append(random.randrange(6,50))
      if self.verbose: print("Ha hecho un daño leve")
    elif 1000<=fu<2000:
      self.cs[i].hemo.append(random.randrange(51,100))
      if self.verbose: print("Ha hecho un daño moderado")
    elif 2000<=fu<3000:
      self.cs[i].hemo.append(random.randrange(101,200))
      if self.verbose: print("Ha hecho un daño profundo")
    elif 3000<=fu<6000:
      self.cs[i].hemo.append(random.randrange(201,300))
      if self.verbose: print("Ha hecho un daño severo")
    elif fu>=6000:
      self.cs[i].hemo.append(random.randrange(301,500))
      if self.verbose: print("Ha hecho un daño mortal")
  def status(self):
    for c in range(len(self.cs)):
      if self.asaltos%3==0:
        if self.verbose: print("\n")
        self.fatiga(c)
        self.cs[c].sangre= self.cs[c].sangre - sum(self.cs[c].hemo)
        if self.verbose: print("c",c+1," ha perdido ", sum(self.cs[c].hemo), " ml de sangre")
        if self.cs[c].sangre < self.cs[c].sangrePe - self.cs[c].sangrept*self.cs[c].sangrePe/100:
          if self.verbose: print("c",c+1," sufre de hipovolemia...")
          efec=["desmayo","mareos","fatiga"]
          if random.randrange(3,30) >  self.cs[c].psico['cone']+self.cs[c].psico['mor']+self.cs[c].fisico['cons']:
            st=random.choice(efec)
            if st=="desmayo":
              self.cs[c].estado="desmayo"
            elif st=="mareos":
              self.cs[c].estado="mareos"
            else:
              self.cs[c].fatigan=+1
            if self.verbose: print("c",c+1," sufre de ", st,"!")
        if self.cs[c].sangre < self.cs[c].sangrePe - self.dblood*self.cs[c].sangrePe/100:
          if self.verbose: print("c",c+1," ha muerto por hemorragia... en el asalto ",self.asaltos)
          self.cs[c].estado="muerto"
        if self.verbose: 
          print("Volumen sanguinieo: ",self.cs[c].sangre)
          print("fatiga: ",self.cs[c].fatiga)
          print("armor: ",self.cs[c].armor)
          print("\n")
    if self.cs[0].estado=='muerto' and self.cs[1].estado=='muerto':
      self.ganador=0
    elif self.cs[0].estado=='muerto':
      self.ganador=2
    elif self.cs[1].estado=='muerto':
      self.ganador=1

  def fatiga(self,c):
    res=self.cs[c].fisico['res']
    if 0 < self.asaltos < 15+res:
      pass
    elif 15+res < self.asaltos < 25+res:
      self.cs[c].fatiga="Ligeramente Cansado"
      self.cs[c].fatigan=1
    elif 25+res < self.asaltos < 30+res:
      self.cs[c].fatiga="Cansado"
      self.cs[c].fatigan=2  
    elif 30+res < self.asaltos < 33+res:
      self.cs[c].fatiga="Muy Cansado"
      self.cs[c].fatigan=3
    elif 33+res < self.asaltos:
      self.cs[c].fatiga="Agotado"  
      self.cs[c].fatigan=4
      
    
def initOP():
  c3= Combatiente()
  c3.setFisico(10,10,80,10,10,5)
  c3.setNofisico(10,10,10,10,10)
  c3.setMental(10,10,3,10,'espada')
  c3.setPsico(10,10,10,10,10)

  c4= Combatiente()
  c4.setFisico(10,10,80,10,10,5)
  c4.setNofisico(10,10,10,10,10)
  c4.setMental(10,10,3,10,'espada')
  c4.setPsico(10,10,10,10,10)
  return c3,c4

def initUP():
  c3= Combatiente()
  c3.setFisico(5,5,50,5,5,1)
  c3.setNofisico(5,5,5,5,5)
  c3.setMental(5,5,3,5,'espada')
  c3.setPsico(5,5,5,5,5)

  c4= Combatiente()
  c4.setFisico(5,5,50,5,5,1)
  c4.setNofisico(5,5,5,5,5)
  c4.setMental(5,5,3,5,'espada')
  c4.setPsico(5,5,5,5,5)
  return c3,c4

def initWP():
  c3= Combatiente()
  c3.setFisico(1,1,40,1,1,1)
  c3.setNofisico(1,1,1,1,1)
  c3.setMental(1,1,3,1,'espada')
  c3.setPsico(1,1,1,1,1)

  c4= Combatiente()
  c4.setFisico(1,1,40,1,1,1)
  c4.setNofisico(1,1,1,1,1)
  c4.setMental(1,1,3,1,'espada')
  c4.setPsico(1,1,1,1,1)
  return c3,c4
