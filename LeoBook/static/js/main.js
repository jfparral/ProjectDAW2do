var pageCounter = 1;
var numero = 1;
var animalContainer = document.getElementById("book-info");
var btn = document.getElementById("btnSaber");

btn.addEventListener("click", function() {
  var ourRequest = new XMLHttpRequest();
  ourRequest.open('GET', 'https://dawteam.github.io/WebApp/data/topbooks' + pageCounter +  '.json');
  ourRequest.onload = function() {
    if (ourRequest.status >= 200 && ourRequest.status < 400) {
      var ourData = JSON.parse(ourRequest.responseText);
      renderHTML(ourData);
    } else {
      console.log("We connected to the server, but it returned an error.");
    }
    
  };

  ourRequest.onerror = function() {
    console.log("Connection error");
  };

  ourRequest.send();
  pageCounter++;
  if (pageCounter > 3) {
    btn.classList.add("hide-me");
  }
});

function renderHTML(data) {


  var htmlString = "";
  

  for (i = 0; i < data.length; i++) {
  	
    htmlString += "<p>" + "<strong>" + numero + ") " + data[i].name + "</strong>"  + "</p>" +  
    "<p>" + "Autor: " + data[i].author +   " | Género: " + data[i].genre+ "</p>";
 	numero += 1;   
 

  }

  animalContainer.insertAdjacentHTML('beforeend', htmlString);
}

