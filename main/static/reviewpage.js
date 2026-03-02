const hospitalContainer = document.getElementById("hospitalContainer");

async function loadHospitals() {
    try {
        const response = await fetch('/api/facilities/');
        const facilities = await response.json();

        hospitalContainer.innerHTML = ''; // Clear previous content

        if (facilities.length === 0) {
            hospitalContainer.innerHTML = '<p>No hospitals found in the database. Please make sure you have imported the data correctly.</p>';
            return;
        }

        facilities.forEach(facility => {
            const card = document.createElement("div");
            card.classList.add("hospital-card");
            card.innerHTML = `
                <h2>${facility.name}</h2>
                <div class="hospital-info">
                    <p><strong>📍 City:</strong> ${facility.city}</p>
                    <p><strong>🏠 Address:</strong> ${facility.full_address}</p>
                </div>
                <a href="/hospital/${facility.id}/" class="review-btn" style="display:inline-block; margin-top:10px; padding:10px 20px; background:#007bff; color:white; text-decoration:none; border-radius:5px; font-weight:bold;">
                    View & Write Reviews
                </a>
            `;
            hospitalContainer.appendChild(card);
        });
    } catch (error) {
        console.error('Error loading hospitals:', error);
        hospitalContainer.innerHTML = '<p>Error loading hospitals. Please try again later.</p>';
    }
}

// Initial load
loadHospitals();

const searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", function( ){
    const searchValue = searchInput.value.toLowerCase();
    
    const cards = document.querySelectorAll(".hospital-card");

    cards.forEach(card => {
        const hospitalName = card.querySelector("h2").textContent.toLowerCase();
        const hospitalCity = card.querySelector(".hospital-info").textContent.toLowerCase();

        if (hospitalName.includes(searchValue) || hospitalCity.includes(searchValue)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    });
});