# 2006/2007 1. feladat: Madár

Egyes madarak a fészkelő helyüktől adott távolságra saját területet, ún. territóriumot tartanak. Ha két madár territóriuma átfedő, akkor ott összeverekedhetnek egymással.  

Készíts programot ([madar.py](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Madar/madar.py)), amely megadja  
1. A senki mással nem verekedő madarakat
2. A legtöbb másik madárral verekedő madarat
3. Azon madarak számát, amelyek territóriuma része valamely más madár territóriumának

A [madar.be](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Madar/madar.be) szöveges állomány első sorában a madarak száma *(1≤M≤1000)* és egy, a fészkeket tartalmazó négyzet alakú terület mérete *(1≤N≤10000)* van.  
A következő M sorban egy-egy madarat leíró **3** szám szerepel egy-egy szóközzel elválasztva. Az első két szám a madár fészkének helye *(1≤X,Y≤N)*,  
a harmadik pedig a territórium mérete *(1≤R≤100)*, ami azt jelenti, 
hogy a territórium az **(X-R,Y-R)** ponttól az **(X+R,Y+R)** pontig tart.  

A [madar.ki](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Madar/madar.ki) szöveges állomány három sorába a három részfeladat megoldását kell írni.  
Ha valamelyik részfeladatra nincs megoldás, egy üres sort akkor is ki kell írni!  
- Az első a senki mással nem verekedő madara sorszáma kerüljön, egy-egy szóközzel elválasztva!
- A második sorba a legtöbb másik madárral verekedő madár sorszámát kell írni (ha több megoldás van, akkor bármelyik kiírható)!
- A harmadik sorba azon madarak száma kerüljön, amelyek territóriuma teljes egészében része valamely más madár territóriumának!  

### Példa:
[madar.be](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Madar/madar.be)
>7 100  
>7 7 4  
>7 7 2  
>20 15 5  
>14 21 4  
>19 22 2  
>20 5 2  
>23 23 1

[madar.ki](https://github.com/sens1tiv/Nemes-Tihamer-Feladatok/blob/master/Madar/madar.ki)  
>6 7  
>3  
>1