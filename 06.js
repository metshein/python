//tooted
const products = ["Õunad", "Piim", "Leib", "Juust", "Tomatid", "Kanafilee", "Muna", "Sibul", "Apelsinid", "Riis", "Jogurt", "Kartul", "Kalafilee", "Pasta", "Jogurtijook", "Porgandid", "Virsikud", "Pähklid", "Rosinad", "Kapsas", "Kreeka jogurt", "Veiseliha", "Banaanid", "Oliivid", "Mandlid", "Magus kartul", "Greibid"];


for (let i=0; i<10; i++) {
    const element = products[i];
    if(element=="Muna" || element=="Sibul" || element=="Riis"){
        continue;
    } else {
       console.log(`${i+1}. ${element}`); 
    }
    
}

//tempid
const temperatures = [
    [5, 8, 12, 10, 7, 9, 11, 14, 16, 13, 10, 6, 4, 3, 2, 4, 6, 8, 10, 12, 15, 17, 18, 16, 13, 10],
    [1, 4, 6, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19, 18, 16, 13, 11],
    [8, 10, 13, 15, 16, 18, 19, 20, 17, 15, 13, 11, 10, 9, 8, 10, 12, 14, 16, 18, 20, 22, 21, 18, 16, 14],
    [2, 5, 7, 9, 12, 15, 17, 18, 15, 13, 11, 8, 6, 5, 4, 7, 9, 12, 14, 16, 19, 21, 20, 18, 16, 13],
    [6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18, 20, 22, 21, 19, 16, 13],
    [11, 14, 17, 19, 21, 23, 24, 22, 19, 16, 13, 11, 10, 9, 9, 12, 15, 18, 20, 23, 25, 27, 26, 24, 21, 18],
    [9, 11, 14, 16, 18, 20, 22, 21, 18, 16, 13, 11, 9, 8, 7, 10, 13, 16, 18, 21, 23, 24, 23, 21, 18, 15],
    [7, 10, 13, 15, 17, 20, 22, 23, 20, 17, 14, 12, 10, 9, 8, 11, 14, 17, 19, 22, 24, 26, 25, 23, 20, 17],
    [3, 6, 9, 11, 13, 15, 17, 18, 16, 14, 11, 9, 7, 6, 5, 8, 10, 13, 15, 17, 19, 21, 20, 18, 15, 12],
    [1, 3, 5, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19, 18, 16, 13, 11],
    [6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18, 20, 22, 21, 19, 16, 13],
    [10, 13, 16, 18, 20, 22, 23, 24, 21, 18, 15, 13, 11, 10, 9, 12, 15, 18, 20, 23, 25, 27, 26, 24, 21, 18]
    ];

const months = "Jaanuar, Veebruar, Märts, Aprill, Mai, Juuni, Juuli, August, September, Oktoober, November, Detsember";
    
let kuude_keskmised = [];

for (let j = 0; j < temperatures.length; j++) {
    const e = temperatures[j];
    const sum = e.reduce((b, a) => b + a, 0);
    let keskmine = sum/e.length;
    kuude_keskmised.push(keskmine);
    //console.log(keskmine);
}

const max = kuude_keskmised.reduce((a, b) => Math.max(a, b), -Infinity);
const min = kuude_keskmised.reduce((a, b) => Math.min(a, b), Infinity);

console.log(months.split(",")[kuude_keskmised.indexOf(max)]+" "+kuude_keskmised.indexOf(max));
console.log(months.split(",")[kuude_keskmised.indexOf(min)]+" "+kuude_keskmised.indexOf(min));













//pos neg
let nr = 5555555;
let vastus = "";
 
switch (true) {
    case nr>0:
        vastus = "pos";
        break;
    case nr==0:
        vastus = "0";
        break;
    default:
        vastus = "neg";
}
 
console.log(vastus);


//resto
let bron = 10;
let valik = "";

switch(true){
    case bron<3:
        valik = "Valige laud kahele inimesele.";
        break;
    case bron>2 && bron<5:
        valik = "Valige laud neljale inimesele.";
        break;
    case bron>4 && bron<7:
        valik = "Valige laud kuuele inimesele.";
        break;
    default:
        valik = "Valige suur laud";
}

console.log(valik);