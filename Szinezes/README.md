# 2005/2006 4. feladat: Színezés

Egy **N** emeletes fehér épület bizonyos emeleteit a szépség kedvéért pirosra szeretnénk festeni.  
Csak olyan festést tartunk elfogadhatónak, amelynél szomszédos szinteket nem festünk
pirosra.  

A színezéseket **N+1** elemű *0-1* számsorozattal kódoljuk:  
- 1-es jelöli a piros
- 0-s pedig a fehér színű emeletet  

Az első szám jelenti a földszint, az utolsó pedig az **N.** emelet színét. 
Készíts programot, amely megadja, hogy az épület hányféleképpen színezhető ki,  valamint a lexikografikus *(ábécé szerinti)* **K**-adik színezést!  

A SZIN.BE szöveges állomány egyetlen sorában az emeletek **N** száma *(0≤N≤40)* és **K** szám *(1≤K≤100000000)* van.  
A SZIN.KI szöveges állomány első sorába a színezések lehetséges számát kell írni!  
A második sorba a **K.** színezést kell kiírni: az emeletek növekvő sorrendjében **N+1** darab egész számot egy-egy szóközzel elválasztva, ahol *0* jelöli a fehér, *1* pedig a pirosra festett szintet!  

### Példa:  
SZIN.BE  
>3 4

SZIN.KI
>8
>0 1 0 0  

Sorrendben a jó festések:  
```
1.  0 0 0 0
2.  0 0 0 1
3. 0 0 1 0
4.  0 1 0 0
5.  0 1 0 1
6.  1 0 0 0
7.  1 0 0 1
8.  1 0 1 0
```