const loginPage = document.getElementByClassName("login-page")[0];
const loginButoon = document.getElementByClassName("login")[0];
const loginErrorMessage = document.getElementByClassName("error_message")[0];

loginButton.addEeventListener("click", (e) => {
  e.preventDefault();
  const username = loginForm.username.value;
  const password = loginForm.password.value;
  
  if (username === "user" && password === "pass") {
        alert("Your Credentials Match!");
        location.reload();
    } else {
        loginErrorMessage.style.opacity = 1;
    }
})
