function validateSelection(editUrl) {
    // Gets all checkboxes in the table
    const checkboxes = document.querySelectorAll("input[name='selected']");

    // Checks whether any checkbox is selected
    let hasSelection = false;
    checkboxes.forEach(cb => {
        if (cb.checked) hasSelection = true;
    });

    // If none is selected, displays an alert
    if (!hasSelection) {
        alert("Please select a row before clicking Edit.");
        return;
    }

    // If a selection exists, redirects to the edit route
    window.location.href = editUrl;
}

function showAlert(message) {
    document.getElementById("alertMessage").innerText = message;
    document.getElementById("customAlert").style.display = "flex";
}

function closeAlert() {
    document.getElementById("customAlert").style.display = "none";
}

function validateSelection(editUrl) {
    // pega o radio selecionado
    const selected = document.querySelector("input[name='selected']:checked");

    if (!selected) {
        // aqui você pode usar o seu custom alert se quiser
        alert("Please select a row before clicking Edit.");
        return;
    }

    // monta a URL: /edit?student_id=123
    const urlWithId = `${editUrl}?student_id=${selected.value}`;
    alert("Row before ." + urlWithId);

    window.location.href = urlWithId;
}
