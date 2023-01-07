// var staticCacheName = "django-pwa-phars+" +new Date().getDay()+":"+new Date().getHours()+":"+new Date().getMinutes();
// // console.log(staticCacheName)
// var filesToCache = [
//   '/static/CSS/style3.css',
//   '/static/CSS/bootstrap.min.css',
//   '/static/CSS/animate.css',
//   '/static/CSS/Style.css',
//   '/static/js/bootstrap.min.js',
//   '/static/js/bootstrap3.min.js',
//   '/static/js/popper.min.js',
//   '/static/js/slim.min.js',
//   '/static/js/jquery.min.js',
//   'https://use.fontawesome.com/releases/v5.7.0/css/all.css',
//   'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
//   '/offline',
// ];

// // Cache on install
// self.addEventListener("install", event => {
//     this.skipWaiting();
//     event.waitUntil(
//         caches.open(staticCacheName)
//             .then(cache => {
//         return fetch('/offline/')
//         .then(response => cache.put('/offline/', new Response(response.body)));
//             })
//     )
// });

// // Clear cache on activate
// self.addEventListener('activate', event => {
//     event.waitUntil(
//         caches.keys().then(cacheNames => {
//             return Promise.all(
//                 cacheNames
//                     .filter(cacheName => (cacheName.startsWith("django-pwa-phars+"+new Date().getDay()+":"+new Date().getHours())))
//                     .filter(cacheName => (cacheName !== staticCacheName))
//                     .map(cacheName => caches.delete(cacheName))
//             );
//         })
//     );
// });


// // Serve from Cache
// self.addEventListener("fetch", event => {
//     event.respondWith(
//         caches.match(event.request)
//             .then(response => {
//                 return response || fetch(event.request);
//             })
//             .catch(() => {
//                 return caches.match('/offline/');
//             })
//     )
// });




var filesToCache = [
  '/static/plugins/dexie/dexie.js',
  '/static/plugins/bootstrap-4.3.1-dist/css/bootstrap.min.css',
  '/static/css/animate.css',
  '/static/css/style.css',
  '/static/css/icons.css',
  '/static/plugins/scroll-bar/jquery.mCustomScrollbar.css',
  '/static/color-skins/color-skins/color10.css',
  '/static/plugins/Semantic-UI-CSS/semantic.min.css',
  '/static/js/bootstrap3.min.js',
  '/static/js/jquery.min.js',
  '/static/js/vendors/jquery-3.2.1.min.js',
  '/static/plugins/bootstrap-4.3.1-dist/js/popper.min.js',
  '/static/plugins/bootstrap-4.3.1-dist/js/bootstrap.min.js',
  '/static/plugins/Semantic-UI-CSS/semantic.min.js',
  '/static/js/vendors/circle-progress.min.js',
  '/static/plugins/scroll-bar/jquery.mCustomScrollbar.concat.min.js',
  '/static/js/custom.js',
  '/static/js/axios.min.js',
  '/static/js/campaign.js',
  '/static/js/login.js',
  '/campaigns/new-basket',
  '/campaigns/new-pharmacy',
  '/campaigns/new-session',
  '/campaigns/observation-session',
  '/campaigns/lockscreen',
  '/campaigns/edit-session',
  '/campaigns/edit-basket',
  '/campaigns/edit-pharmacy'
];

var staticCacheName = "django-pwa-observe" +new Date().getDay()+":"+new Date().getHours()+":"+new Date().getMinutes();



self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll(filesToCache);
    })
  );
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-observe"+new Date().getDay()+":"+new Date().getHours())))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});




// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/campaigns');
            })
    )
});

self.onnotificationclick = function(event) {
  console.log('On notification click: ', event.notification.tag);
  event.notification.close();

  // This looks to see if the current is already open and
  // focuses if it is
  event.waitUntil(clients.matchAll({
    type: "window"
  }).then(function(clientList) {
    //   console.log(clientList)
    for (var i = 0; i < clientList.length; i++) {
      var client = clientList[i];
      var baseUrl = "https://observe.pywe.org"
      if (client.url == baseUrl+'/campaigns/' || client.url == baseUrl || client.url == baseUrl+'/api/v1/' && 'focus' in client)
        return client.focus();
    }
    if (clients.openWindow)
      return clients.openWindow('/campaigns');
  }));
};





// Register event listener for the 'push' event.
self.addEventListener('push', function (event) {
    // Retrieve the textual payload from event.data (a PushMessageData object).
    // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
    // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.
    const eventInfo = event.data.text();
    const data = JSON.parse(eventInfo);
    const head = data.head || 'New Notification 🕺🕺';
    const body = data.body || 'This is default content. Your notification didn\'t have one 🙄🙄';
    const tag = data.tag || 'incognito';


    // Keep the service worker alive until the notification is created.
    event.waitUntil(
        clients.matchAll().then(all => all.forEach(client => {
        if(tag=="typing"){
        client.postMessage("Hello there "+tag);
        }else{
        self.registration.showNotification(head, {
            body: body,
            icon: 'https://observe.pywe.org/static/images/logo.svg',
            vibrate: [300, 100, 400],
            tag:tag
        })
        }
    })));

});

self.addEventListener("message", function(event) {
    //event.source.postMessage("Responding to " + event.data);
    self.clients.matchAll().then(all => all.forEach(client => {
        client.postMessage("Responding to " + event.data);
    }));
});
// self.addEventListener('notificationclick', function(event) {
//   event.notification.close();
//     event.waitUntil(clients.matchAll({
//     type: "window"
//   }).then(function(clientList) {
//     for (var i = 0; i < clientList.length; i++) {
//       var client = clientList[i];
//       if (client.url == '/' && 'focus' in client)
//         return client.focus();
//     }
//     if (clients.openWindow)
//       return clients.openWindow('/drugapi/v1/results/');
//   }));

// });