# [2007/2008](https://www.oktatas.hu/pub_bin/dload/kozoktatas/tanulmanyi_versenyek/oktv/oktv_2007_2008/oktv0708_info2_d_flut.pdf) 1. feladat: Robot  

Egy gyárban a munkagépek négyzetrácsos elrendezésben vannak. A futószalagon érkező tárgyakat egy robotnak kell elszállítania a rendeltetési helyére.  
A robot a **(0,0)** mezőről indul, a tárgyakat érkezési sorrendjükben veheti le a futószalagról és egyszerre legfeljebb **3** tárgyat szállíthat.  
Ha több tárgyat szállít, akkor azokat tetszőleges sorrendben adhatja le a rendeltetési helyre. A robot a munkagépek felett mozoghat, egy lépésben szomszédos mezőre léphet egyet:  
- balra  
- jobbra  
- felfelé  
- lefelé  

Egy lépése *egy időegységet* igényel. Miután leadta az egy menetben szállított tárgyakat, vissza kell térnie a kiindulási helyére, a **(0,0)** mezőre.  

Készíts programot ([robot.py](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Robot/robot.py)), amely kiszámítja, hogy legkevesebb mennyi idő alatt tudja a robot elszállítani az összes tárgyat, és meg is ad egy szállítási ütemezést!  
A [robot.be](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Robot/robot.be) szöveges állomány első sorában a tárgyak **N** *(1≤N≤10000)* száma van.  
A következő **N** sor mindegyikében két pozitív egész szám van; **X és Y** *(1≤X,Y≤1000)* egy szóközzel elválasztva, egy tárgy rendeltetési helyének koordinátái. Ugyanarra a helyre több tárgy is érkezhet.  
A [robot.ki](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Robot/robot.ki) szöveges állomány első sorába azt a legkisebb **M** számot kell írni, amely alatt a robot az összes tárgyat el tudja szállítani a rendeltetési helyére.  
A második sorba egy számsorozatot kell írni *(egy-egy szóközzel elválasztva)*, amely megadja, hogy a robot egy-egy menetben hány tárgyat szállít. Tehát a számsorozat minden eleme **1**,**2**, vagy **3** lehet.

### Példa:  
[robot.be](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Robot/robot.be)
>6  
>1 2  
>3 2  
>4 7  
>8 3  
>5 7  
>9 2  

[robot.ki](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Robot/robot.ki)  
>54  
>3 3
