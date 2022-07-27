import fetch from "node-fetch";
const username = process.argv[2];


(async () => {
    const res2 = await fetch(`https://overseer.1337.ma/api/users?page=1&username=${username}`, { headers: { "Cookie": "PHPSESSID=e1i5utuv7n3otan2llerlutgkn"}})
    const body2 = await res2.json();
	console.log(body2)
    const userId = body2['hydra:member'][0].student.id;
    

    const res = await fetch(`https://overseer.1337.ma/_next/data/QLfn6qnLowKAK_ZiVhg8E/user/${userId}.json?id=0`, { headers: { "Cookie": "PHPSESSID=e1i5utuv7n3otan2llerlutgkn"}})
    const body = await res.json();
	// console.log(body)
    const overseerData = body.pageProps.data
    
    const userY = overseerData.student[0].y
    const userX = overseerData.student[0].x
    const userStats = overseerData.plotData.plots[userX] ?? {}
    const bigWire = userStats['`Avg`. teams']
    const smallWire = userStats['Min. of double ETA'] ?? userStats['Max blackhole']
    
    console.log(userX);
    console.log(overseerData.student[0].login);
    if (userX > 614) {
        console.log("saliti");
    }
    else if (userY >= bigWire) {
        console.log("nadi");
    }
    else if (userY < bigWire && userY >= smallWire) {
        console.log('chwia')
    }
    else {
        console.log('d3if')
    }
})();