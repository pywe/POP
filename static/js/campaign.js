//
    // Define your database
    //
    var db = new Dexie("observedb");
    db.version(1).stores({
        pharmacies: 'name,pharmacy_info',
        baskets: '++id,basket',
        sessions: 'session_name,session',
        backdata: 'name,data',
        uinns: '++id,things',
        ubrands: '++id,things'
    });

function fetchCampaigns(){
    function getPharmacies() {
  return axios.get('/api/v1/pharmacy/get-pharmacies/');
}
    function getDistricts() {
  return axios.get('/api/v1/options/get-districts/');
}

function getAvailableTests() {
  return axios.get('/api/v1/options/get-available-tests/');
}

function getDrugReferences() {
  return axios.get('/api/v1/options/get-drug-references/');
}

function getInns() {
  return axios.get('/api/v1/options/get-inns/');
}

function getPrescribers() {
  return axios.get('/api/v1/options/get-prescribers/');
}

function getDivisions() {
  return axios.get('/api/v1/options/get-divisions/');
}

function getSalesDrivers() {
  return axios.get('/api/v1/options/get-sales-drivers/');
}

function getSwitchReasons() {
  return axios.get('/api/v1/options/get-switch-reasons/');
}

function getStaffFollowed() {
  return axios.get('/api/v1/options/get-staff-followed/');
}

function getDistrictProfiles() {
  return axios.get('/api/v1/options/get-district-profiles/');
}

function getPharmacyStandards() {
  return axios.get('/api/v1/options/get-pharmacy-standards/');
}

function getDistrictStandards() {
  return axios.get('/api/v1/options/get-district-standards/');
}

function getInsuranceTypes() {
  return axios.get('/api/v1/options/get-insurance-types/');
}



axios.all([getPharmacies(), getDistricts(), getAvailableTests(), getDrugReferences(), getInns(), getPrescribers(), getDivisions(), getSalesDrivers(), getSwitchReasons(), getStaffFollowed(), getDistrictProfiles(), getPharmacyStandards(), getDistrictStandards(), getInsuranceTypes()])
  .then(axios.spread(function (pharmacies, districts, tests, refs, inns, pribers, isions, drivers, swireason, stowed, dprof, phasta, dissta, instyp) {
    console.log(pharmacies.data.objects)
    db.backdata.put({name:"pharmacies", data:pharmacies.data.objects}).then(
    console.log("added"))

    console.log(districts.data.objects)
    db.backdata.put({name:"districts", data:districts.data.objects}).then(
    console.log("added"))

console.log(tests.data.objects)
    db.backdata.put({name:"available_tests", data:tests.data.objects}).then(
    console.log("added"))

console.log(refs.data.objects)
    db.backdata.put({name:"drug_references", data:refs.data.objects}).then(
    console.log("added"))

console.log(inns.data.objects)
    db.backdata.put({name:"inns", data:inns.data.objects}).then(
    console.log("added"))

console.log(pribers.data.objects)
    db.backdata.put({name:"prescribers", data:pribers.data.objects}).then(
    console.log("added"))

console.log(isions.data.objects)
    db.backdata.put({name:"divisions", data:isions.data.objects}).then(
    console.log("added"))


console.log(drivers.data.objects)
    db.backdata.put({name:"sales_drivers", data:drivers.data.objects}).then(
    console.log("added"))

console.log(swireason.data.objects)
    db.backdata.put({name:"switch_reasons", data:swireason.data.objects}).then(
    console.log("added"))

console.log(stowed.data.objects)
    db.backdata.put({name:"staff_followed", data:stowed.data.objects}).then(
    console.log("added"))

console.log(dprof.data.objects)
    db.backdata.put({name:"district_profiles", data:dprof.data.objects}).then(
    console.log("added"))

console.log(phasta.data.objects)
    db.backdata.put({name:"pharmacy_standards", data:phasta.data.objects}).then(
    console.log("added"))

console.log(dissta.data.objects)
    db.backdata.put({name:"district_standards", data:dissta.data.objects}).then(
    console.log("added"))


console.log(instyp.data.objects)
    db.backdata.put({name:"insurance_types", data:instyp.data.objects}).then(
    console.log("added"))

  }));

    // get country
    var country = "Ghana"
    const mydata = {country:country}
    fetch(window.location.origin+"/api/v1/campaigns/fetch/", {
method: 'POST', // *GET, POST, PUT, DELETE, etc.
 mode: 'no-cors', // no-cors, cors, *same-origin
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
     console.log(data);
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
        tr += `<td><a href="/campaigns/new-pharmacy/" onclick="saveCampaign('`+data.objects[i]['name']+`',`+data.objects[i]['id']+`)" class="btn btn-light"><img src="/static/images/icon-viewlink.svg" /> Open</a> <a onclick="fetchCampaigns()" class="btn btn-primary text-white">Update this campaign</a></td>`
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

function saveCampaign(name,id){
    localStorage.setItem('campaign',name)
    localStorage.setItem('campaignId',id)
}