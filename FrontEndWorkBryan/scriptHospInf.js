const hospitalName = document.getElementById("hospitalName");
const hospitalInfo = document.getElementById("hospitalInfo");
const reviewsContainer = document.getElementById("reviewsContainer");

const ratingSelect = document.getElementById("ratingSelect");
const reviewText = document.getElementById("reviewText");
const submitReview = document.getElementById("submitReview");
const message = document.getElementById("message");

//  temporary database
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

// hospital ID from URL
const params = new URLSearchParams(window.location.search);
const hospitalId = params.get("id");

if (!hospitalId || !hospitalData[hospitalId]) {
  hospitalName.textContent = "Hospital not found.";
} else {
  const hospital = hospitalData[hospitalId];

  hospitalName.textContent = hospital.name;
  hospitalInfo.textContent = hospital.info;

  displayReviews(hospital);
}

function displayReviews(hospital) {
  reviewsContainer.innerHTML = "";

  if (hospital.reviews.length === 0) {
    reviewsContainer.textContent = "No reviews yet.";
    return;
  }

  hospital.reviews.forEach(r => {
    const div = document.createElement("div");
    div.textContent = `${r.rating} Stars - ${r.text}`;
    reviewsContainer.appendChild(div);
  });
}

submitReview.addEventListener("click", () => {
  const rating = ratingSelect.value;
  const text = reviewText.value.trim();

  if (!rating) {
    message.textContent = "Please select a rating.";
    return;
  }

  hospitalData[hospitalId].reviews.push({
    rating: rating,
    text: text
  });

  displayReviews(hospitalData[hospitalId]);

  ratingSelect.value = "";
  reviewText.value = "";
  message.textContent = "Review added!";
});