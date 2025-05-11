// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.7.1/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.7.1/firebase-analytics.js";
import { getAuth, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/11.7.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/11.7.1/firebase-firestore.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAurrrsK2XH4PSKJrWDHrHYjU79_Rn04HM",
  authDomain: "spiritual-matters-signin.firebaseapp.com",
  projectId: "spiritual-matters-signin",
  storageBucket: "spiritual-matters-signin.firebasestorage.app",
  messagingSenderId: "1064211785611",
  appId: "1:1064211785611:web:eaedb07360bf6c11f4318e",
  measurementId: "G-3FFHRJ375X",
};
// export const firebaseConfig = {{ firebase_config|tojson|safe }};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const analytics = getAnalytics(app);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const provider = new GoogleAuthProvider();