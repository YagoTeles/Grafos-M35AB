from trabalho01 import trabalho


class adicionar:
    RS = 1; SC = 2; PR = 3;MS = 4; SP = 5; RJ = 6; ES = 7; MG = 8; GO = 9; MT = 10; RO = 11; AC = 12; AM = 13; RR = 14
    PA = 15; AP =16; MA=17; TO=18; DF=19; PI=20; CE=21; RN=22; PB=23; PE=24; AL=25; SE=26; BA=27
    m = trabalho(27)
    m.add_arrest(RS, SC)
    m.add_arrest(SC, RS);m.add_arrest(SC, PR)
    m.add_arrest(PR, MS);m.add_arrest(PR, SP);m.add_arrest(PR, SC)
    m.add_arrest(MS, PR);m.add_arrest(MS, SP);m.add_arrest(MS, MT);m.add_arrest(MS, GO);m.add_arrest(MS, MG)
    m.add_arrest(SP, PR);m.add_arrest(SP, MS);m.add_arrest(SP, RJ);m.add_arrest(SP, MG)
    m.add_arrest(RJ, SP);m.add_arrest(RJ, ES);m.add_arrest(RJ, MG)
    m.add_arrest(ES, RJ);m.add_arrest(ES, MG);m.add_arrest(ES, BA)
    m.add_arrest(MG, ES);m.add_arrest(MG, RJ);m.add_arrest(MG, SP);m.add_arrest(MG, MS);m.add_arrest(MG, GO);m.add_arrest(MG, DF);m.add_arrest(MG, BA)
    m.add_arrest(GO, MG);m.add_arrest(GO, BA);m.add_arrest(GO, DF);m.add_arrest(GO, TO);m.add_arrest(GO, MT);m.add_arrest(GO, MS)
    m.add_arrest(MT, GO);m.add_arrest(MT, MS);m.add_arrest(MT, RO);m.add_arrest(MT, TO);m.add_arrest(MT, PA)
    m.add_arrest(RO, MT);m.add_arrest(RO, AC);m.add_arrest(RO, AM)
    m.add_arrest(AC, RO);m.add_arrest(AC, AM)
    m.add_arrest(AM, RO);m.add_arrest(AM, AC);m.add_arrest(AM, RR);m.add_arrest(AM, PA)
    m.add_arrest(RR, AM);m.add_arrest(RR, PA)
    m.add_arrest(PA, AP);m.add_arrest(PA, RR);m.add_arrest(PA, AM);m.add_arrest(PA, MT);m.add_arrest(PA, TO);m.add_arrest(PA, MA)
    m.add_arrest(AP, PA)
    m.add_arrest(MA, PA);m.add_arrest(MA, TO);m.add_arrest(MA, PI);m.add_arrest(MA, BA)
    m.add_arrest(TO, PA);m.add_arrest(TO, MA);m.add_arrest(TO, PI);m.add_arrest(TO, BA);m.add_arrest(TO, GO);m.add_arrest(TO, MT)
    m.add_arrest(DF, GO);m.add_arrest(DF, MG)
    m.add_arrest(PI, TO);m.add_arrest(PI, MA);m.add_arrest(PI, CE);m.add_arrest(PI, PE);m.add_arrest(PI, BA)
    m.add_arrest(CE, PI);m.add_arrest(CE, RN);m.add_arrest(CE, PB);m.add_arrest(CE, PE) 
    m.add_arrest(RN, CE);m.add_arrest(RN, PB)
    m.add_arrest(PB, RN);m.add_arrest(PB, CE);m.add_arrest(PB, PE)
    m.add_arrest(PE, PB);m.add_arrest(PE, CE);m.add_arrest(PE, PI);m.add_arrest(PE, BA);m.add_arrest(PE, AL)
    m.add_arrest(AL, PE);m.add_arrest(AL, BA);m.add_arrest(AL, SE)
    m.add_arrest(SE, AL);m.add_arrest(SE, BA)
    m.add_arrest(BA, SE);m.add_arrest(BA, ES);m.add_arrest(BA, MG);m.add_arrest(BA, GO);m.add_arrest(BA, TO);m.add_arrest(BA, PI);m.add_arrest(BA, PE);m.add_arrest(BA, AL)
    m.show_matrix()

    print()
