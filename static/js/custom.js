(function($) {
	"use strict";	
	
	// ______________Active Class
	$(document).ready(function() {
		$(".horizontalMenu-list li a").each(function() {
			var pageUrl = window.location.href.split(/[?#]/)[0];
			if (this.href == pageUrl) {
				$(this).addClass("active");
				$(this).parent().addClass("active"); // add active to li of the current link
				$(this).parent().parent().prev().addClass("active"); // add active class to an anchor
				$(this).parent().parent().prev().click(); // click the item to make it drop
			}
		});
	});
	
	// ______________ Back to Top
	$(window).on("scroll", function(e) {
		if ($(this).scrollTop() > 0) {
			$('#back-to-top').fadeIn('slow');
		} else {
			$('#back-to-top').fadeOut('slow');
		}
	});
	$("#back-to-top").on("click", function(e) {
		$("html, body").animate({
			scrollTop: 0
		}, 600);
		return false;
	});	

	$('select.dropdown')
  .dropdown()
;

$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;
	
	// ______________Quantity-right-plus
	var quantitiy = 0;
	$('.quantity-right-plus').on('click', function(e) {
		e.preventDefault();
		var quantity = parseInt($('#quantity').val()); 
		$('#quantity').val(quantity + 1); 
	});
	$('.quantity-left-minus').on('click', function(e) {
		e.preventDefault();
		var quantity = parseInt($('#quantity').val());
		if (quantity > 0) {
			$('#quantity').val(quantity - 1);
		}
	});	
	
	/*boYSIqMee+p4uAjskftSrErYaF9PDNDn+EGSzR9N2BspYI8=
feCz66HNQhyoUIndT6pXQpWta+PA3e1h3yExMyH1EsOo6f8PXnNPyHGLRfchOSF9WSX7exs=*/	
	
	// ______________Chart-circle
	if ($('.chart-circle').length) {
		$('.chart-circle').each(function() {
			let $this = $(this);
			$this.circleProgress({
				fill: {
					color: $this.attr('data-color')
				},
				size: $this.height(),
				startAngle: -Math.PI / 4 * 2,
				emptyFill: '#f9faff',
				lineCap: ''
			});
		});
	}
	
	// ______________HEADER COLOR
	$(document).on('click', '#myonoffswitch', function(e){
		if (this.checked) {
			$('body').addClass('top-header-light');
			$('body').removeClass('top-header-dark');
		}
		else {
			$('body').removeClass('top-header-color');
			localStorage.setItem("top-header-color", "false");
		}
	});
	
	// ______________HEADER COLOR
	$(document).on('click', '#myonoffswitch1', function(e){
		if (this.checked) {
			$('body').addClass('top-header-dark');
			$('body').removeClass('top-header-light');
		}
		else {
			$('body').removeClass('top-header-dark');
			localStorage.setItem("top-header-dark", "false");
		}
	});
	
	// ______________HEADER COLOR
	$(document).on('click', '#myonoffswitch3', function(e){
		if (this.checked) {
			$('body').removeClass('horizontal-gradient');
			$('body').removeClass('top-header-dark');
			$('body').removeClass('top-header-light');
			$('body').removeClass('banner-dark');
		}
		else {
			$('body').removeClass('Clear');
			localStorage.setItem("Clear", "false");
		}
	});
	// ______________HEADER COLOR
	$(document).on('click', '#myonoffswitch2', function(e){
		if (this.checked) {
			$('body').addClass('horizontal-gradient');
		}
		else {
			$('body').removeClass('horizontal-gradient');
			localStorage.setItem("horizontal-gradient", "false");
		}
	});
	
	// ______________HEADER COLOR
	$(document).on('click', '#myonoffswitch4', function(e){
		if (this.checked) {
			$('body').addClass('banner-dark');
		}
		else {
			$('body').removeClass('banner-dark');
			localStorage.setItem("banner-dark", "false");
		}
	});
	
	const DIV_CARD = 'div.card';	
	
	
	// ______________Tooltip
	$('[data-toggle="tooltip"]').tooltip();
	
	// ______________Popover
	$('[data-toggle="popover"]').popover({
		html: true
	});
	
	// ______________Card Remove
	$('[data-toggle="card-remove"]').on('click', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.remove();
		e.preventDefault();
		return false;
	});
	
	// ______________Card Collapse
	$('[data-toggle="card-collapse"]').on('click', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.toggleClass('card-collapsed');
		e.preventDefault();
		return false;
	});
	
	// ______________Card Full Screen
	$('[data-toggle="card-fullscreen"]').on('click', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.toggleClass('card-fullscreen').removeClass('card-collapsed');
		e.preventDefault();
		return false;
	});


	//______________Indexeddb
	
	  $(document).ready(function(){

	  
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
		var basketStore = db.createObjectStore("baskets", {keyPath: "id"},{autoIncrement: "true"});
		if (!window.indexedDB) {
			console.log("Your browser doesn't support a stable version of IndexedDB. Such and such feature will not be available.");
		  }
		  $('.positive.ui.big.submit.button"]').on('click', function collectForm() {
			var
				$form = $('.form'),
				allFields = $form.form('get values')
				;
			console.log(allFields);
			store();
		});
	
	
		  function store () {
			// create the transaction with 1st parameter is the list of stores and the second specifies
			// a flag for the readwrite option
			var transaction = db.transaction([ 'baskets' ], 'readwrite');
		
			
			//Create the Object to be saved i.e. our details
			var allFields;
		
			// add the details to the store
			var store = transaction.objectStore('baskets');
			var request = store.add(allFields);
			request.onsuccess = function (e) {
				alert("Your Basket data has been saved");
			};
			request.onerror = function (e) {
				alert("Error in saving the basket data. Reason : " + e.value);
			}
		}
	  };
	});
				  
})(jQuery);
