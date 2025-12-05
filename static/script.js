function validateSelection(editUrl) {
    // Pega o radio selecionado
    const selected = document.querySelector('input[name="selected"]:checked');

    if (!selected) {
        showAlert("Please select a student to edit.");
        // ou: alert("Please select a row before clicking Edit.");
        return false;
    }

    const studentId = selected.value;

    // Monta a URL: /edit?student_id=123
    const urlWithId = `${editUrl}?student_id=${encodeURIComponent(studentId)}`;

    window.location.href = urlWithId;
    return false; // impede o href="#" de disparar outra navegação
}

function showAlert(message) {
    document.getElementById("alertMessage").innerText = message;
    document.getElementById("customAlert").style.display = "flex";
}

function closeAlert() {
    document.getElementById("customAlert").style.display = "none";
}

function validateDelete(deleteUrl) {
    // verifica se algum registro foi selecionado
    const selected = document.querySelector('input[name="selected"]:checked');

    if (!selected) {
        showAlert("Please select a student to delete.");
        return false;
    }

    const studentId = selected.value;

    // Ensure before delete
    if (!confirm("Are you sure you want to delete this student?")) {
        return false;
    }

    // Build  Final URL  /delete?student_id=XX
    const finalUrl = `${deleteUrl}?student_id=${studentId}`;
    window.location.href = finalUrl;

    return false;
}