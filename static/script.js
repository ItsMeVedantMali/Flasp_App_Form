document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value
  }; 

  fetch("https://your-flask-app-url.onrender.com/submit", {  // <-- use your real deployed URL
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
  .then(res => res.text())
  .then(response => {
    document.getElementById("responseMessage").innerText = response;
    document.getElementById("contactForm").reset();
  })
  .catch(error => {
    document.getElementById("responseMessage").innerText = "Something went wrong!";
    console.error('Error:', error);
  });
});
