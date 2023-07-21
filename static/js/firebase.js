  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.22.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyA0S91PlNeTylx0TuzmIQqyf8syOyT8nVk",
    authDomain: "blog-108b0.firebaseapp.com",
    projectId: "blog-108b0",
    storageBucket: "blog-108b0.appspot.com",
    messagingSenderId: "15346562257",
    appId: "1:15346562257:web:3a86494cb0177cba9081f0",
    measurementId: "G-ESXQ31SCTD"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);