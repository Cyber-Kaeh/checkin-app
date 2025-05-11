import { db } from "./firebase-init.js";

document.getElementById("loginButton").addEventListener("click", async () => {
  const phone = document.getElementById("phoneInput").value.trim();
  const name = document.getElementById("nameInput").value.trim();

  if (!phone || !name) {
    alert("Please enter both phone number and name.");
    return;
  }

  try {
    // Check if the phone number exists in the database
    const membersRef = db.child("members");
    const snapshot = await membersRef.orderByChild("phone").equalTo(phone).once("value");

    if (snapshot.exists()) {
      const members = snapshot.val();
      const memberKey = Object.keys(members)[0];
      const member = members[memberKey];

      if (member.name === name) {
        // Name matches, log the user in
        alert("Login successful!");
        window.location.href = "/dashboard";
      } else {
        // Name does not match
        alert("Name does not match the phone number.");
      }
    } else {
      // Phone number does not exist, create a new entry
      const newMember = {
        name: name,
        phone: phone,
        available: false, // Default value
      };

      await membersRef.push(newMember);
      alert("Account created successfully!");
      window.location.href = "/dashboard";
    }
  } catch (error) {
    console.error("Error during login:", error);
    alert("An error occurred. Please try again.");
  }
});