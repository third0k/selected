function checkCredentials() {
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const correctMessage = document.getElementById("correct-message");
    const errorMessage = document.getElementById("error-message");

    const correctUsername = "Admin"; // 
    const correctPassword = "1234"; 

    if (usernameInput.value === correctUsername && passwordInput.value === correctPassword) {
        correctMessage.textContent = "Your username and password are correct! you are logged in";
        return false; 
    } else {
        errorMessage.textContent = "Your username or password is incorrect! please try again.";
        passwordInput.value = "";
        return false;
    }
}