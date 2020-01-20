if (!window.indexedDB) {
  console.log("Your browser doesn't support a stable version of IndexedDB. Such and such feature will not be available.");
}

document.getElementById('name').oninput = function () {
  var sessionName = this.value;
  console.log(sessionName)
}




var db;
// Let us open our database
var request = window.indexedDB.open("POP Ghana");
request.onerror = function(event) {
  // Do something with request.errorCode!
  console.log("Why didn't you allow my web app to use IndexedDB?!");
};
request.onsuccess = function(event) {
  // Do something with request.result!
  db = event.target.result;
  db.onerror = function(event) {
    // Generic error handler for all errors targeted at this database's
    // requests!
    console.error("Database error: " + event.target.errorCode);
  };
};


// This event is only implemented in recent browsers   
request.onupgradeneeded = function(event) { 
  // Save the IDBDatabase interface 
  var db = event.target.result;

  // Create an objectStore for this database
  var sessionStore = db.createObjectStore("sessions", { keyPath: "id" }, {autoIncrement: "true"});
  var pharmacyStore = db.createObjectStore("pharmacies", {keyPath: "id"},{autoIncrement: "true"});
};




function addDrug() {
  
  document.getElementById('newdrug').innerHTML += `<h3>New Drug</h3><div class="control-group">
  <label class="control-label" for="drug_initial_request">Initial request
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(Who started the request?)" title="Who started the request?"></label>
  <div class="controls">
      <select name="drug_initial_request" id="drug_initial_request" required>
          <option value="" selected>---------</option>
  
          <option value="brand patient">brand patient</option>
  
          <option value="brand prescription">brand prescription</option>
  
          <option value="inn patient">inn patient</option>
  
          <option value="inn prescription">inn prescription</option>
  
      </select>
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_sold">Drug sold
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(brand name of drug that has been sold?)"
          title="brand name of drug that has been sold?"></label>
  <div class="controls">
      <input type="text" name="drug_sold" class="form-control" maxlength="200" id="drug_sold">
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_sale_driver">&nbsp;<img src="images/icon-unknown.svg"
          class="help help-tooltip" width="10" height="10"
          alt="(Who makes the final selection for the purchased product?)"
          title="Who makes the final selection for the purchased product?"></label>
  <div class="controls">
      <select name="drug_sale_driver" id="drug_sale_driver">
          <option value="" selected>---------</option>
  
          <option value="Patient">Patient</option>
  
          <option value="Pharmacist">Pharmacist</option>
  
          <option value="Prescriber">Prescriber</option>
  
      </select>
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_switched">Switched
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(Was there a switch?)" title="Was there a switch?"></label>
  <div class="controls">
      <input type="checkbox" name="drug_switched" id="drug_switched">
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_switched">Leaked&nbsp;<img src="images/icon-unknown.svg"
          class="help help-tooltip" width="10" height="10" alt="(Was there a leak?)"
          title="Was there a leak?">
  </label>
  <div class="controls">
      <input type="checkbox" name="drug_leaked" id="drug_leaked">
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_product_switched_or_leaked">Product switched or leaked
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(What product was switched or leaked?)"
          title="What product was switched or leaked?"></label>
  <div class="controls">
      <input type="text" name="drug_product_switched_or_leaked" class="form-control" maxlength="200"
          id="drug_product_switched_or_leaked">
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="reason_for_switch_or_leak">Reason for switch or leak
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(Why was there a switch or a leak?)" title="Why was there a switch or a leak?"></label>
  <div class="controls">
      <select name="reason_for_switch_or_leak" id="reason_for_switch_or_leak">
          <option value="" selected>---------</option>
  
          <option value="Not available">Not available</option>
  
          <option value="Price">Price</option>
  
          <option value="Therapeutic Reason">Therapeutic Reason</option>
  
          <option value="Other Reason">Other Reason</option>
  
      </select>
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_form_sold">Form sold
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(What form of drug was sold? liquid,tablet)"
          title="What form of drug was sold? liquid,tablet"></label>
  <div class="controls">
      <select name="drug_form_sold" id="drug_form_sold">
          <option value="" selected>---------</option>
  
          <option value="3">Capsule</option>
  
          <option value="7">Cream</option>
  
          <option value="14">Ear drop</option>
  
          <option value="15">Eye drop</option>
  
          <option value="9">Gel</option>
  
          <option value="12">Inhaler</option>
  
          <option value="6">Injection</option>
  
          <option value="8">Ointment</option>
  
          <option value="10">Patch</option>
  
          <option value="13">Pessary</option>
  
          <option value="16">Powder</option>
  
          <option value="11">Spray</option>
  
          <option value="1">Suppositories</option>
  
          <option value="4">Suspension</option>
  
          <option value="5">Syrup</option>
  
          <option value="2">Tablet</option>
  
      </select>
  
  </div>
  </div>
  
  
  <div class="control-group">
  <label class="control-label" for="drug_division">Division
      &nbsp;<img src="images/icon-unknown.svg" class="help help-tooltip" width="10" height="10"
          alt="(Was the whole box sold? How was it divided?)"
          title="Was the whole box sold? How was it divided?"></label>
  <div class="controls">
      <select name="drug_division" id="drug_division">
          <option value="" selected>---------</option>
  
          <option value="unit">unit</option>
  
          <option value="blister">blister</option>
  
          <option value="box">box</option>
  
          <option value="blister+unit">blister+unit</option>
  
          <option value="box+unit">box+unit</option>
  
          <option value="box+blister">box+blister</option>
  
      </select>
  
  </div>
  </div>
  
  
  </form>`;
  
};