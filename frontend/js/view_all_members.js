function getMembers() {
    console.log("can you read me darling")
    let token = localStorage.getItem("access_token");
  
    fetch("http://localhost:5000/api/v1/members", {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
        "Access-Control-Allow-Origin": "*"
      }
    })
      .then(response => response.json())
      .then(res => {
        console.log("all the members are", res);
        //   if (res.msg == "Token has expired") {
        //     // customModal("Session expired! Login to proceed");
        //     let ok = document.getElementById("ok");
        //     ok.onclick = function() {
        //       location.href = "../../index.html";
        //     };
        //   } else {
  
        let tdata = "";
        //     let arr = [];
        //     let myNewArr = [];
        // loop throught the data returned by the request
        res.message.forEach(member => {
          document.getElementById("imager").innerHTML = member.image;
  
          //    if (parcel.status == "intransit" || parcel.status == "pending") {
          tdata += `
                    <tr>
                         <td>${member.name}</td>
                         <td>${member.gender}</td>
                         <td>${member.maritalstatus}</td>
                         <td>${member.cell}</td>
                         <td>${member.residence}</td>
                         <td>${member.phonecontact}</td>
                         <td>  <a href = '../templates/view_one_member.html?id=${member.user_id}'> <button>view profile</button> </a></td>
    
                         </tr>`;
        });
        document.getElementById("tbody").innerHTML = tdata;
      });
  }
  