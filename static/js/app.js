

//document.getElementById('name').oninput = function () {
  //var sessionName = this.value;
  //console.log(sessionName)
//}



  // Create an objectStore for this database
 // var sessionStore = db.createObjectStore("sessions", { keyPath: "id" }, {autoIncrement: "true"});
  //var pharmacyStore = db.createObjectStore("pharmacies", {keyPath: "id"},{autoIncrement: "true"});



  function idbOK() {
    return "indexedDB" in window;
}

var db;

$(document).ready(function() {

    //No support? Go in the corner and pout.
    if(!idbOK()) return;

    var openRequest = indexedDB.open("ora_idb1",1);

    openRequest.onupgradeneeded = function(e) {
        console.log("running onupgradeneeded");
    }

    openRequest.onsuccess = function(e) {
        console.log("running onsuccess");
        db = e.target.result;
    }

    openRequest.onerror = function(e) {
        console.log("onerror!");
        console.dir(e);
    }

});