
function getMembers() {
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
  
        let tdata = "";

        res.message.forEach(member => {
          document.getElementById("imager").innerHTML = member.image;
            tdata += `
                    <tr>
                         <td>${member.name}</td>
                         <td>${member.gender}</td>
                         <td>${member.maritalstatus}</td>
                         <td>${member.cell}</td>
                         <td>${member.residence}</td>
                         <td>${member.phonecontact}</td>
                         <td>  <a href = view_one_member.html?id=${member.user_id}'> <button>view profile</button> </a></td>
    
                         </tr>`;
        });
        document.getElementById("tbody").innerHTML = tdata;
      });
  }


  
  