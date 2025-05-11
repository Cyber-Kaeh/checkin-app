import { auth, provider, db } from "./firebase-init.js";

document.getElementById("signInButton").addEventListener("click", () => {
    auth
      .signInWithPopup(provider)
      .then(async (result) => {
        const user = result.user;
        console.log(`User signed in: ${user.displayName}`);

        // Check if user exists in Firestore
        const userRef = db.collection("users").doc(user.uid);
        const doc = await userRef.get();

        if (doc.exists) {
          // User exists, redirect to dashboard
          window.location.href = "/dashboard";
        } else {
          // User does not exist, redirect to signup
          window.location.href = "/signup";
        }
      })
      .catch((error) => {
        console.error(`Sign-in error: ${error.message}`);
      });
  });