importScripts('https://www.gstatic.com/firebasejs/10.11.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.11.0/firebase-messaging-compat.js');

const firebaseConfig = {
  apiKey: "AIzaSyBtrJeMwMfj_rXWJe9000x2845S7Y1smCM",
  authDomain: "gunasekaran-80514.firebaseapp.com",
  projectId: "gunasekaran-80514",
  storageBucket: "gunasekaran-80514.appspot.com",
  messagingSenderId: "614767996940",
  appId: "1:614767996940:web:6f3b4106f60ece430d3e29",
  measurementId: "G-GNLVP9K3VX"
};

firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/icon.png'
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});