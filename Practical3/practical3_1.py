Temp_rule = {
  "lc": 10,
  "lr": 25,
  "bal": 15,
  "bar": 45,
  "al": 40,
  "ar":60,
  "aal":55,
  "aar":85,
  "hl":75,
  "hc":90
}
Press_rule = {
  "lc": 1,
  "lr": 1.75,
  "bal": 1.25,
  "bar": 2.75,
  "al": 2,
  "ar":4,
  "aal":3.25,
  "aar":4.75,
  "hl":4.25,
  "hc":5
}
Heating_power_rule = {
  "lc": 1,
  "lr": 1.75,
  "bal": 1.25,
  "bar": 2.75,
  "al": 2,
  "ar":4,
  "aal":3.25,
  "aar":4.75,
  "hl":4.25,
  "hc":5
}
Valve_opening_rule = {
  "lc": 1,
  "lr": 1.75,
  "bal": 1.25,
  "bar": 2.75,
  "al": 2,
  "ar":4,
  "aal":3.25,
  "aar":4.75,
  "hl":4.25,
  "hc":5
}

temp=16.5
press=1.3


def rule_1temptri(temp):
    if temp >= Temp_rule["bal"] or temp <= Temp_rule["bar"]:
        center=Temp_rule["bar"] - Temp_rule["bal"] 
        if temp <= center:
            tempr1=(temp-Temp_rule["bal"])/(Temp_rule["bar"]-Temp_rule["bal"])
        if temp > center:
            tempr1=(center-temp)/(center-Temp_rule["bar"])
    else:
        tempr1=0
    print("tempr1:", tempr1)
    return(tempr1)     
def rule_1presstri(press):
    if press >= Press_rule["bal"] or temp <= Press_rule["bar"]:
        center=Press_rule["bar"] - Press_rule["bal"] 
        if press <= center:
            #print((press-Press_rule["bal"]))
            press1=(press-Press_rule["bal"])/(Press_rule["bar"]-Press_rule["bal"])
        if press > center:
            press1=(center-press)/(center-Press_rule["bar"])
    else:
        press1=0
    print("Press1:",press1)
    return(press1)   

def rule_2temptri(temp):
    if temp >= Temp_rule["lc"] or temp <= Temp_rule["lr"]:
        if temp >= Temp_rule["lc"]:
            tempr2=(Temp_rule["lc"]-temp)/(Temp_rule["lc"]-Temp_rule["lr"])
    else:
        tempr2=0
    print("tempr2:", tempr2)
    return(tempr2)
def rule_2presstri(press):
    if press >= Press_rule["lc"] or press <= Press_rule["lr"]:
        if press >= Press_rule["lc"]:
            press2=(Press_rule["lc"]-press)/(Press_rule["lc"]-Press_rule["lr"])
    else:
        press2=0
    print("Press2:",press2)
    return(press2)

def triarea(a,b):
    area=(a-tricenter(a,b))
    return(area)

def tricenter(a,b):
    center=b-a
    return(center)

def triz(a,b):
    c=(min(a,b))
    return c

def tridefuzz(z1,z2,a1,a2,a3,a4):
    c = (z1*(triarea(a1,a2)*tricenter(a1,a2))+z2*(triarea(a3,a4)*tricenter(a3,a4)))
    return c

def trifunction():
    Z1=triz(rule_1temptri(temp),rule_1presstri(press))
    Z2=triz(rule_2temptri(temp),rule_2presstri(press))
    print("Z1:", Z1)
    print("Z2:", Z2)
    c1=tridefuzz(Z1,Z2,Heating_power_rule["aal"],Heating_power_rule["aar"],Heating_power_rule["hl"],Heating_power_rule["hc"])
    c2=tridefuzz(Z1,Z2,Valve_opening_rule["bal"],Valve_opening_rule["bar"],Valve_opening_rule["lc"],Valve_opening_rule["lr"])
    print("center1 is: "+c1)
    print("center2 is: "+c2)

trifunction()