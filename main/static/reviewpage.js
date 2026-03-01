const hospitalContainer = document.getElementById("hospitalContainer");

//Temproary Hospital data
const hospitalData = {
  "city-hospital": {
    name: "City Hospital",
    info: "Located downtown. 24/7 emergency services.",
    reviews: []
  },
  "metro-health": {
    name: "Metro Health Center",
    info: "Specializes in cardiology and pediatrics.",
    reviews: []
  },
  "sunrise-clinic": {
    name: "Sunrise Clinic",
    info: "Community clinic with affordable care.",
    reviews: []
  }
};

for (let key in hospitalData){
    const hospital = hospitalData[key];

    const card = document.createElement("div");
    card.classList.add("hospital-card");
    card.innerHTML = `
        <h2>${hospital.name}</h2>
        <p>${hospital.info}</p>
    `;

    hospitalContainer.appendChild(card);

}

const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", function( ){
    const searchValue = searchInput.value.toLowerCase();
    
    const cards = document.querySelectorAll(".hospital-card");

    cards.forEach(card => {
        const hospitalName = card.querySelector("h2").textContent.toLowerCase();

        if (hospitalName.includes(searchValue)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    });
});