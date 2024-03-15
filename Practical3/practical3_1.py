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

def area(a,b):
    area=1/2*(b-a)
    return(area)

def center(a,b):
    center=b-a
    return(center)


def trifunction():
    Z1=(min(rule_1temptri(temp),rule_1presstri(press)))
    Z2=(min(rule_2temptri(temp),rule_2presstri(press)))
    print("Z1:", Z1)
    print("Z2:", Z2)
    #C1 = (Z1*area(Heating_power_rule["aal"],Heating_power_rule["aar"])*center(Heating_power_rule["aal"],Heating_power_rule["aar"]))+(Z2*area(Heating_power_rule["hl"],Heating_power_rule["hc"])*center(Heating_power_rule["hl"],Heating_power_rule["hc"]))/(Z1*area(Heating_power_rule["aal"],Heating_power_rule["aar"]))+(Z2*area(Heating_power_rule["hl"],Heating_power_rule["hc"]))
    C2 = (Z1*area(Valve_opening_rule["bal"],Valve_opening_rule["bar"])*center(Valve_opening_rule["bal"],Valve_opening_rule["bar"]))+(Z2*area(Valve_opening_rule["lc"],Valve_opening_rule["lr"])*center(Valve_opening_rule["lc"],Valve_opening_rule["lr"]))/(Z1*area(Valve_opening_rule["bal"],Valve_opening_rule["bar"]))+(Z2*area(Valve_opening_rule["lc"],Valve_opening_rule["lr"]))
    #print(C1)
    print("this is c2:",C2)
    print(Valve_opening_rule["bal"])
    print(Z1)
    print(area(Valve_opening_rule["bal"],Valve_opening_rule["bar"]))
    print(center(Valve_opening_rule["bal"],Valve_opening_rule["bar"]))
    print(Z2)
    print(area(Valve_opening_rule["lc"],Valve_opening_rule["lr"]))
    print(center(Valve_opening_rule["lc"],Valve_opening_rule["lr"]))

trifunction()