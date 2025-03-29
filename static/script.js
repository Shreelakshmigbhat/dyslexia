async function translateText(toDyslexic) {
    let inputText = document.getElementById("inputText").value;

    let response = await fetch("http://127.0.0.1:8000/translate/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText, to_dyslexic: toDyslexic })
    });

    let data = await response.json();
    document.getElementById("outputText").innerText = data.translated_text;
}
