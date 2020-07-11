var loadFile = function(event) {
    var reader = new FileReader();
    reader.onload = function(){
      var output = document.getElementById('output');
      output.src = reader.result;
      localStorage.setItem("imaging", output.src)
      console.log("the source is", output.src)
    };
    reader.readAsDataURL(event.target.files[0]);
  }

function Register() {

    console.log("register defined")
    uploadedImage = localStorage.getItem("imaging")
    /**
      * Registration function
      *
      * @variables All the input items on teh registration form
      *   The messenger.
      */
  
    var idnum = document.getElementById("member_id");
    var name = document.getElementById("recipient_name");
    var gender = document.getElementById("gender");
    var dob = document.getElementById("date_of_birth");
    var mstatus = document.getElementById("marital-status");
    var cell = document.getElementById("cell");
    var educ = document.getElementById("education_level");
    var prof = document.getElementById("profession");
    var occup = document.getElementById("occupation");
    var work = document.getElementById("place-of-work");
    var resid = document.getElementById("residence");
    var phon = document.getElementById("phone_contact");
    var email = document.getElementById("email");
    var dobapt = document.getElementById("date_of_baptism");
    var pobapt = document.getElementById("place_of_baptism");
    var baptpr = document.getElementById("baptising_pastor");
    var formr = document.getElementById("former_religion");
    var imag = document.getElementById("image_url");

    console.log("the image url is", imag.value)
    if (idnum.value == "") {
      document.getElementById("idErr").innerHTML = "Id must be filled";
    } else if (name.value == "") {
      document.getElementById("recnameErr").innerHTML = "Please fill in the Name";
    } else if (gender.value == " ") {
      document.getElementById("genderr").innerHTML = "Please select gender";
    } else if (dob.value == " ") {
      document.getElementById("doberr").innerHTML = "Fill in the date of birth";
    } else if (mstatus.value == "") {
      document.getElementById("mserr").innerHTML = "Please select marital status";
    } else if (cell.value == " ") {
      document.getElementById("cellerr").innerHTML =
        "Please fill in the cell name";
    } else if (educ.value == "") {
      document.getElementById("educerr").innerHTML =
        "Please fill in education level";
    } else if (prof.value == "") {
      document.getElementById("proferr").innerHTML =
        "Please provide the profession";
    } else if (occup.value == "") {
      document.getElementById("occuperr").innerHTML =
        "Please fill in the occupation";
    } else if (work.value == "") {
      document.getElementById("workerr").innerHTML = "Fill in the place of work";
    } else if (resid.value == "") {
      document.getElementById("residerr").innerHTML =
        "Provide the place of residence";
    } else if (phon.value == "") {
      document.getElementById("phoneerr").innerHTML =
        "Please fill in the phone number";
    } else if (email.value == "") {
      document.getElementById("mailerr").innerHTML =
        "Please provide the email address";
    } else if (dobapt.value == "") {
      document.getElementById("dobpterr").innerHTML =
        "Provide the date of baptism";
    } else if (pobapt.value == "") {
      document.getElementById("placerr").innerHTML =
        "Provide the place of baptism";
    } else if (baptpr.value == "") {
      document.getElementById("cpasterr").innerHTML =
        "Provide the name of the pastor who baptised";
    } else if (formr.value == "") {
      document.getElementById("formerr").innerHTML =
        "Please fill in the former religion";
    } else if (imag.value == "") {
      document.getElementById("imgerr").innerHTML =
        "Please provide the person's image";
    } else {
      console.log("Id number is", idnum.value);
      let userdata = {
        user_id: idnum.value,
        name: name.value,
        gender: gender.value,
        dateofbirth: dob.value,
        maritalstatus: mstatus.value,
        cell: cell.value,
        educationlevel: educ.value,
        profession: prof.value,
        occupation: occup.value,
        placeofwork: work.value,
        residence: resid.value,
        phonecontact: phon.value,
        emailaddress: email.value,
        dateofbaptism: dobapt.value,
        placeofbaptism: pobapt.value,
        baptisingpastor: baptpr.value,
        formerreligion: formr.value,
        image: uploadedImage,
        uploadedImage: uploadedImage 
    
        
        // "imageurl":imag.value
      };
      console.log("the data to be posted is", userdata)
  
  
      let token = localStorage.getItem("access_token");
  
      fetch("http://localhost:5000/api/v1/auth/register", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
          "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify(userdata)
        // console.log(userdata)
      })
  
      .then(response => response.json())
        .then(data => {
          if (data.message === "Member has been successfully registered") {
            console.log("you have successfully registered", name.value);
            document.querySelector("#parcelForm").reset();
          }
  
        });
    }
    }