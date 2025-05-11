import { auth } from "./firebase-init.js";
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.7.1/firebase-auth.js";

onAuthStateChanged(auth, (user) => {
  const signInButton = document.getElementById("signInButton");

  if (user) {
    console.log("User is signed in:", user.phoneNumber || user.email);
    signInButton.textContent = "Sign Out";
    signInButton.addEventListener("click", () => {
      auth.signOut().then(() => {
        alert("Signed out successfully!");
        window.location.href = "/";
      });
    });
  } else {
    console.log("No user is signed in.");
    signInButton.textContent = "Log In";
    signInButton.href = "/login";
  }
});