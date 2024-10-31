// Temperatuur
// Kirjutage programm, mis kontrollib saadud temperatuuri põhjal olukorda. Kui temperatuur on suurem kui 25 kraadi, väljastage "Väga kuum ilm!". Kui temperatuur on vahemikus 15 kuni 25 kraadi, väljastage "Mõnus temperatuur". Kui temperatuur on väiksem kui 15 kraadi, väljastage "Jahe ilm".

let temp  = 30

if(temp>25){
    console.log("kuum");
} else if (temp>=15 && temp<=25) {
    console.log("mõnus");
} else {
    console.log("jahe");
}


// Kasutajanime kontroll
// Kirjutage programm, mis küsib kasutajalt nime ja kontrollib lühendatud IF-lause abil, kas kasutajanimi on administraatori nimi. Kui kasutajanimi on "admin", väljastage konsooli "Tere, administraator!". Kui kasutajanimi ei ole "admin", väljastage konsooli "Tere, külaline!".



// Ürituse piletite hind
// Kirjutage programm, mis "küsib" (lisa ise muutujasse) kasutajalt üritusele soovitud piletitüübi (taispilet või sooduspilet) ja vanuse ning kasutab pesastatud IF-lauset, et arvutada välja pileti hind vastavalt piletitüübile ja vanusele. Programm võtab arvesse järgmised tingimused:
//     Täispilet: Alla 18-aastastele on hind 10 eurot, 18-64-aastastele 20 eurot ja 65-aastastele ja vanematele 15 eurot.
//     Sooduspilet: Alla 18-aastastele ja 65-aastastele ja vanematele on hind 8 eurot, 18-64-aastastele 15 eurot

let tyyp = "tais"
let vanus = 70
let hind =  0

if(tyyp=="tais" && (vanus<18)){
    hind = 10
} else if (tyyp="tais" && (vanus>18 && vanus<64)) {
    hind = 20
} else if (tyyp=="soodus" && (vanus<18 || vanus>64)) {
    hind = 8
} else {
    hind = 15
} 




console.log(hind)