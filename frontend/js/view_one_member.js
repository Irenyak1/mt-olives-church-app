function GetoneMember() {
  console.log("do u see me", document.getElementById("gender").innerHTML)


  var r = window.location.href
  user_id = r.split('=')[1].split('%')[0]

  let token = localStorage.getItem("access_token");

  fetch(`http://localhost:5000/api/v1/members/${user_id}`, {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      "Access-Control-Allow-Origin": "*"
    }
  })


    .then(response => response.json())
    .then(res => {
      console.log("this is itjhgjhg", res.message.gender)
      image = res.message.image
      document.getElementById("gender").innerHTML = res.message.gender;

      document.getElementById("userid").innerHTML = res.message.user_id;
      document.getElementById("name").innerHTML = res.message.name;

      document.getElementById("mobile").innerHTML = res.message.phonecontact;
      document.getElementById("email").innerHTML = res.message.emailaddress
      document.getElementById("maritalstatus").innerHTML = res.message.maritalstatus
      document.getElementById("cell").innerHTML = res.message.cell
      document.getElementById("education").innerHTML = res.message.educationlevel
      document.getElementById("proffession").innerHTML = res.message.profession
      document.getElementById("occupation").innerHTML = res.message.occupation
      document.getElementById("residence").innerHTML = res.message.residence
      document.getElementById("bapdate").innerHTML = res.message.dateofbaptism
      document.getElementById("bapplace").innerHTML = res.message.placeofbaptism

      document.getElementById("bappas").innerHTML = res.message.baptisingpastor
      document.getElementById("formerrel").innerHTML = res.message.formerreligion
      document.getElementById("imao").innerHTML = `<img src="${image}" alt="sddsfgdg"></img>`




    });



}