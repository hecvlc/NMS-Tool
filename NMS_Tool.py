#No Man's Sky database and helper
#Created by: Hec

#Item and Blueprint database dictionary
database = {
    
    #Elements base value in U
    'elements': {
            'Th': 20.6, 'Pu': 41.3, 'C': 6.9,
            'Em': 275, 'Au': 220, 'Al': 165, 'Ni': 137.5, 'Cu': 110, 'Ir': 96.3,
            'Ca': 288.8, 'Ra': 302.5, 'Mu': 305, 'Om': 309.4,
            'Hr': 27.5, 'Pt': 55, 'Ch': 82.5,
            'Fe': 13.8, 'Zn': 41.3, 'Ti': 61.9
        },
    
    #Products base value in U
    'products': {
            #Technology Components
            'carite sheet': 825,
            'suspension fluid': 1100,
            'microdensity fabric': 1650,
            'electron vapour': 4950,
            'antimatter': 5232, 
            'dynamic resonator': 27500,
            
            #Alloys
            'aronium': 1546.9, 
            'herox': 2877.5, 
            'magmox': 30030, 
            'lemmium': 30937,
            'crollium': 35378.8, 
            'grantine': 35646.9, 
            'terumin': 39105,
            
            #Energy Resources
            'power gel': 171.9,
            'shielding shard': 343.8,
            'power canister': 343.8,
            'power reservoir': 515.6,
            'shielding plate': 687.5,
            'shielding sheet': 1031.1,
            'unstable plasma': 27500,
            'warp cell': 46750
        },
    
    #Crafting blueprints
    'blueprints': {
        #Technology Components
        'carite sheet':{
            'Fe': 50
            },
        'suspension fluid': {
            'C': 50
            },
        'microdensity fabric':{
            'Fe': 50,
            'Pt': 10
            },
        'electron vapour':{
            'suspension fluid': 1,
            'Pu': 100
            },
        'antimatter': {
            'electron vapour': 1,
            'Zn': 20,
            'Hr': 50
            },      
        'dynamic resonator':{
            'antimatter': 2,
            'microdensity fabric': 4,
            'Ch': 100
            },
                   
        #Alloys
        'aronium': {
            'Fe': 50,
            'C': 50
            },
        'herox': {
            'Zn': 20,
            'Pu': 20
            },
        'magmox': {
            'C': 30,
            'Th': 300,
            'Pu': 300
            }, 
        'lemmium': {
            'Pu': 200,
            'Ti': 100
            },
        'crollium': {
            'Ch': 80,
            'Ir': 100
            },
        'grantine': {
            'Ir': 150,
            'Cu': 50,
            'aronium': 1
            },
        'terumin': {
            'Em': 40,
            'Al': 40,
            'herox':1
            },
                   
        #Energy Resources
        'shielding shard': {
            'Fe': 25
            },
        'power canister': {
            'C': 50
            },
        'power reservoir': {
            'C': 75
            },
        'shielding plate':{
            'Fe': 50
            },
        'shielding sheet': {
            'Fe': 75
            },
        'unstable plasma': {
            'Th': 400,
            'Pu': 200
            },
        'warp cell': {
            'antimatter': 1,
            'Th': 100
            },
        
        #Tools
        'bypass chip': {
            'Pu': 10,
            'Fe': 10
            },
        'atlaspass v1': {
            'Fe': 25,
            'He': 10
            },
        'atlaspass v2': {
            'Ti': 25,
            'Ch': 10
            },
        
        #Exosuit Blueprints
        'stamina enhancement sigma': {
            'Fe': 20,
            'C': 20
            },
        'stamina enhancement tau': {
            'Fe': 100,
            'He': 150,
            'Pu': 50
            },
        'stamina enhancement theta': {
            'Zn': 150,
            'He': 150,
            'Pu': 50
            },
        'life support module sigma': {
            'Pu': 50,
            'Pt': 20
            },
        'life support module tau': {
            'Al': 150,
            'C': 250,
            'Th': 50
            }                
        }
    }

#Function to calculate and return profit of product entered by user
def calculateProfit(product):
    cost = calculateCraftingCost(product)
    profit = database['products'][product] - cost
    return profit

#Function to calculate and return cost to craft product entered by user
def calculateCraftingCost(product):
    cost = 0
    for item in database['blueprints'][product]:
        if item in database['blueprints']:
            cost += calculateCraftingCost(item)
        else:
            cost += database['elements'][item] * database['blueprints'][product][item]
    return cost

#Function to print profit by crafting product and then selling instead of selling raw materials
def printProfit(profit, item):
    if profit > 0:
        print 'You will net a', str(profit) + 'U profit by crafting', item, 'instead of selling the raw materials.\n'
    else:
        profit = 0 - profit
        print 'You will lose', str(profit) + 'U by crafting', item + '. Better invest in another recipe or sell the raw materials.\n' 

#Function to show the components of a blueprint
def showComponents(item):
    print 'You will need',
    i = 1
    for key in database['blueprints'][item]:
        if i < len(database['blueprints'][item]) - 1:
            print database['blueprints'][item][key], key.title() + ',',
        elif i < len(database['blueprints'][item]):
            print database['blueprints'][item][key], key.title(),
        else:
            print 'and', database['blueprints'][item][key], key.title(),
        i += 1
    print 'to craft your 1', item +'.\n'
  
#Title
print 'This is a No Man\'s Sky Tool.\n'

#Interactive Menu

#Infinite Loop
while True:
    
    #User options
    print 'Choose your option:\n1) Show blueprint components.\n2) Calculate profit.\n'
    
    #user picks 1) show recipe 2) profit 3) exit
    userInput = raw_input()
     
    #1) show recipe materials
    if userInput == '1':
        itemUser = raw_input('Blueprint to know: ')
        itemUser = itemUser.lower()
        
        #Check if input exists
        while itemUser not in database['blueprints']:
            itemUser = raw_input('The item or blueprint you are looking for doesn\'t exist. Please try again: ')
            itemUser = itemUser.lower()

        showComponents(itemUser)
        userBreak = raw_input('Do you want to exit the program? (y/n): ')
        if userBreak == 'y':
            break;
        else:
            print '\n'
            
    #2) show profit
    elif userInput == '2':
        itemUser = raw_input('Profit selling: ')
        itemUser = itemUser.lower()
        profit = calculateProfit(itemUser)
        itemUser = itemUser.title()
        printProfit(profit, itemUser)
        userBreak = raw_input('Do you want to exit the program? (y/n): ')
        if userBreak == 'y':
            break;
        else:
            print '\n'