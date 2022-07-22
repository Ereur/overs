import fetch from 'node-fetch';
import fs from 'fs';

// fetch("https://overseer.1337.ma/user/230", { headers: { "Cookie": "PHPSESSID=e1i5utuv7n3otan2llerlutgkn"}}).then(res => { return res.text() }).then(txt => {
//     return (txt.match(/>([0-9]*)<\/span>/)[1])
// }).then(txt => {
//     console.log(txt);
//     // var data = {"time_spent" : txt}
//     // // document.getElementById("my_div").innerHTML = txt;
//     // fs.writeFile ("data.json", JSON.stringify(data), function(err) {
//     //     if (err) throw err;
//     //     console.log(da);
//     //     }
//     // );
// })

fetch("https://overseer.1337.ma/user/search?login=zoukaddo", { headers: { "Cookie": "PHPSESSID=e1i5utuv7n3otan2llerlutgkn"}}).then(res => { return res.text() }).then(txt => {
    console.log(txt);
    // var data = {"time_spent" : txt}
    // // document.getElementById("my_div").innerHTML = txt;
    // fs.writeFile ("data.json", JSON.stringify(data), function(err) {
    //     if (err) throw err;
    //     console.log(da);
    //     }
    // );
})

