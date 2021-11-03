# Metró
Egy metróállomásra N időegységben érkeznek utasok, a K hosszú mozgólépcsőre legfeljebb ketten léphetnek egyszerre (azaz az érkezők közül ketten azonnal a mozgólépcső legfelső
fokára kerülnek), a lépcsőn nincs mozgás – időegységenként mindenki egyet halad lefelé. A
lépcső egy L utast befogadni képes váróterembe érkezik, az i-edik időegységben váróterembe
lépőt ugyanabban az időegységben nem viheti el a metró. A metró M időegységenként jön,
kiszáll belőle adott számú utas, és elviszi az összes metróra várakozó utast. A ki- és beszállás
1 időegység alatt megtörténik. A felfelé menő mozgólépcsőre várakozó utasok közül egy időegységben legfeljebb 2 léphet a lépcsőre. Aki most szállt le a metróról, az leghamarabb a következő időegységben léphet a mozgólépcsőre. Kezdetben (a 0. időegységben) a lépcső és a
váróterem is üres, az első metró az M. időegységben érkezik. Ha a váróterembe nem férnek be
az utasok, akkor a metróállomás működését leállítják.

Készíts programot (allomas.pas,…), amely megadja, hogy az egyes metrószerelvények hány utast visznek el! A végrehajtás vagy N+K+M időegység után fejeződjön be, vagy
amikor a metróállomás működését leállítják!

A allomas.be állomány első sorában az időegységek száma (1≤N≤1 000 000), a mozgólépcső hossza (1≤K≤100), a váróterem kapacitása (1≤L≤1000), a metrók követési távolsága
(1≤M≤1000) és az érkező utasok száma (1≤U≤1 000 000) van egy-egy szóközzel elválasztva.
A következő U sor mindegyikében egy-egy utas érkezési ideje van (0≤Idői≤N), nemcsökkenő
sorrendben. A következő sorban az egyes metrószerelvényekről leszállók száma van, a szerelvények érkezési sorrendjében.

A allomas.ki szöveges állományba két sort kell írni! Az első sorba az állomásról utasokat elvivő metrószerelvények S számát kell írni! A másodikba S szám kerüljön egy-egy
szóközzel elválasztva: az egyes metrószerelvények által elvitt utasok száma!