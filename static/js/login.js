function login(){
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    const mydata={
        username:username,password:password
    }
    console.log(window.location.origin+"/api/v1/auth/")
    fetch(window.location.origin+"/api/v1/auth/", {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    // mode: 'cors', // no-cors, cors, *same-origin
    // cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    // credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json',
        // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    // redirect: 'follow', // manual, *follow, error
    // referrer: 'no-referrer', // no-referrer, *client
    body: JSON.stringify(mydata) // body data type must match "Content-Type" header
})
.then(response => response.json()) // parses JSON response into native JavaScript objects
.then(data => {
    if (data.success){
        console.log(data.message); 
        localStorage.setItem('loggedIn',true) 
        localStorage.setItem('user',JSON.stringify(data.user))
        window.location.href = "/"
    }else{
        console.log(data.message); 
    }
      
})
.catch(err =>{
    console.log(err);
})

}

function isLoggedIn(){
    if(localStorage.getItem('loggedIn')){
        // does user exist
        if (localStorage.getItem('user')){
            // if the user exists, let's get them
            var user = JSON.parse(localStorage.getItem('user'))
            // is the user is active
            if (user['active']){
                // setting username if the user is active
                document.getElementById('username').innerHTML = user['username']
            return true
            }else{
                return false 
            }      
        }else{
            return false
        }         
    }else{
        return false
        }
    }
