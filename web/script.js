// Onclick of the button
document.querySelector("button").onclick = function () {  
    // Call python's random_python function
    url1 = document.getElementById("link").value
    console.log(url1)
    eel.random_python(url1)(function(url){                        
      // Update the div with a random number returned by python
      document.querySelector(".output").innerHTML = url;
    })
  }
