function Login() {
    /**
      * Login function
      *
      * @param username
      * @param password
      * the authenticated username should be admin with a password of Admin1234567
      */
    var name = document.getElementById("login_name");
    var password = document.getElementById("login_password");
  
    if (name.value === "admin" && password.value === "Admin1234567") {
      document.location.href = "./templates/register.html";
    } else {
      document.getElementById("err").innerHTML =
        "Name and password did not match, try again!";
    }
  }