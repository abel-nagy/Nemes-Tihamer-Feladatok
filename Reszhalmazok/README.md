# 2005/2006 2. feladat: Részhalmazok
Egy iskola diákjai választhattak, hogy milyen nyelvet szeretnének tanulni, 
illetve hogy testnevelés órán milyen sportággal szeretnének foglalkozni.  
Minden diák egyetlen nyelvet és egyetlen sportágat választhatott.  
Készíts programot (RESZH.PAS, RESZH.C, …), amely megadja, hogy hány olyan nyelv van, 
amelyre igaz, hogy ha egy valamilyen sportággal foglalkozó tanuló ezt a nyelvet választotta, 
akkor mindenki, aki ezzel a sportággal foglalkozik, is ezt a nyelvet választotta!  
A RESZH.BE szöveges állomány első sorában a diákok M (1≤M≤1000), a nyelvek N (1≤N≤100) 
és a sportágak S (1≤S≤100) száma van, egy-egy szóközzel elválasztva.  
A következő N sorban az egyes nyelveket, az azt követő S sorban pedig az egyes sportágakat választó
tanulók sorszáma van, egy-egy szóközzel elválasztva.  
Minden egyes ilyen sor egy darabszámmal (DB) kezdődik, amelyet DB darab tanuló sorszáma követ, 
egy-egy szóközzel elválasztva.  

Az RESZH.KI szöveges állomány egyetlen sorába az adott tulajdonságú nyelv szerinti
csoportok számát kell írni!  
Példa:  

RESZH.BE  
8 4 4 2  
3 1 3 5  
1 2  
2 4 8  
2 7 6  
3 4 8 2  
3 5 1 3  
1 6  
1 7  

RESZH.KI  
2

(Az 1,3,5 sorszámú tanuló a nyelv szerint is és a sportág szerint is ugyanabban a csoportban van. 
A harmadik és negyedik sportágat választók részhalmazának uniója éppen a negyedik nyelvet tanuló részhalmaz: {7,6}={6}∪{7}.) 