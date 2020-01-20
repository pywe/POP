function fetchCampaigns(){
    // get country
    var country = "Ghana"
    const mydata = {country:country}
    fetch(window.location.origin+"/api/v1/campaigns/fetch/", {
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
    // console.log(data);
    // save the objects gotten at this point to local database
    var tbody = document.getElementById("campaignList");
    tbody.innerHTML = ""
    // constructing table data from objects retrieved 
    var d = new Date()
    var year = d.getFullYear()
    var month = parseInt(d.getMonth())+1
    var day = d.getDate()
    var hour = d.getHours()
    var mins = d.getMinutes()
    var seconds = d.getSeconds()
    var time = d.getTime()
    for(var i=0;i < data.objects.length;i++){
        var tr = `<tr>`
        tr += `<td>`+data.objects[i]['country']+`</td>`
        tr += `<td>`+data.objects[i]['name']+`</td>`
        tr += `<td>`+data.objects[i]['status']+`</td>`
        tr += `<td>`+year+"/"+month+"/"+day+"|"+hour+":"+mins+":"+seconds+`</td>`
        if(data.objects[i]['status'] === 'active'){
        tr += `<td><a href="/campaign_list/new_session/" onclick="saveCampaign('`+data.objects[i]['name']+`')" class="btn btn-light"><img src="/static/images/icon-viewlink.svg" /> Open</a> <a onclick="fetchCampaigns()" class="btn btn-primary">Update this campaign</a></td>`
        }else{
         tr += `<td>No action available</td>`   
        }
        tr += `</tr>`
        tbody.innerHTML += tr
    }
    

    }
else{
    console.log(data); 
}
  
})
.catch(err =>{
console.log(err);
})
}

function saveCampaign(name){
    localStorage.setItem('campaign',name)
}