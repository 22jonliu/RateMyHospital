const button = document.getElementById("searchButton");
const input = document.getElementById("nameInput");
const resultsContainer = document.getElementById("resultsContainer");

// Fake hospital database (replace with real API later)
const hospitals = [
  { id: "city-hospital", name: "City Hospital" },
  { id: "metro-health", name: "Metro Health Center" },
  { id: "sunrise-clinic", name: "Sunrise Clinic" }
];

button.addEventListener("click", () => {
  const searchValue = input.value.trim().toLowerCase();
  resultsContainer.innerHTML = "";

  const found = hospitals.find(h =>
    h.name.toLowerCase() === searchValue
  );

  if (!found) {
    resultsContainer.textContent = "Hospital not found.";
    return;
  }

  const link = document.createElement("a");
  link.href = `hospitalInf.html?id=${found.id}`;
  link.textContent = found.name;
  link.classList.add("result-link");

  resultsContainer.appendChild(link);
});
