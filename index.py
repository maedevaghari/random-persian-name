print("\n        < Family Chance >")
print('________________________________\n')
girl = [
'atena','tina','dina','armita','narges','aylin','tara','paniz',
'mahsa','anita','nadia','sakine','mona','sara','nika','samin',
'helina','kiana','nila','mina','barana','hila','tanya','kimia',
'rozhin','elnaz','atoosa','hanye','yasnaw','manya','aysan','leyla',
'elham','nayereh','ayda','hana','sarina','parya','maryam','fatemeh',
'reyhane','shima','dorsa','sofia','roxana','noor tala','mahdie','mobina'
]
old_w = [
'goli khanoom','naz khatoon','noghre','azam','zari joon','eshrat','chini',
'gol gis','taj soltan','shamsi','nane ghamar','bibi','farideh','gohar',
'bibi khatoon','khavar soltan','kobra','ameneh','kokab','sepid banoo',
'farah','farangis','nezakat','yatim'
]
old_m = [
'nosrat','shir ali','asad ali','jorti bag','beig morad','shah hossein',
'geda ali','kalim','noor ali','gorg ali','panj ali','yarvali','ghooch ali',
'ojagh ali','khoda rahm','rajab ali','safr ali','sefr ali','barat ali',
'kalim beig','sabz ali','ghazanfar','gholam ali','yatim'
]
import random
r1 = random.randint(0,47)
r2 = random.randint(0,23)
r3 = random.randint(0,23)
print('aji (khahar) : '+girl[r1])
print("-----------------------------")
print('nanat : '+old_w[r2])
print('-----------------------------')
print('dady : '+old_m[r3])
