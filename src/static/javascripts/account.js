function validatePassword() {
    var password = document.getElementsByName("password")[0];
    var confirm_password = document.getElementsByName("confirm_password")[0];

    if (password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}
