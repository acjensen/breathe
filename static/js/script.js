var peopleText = " ";

// Get number of active users.
async function getNumActiveUsers() {
    const response = await fetch("/num-active-users", {
        method: 'GET',
    }).then(function (response) {
        return response.json()
    }).then(function (json) {
        console.log(json)
        if (json.num_active_users <= 1) {
            peopleText = "1 person is";
        } else {
            peopleText = json.num_active_users + " people are";
        }
        document.getElementById("num-active-users").innerHTML = peopleText + " breathing with you.";
    })
}

// Get number of active users from the server.
async function pingHome() {
    const response = await fetch("/ping-home", {
        method: 'GET',
    }).then(function (response) {
        return response.json()
    }).then(function (json) {
        console.log(json)
    })
}

// Ping home every every x milliseconds so the server knows we're still here.
window.setInterval(pingHome, 300000)

// Refreshing the page gets the number of active users.
window.onload = getNumActiveUsers
