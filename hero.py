class Hero:
    
    # konstruktor
    def __init__(self,user,atk,dfe,hp,mn):
        self.user = user
        self.atk = atk
        self.dfe = dfe
        self.hp = hp
        self.mn = mn
    
    # method
    def get_info(self):
        return "Nama {}, HP: {}, Mana: {}, attack: {}, defence: {}".format(self.user,str(self.hp),str(self.mn),str(self.atk),str(self.dfe))
    
    def greeting(self):
        return "Selamat datang {}".format(self.user)
        
    def get_attack(self):
        return "Nama {}, Attack {}".format(self.user,self.atk)