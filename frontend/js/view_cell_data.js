function loadNaj() {
  najeera = document.getElementById("naj").innerHTML
  let token = localStorage.getItem("access_token");
  fetch(`http://localhost:5000/api/v1/members/cells/${najeera}`, {
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
                         <td>  <a href = '../templates/view_one_member.html?id=${member.user_id}'> <button>view profile</button> </a></td>
    
                         </tr>`;
      });
      document.getElementById("tbody").innerHTML = tdata;
    });
}


function loadBuk() {
  bukoto = document.getElementById("buk").innerHTML
  let token = localStorage.getItem("access_token");
  fetch(`http://localhost:5000/api/v1/members/cells/${bukoto}`, {
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
                         <td>  <a href = '../templates/view_one_member.html?id=${member.user_id}'> <button>view profile</button> </a></td>
    
                         </tr>`;
      });
      document.getElementById("tbody").innerHTML = tdata;
    });
}


function loadKyal() {
  kyal = document.getElementById("kal").innerHTML
  let token = localStorage.getItem("access_token");
  fetch(`http://localhost:5000/api/v1/members/cells/${kyal}`, {
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
                         <td>  <a href = '../templates/view_one_member.html?id=${member.user_id}'> <button>view profile</button> </a></td>
    
                         </tr>`;
      });
      document.getElementById("tbody").innerHTML = tdata;
    });
}


function loadNal() {
  naalya = document.getElementById("nal").innerHTML
  let token = localStorage.getItem("access_token");

  fetch(`http://localhost:5000/api/v1/members/cells/${naalya}`, {
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
                         <td>  <a href = '../templates/view_one_member.html?id=${member.user_id}'> <button>view profile</button> </a></td>
    
                         </tr>`;
      });
      document.getElementById("tbody").innerHTML = tdata;
    });
}
