eel.expose(displayImages);
function displayImages(imageUrls) {
    const container = document.getElementById("image-container");
    container.innerHTML = "";

    for (const url of imageUrls) {
        const img = document.createElement("img");
        img.src = url;
        container.appendChild(img);
    }
}

function loadImages() {
    eel.load_images()();
}
