const container = document.getElementById("container");
const registerbtn = document.getElementById("register");
const loginbtn = document.getElementById("login");

registerbtn.addEventListener("click", () => {
  container.classList.add("active");
});

loginbtn.addEventListener("click", () => {
  container.classList.remove("active");
});
// Password strength checker function
function checkPasswordStrength(password) {
  const strengthMessage = document.getElementById("password-strength-message");

  // Check password length
  if (password.length < 8) {
    strengthMessage.innerText = "Password must be at least 8 characters long.";
    strengthMessage.style.color = "red";
    return false;
  }

  // Check for at least one digit
  if (!/\d/.test(password)) {
    strengthMessage.innerText = "Password must contain at least one digit.";
    strengthMessage.style.color = "red";
    return false;
  }

  // Check for at least one uppercase letter
  if (!/[A-Z]/.test(password)) {
    strengthMessage.innerText = "Password must contain at least one uppercase letter.";
    strengthMessage.style.color = "red";
    return false;
  }

  // Check for at least one lowercase letter
  if (!/[a-z]/.test(password)) {
    strengthMessage.innerText = "Password must contain at least one lowercase letter.";
    strengthMessage.style.color = "red";
    return false;
  }

  // If all checks pass
  strengthMessage.innerText = "Password is strong!";
  strengthMessage.style.color = "green";
  return true;
}

// Event listeners for password inputs
document.getElementById("sign-up-password").addEventListener("input", function () {
  checkPasswordStrength(this.value);
});

document.getElementById("sign-in-password").addEventListener("input", function () {
  checkPasswordStrength(this.value);
});
