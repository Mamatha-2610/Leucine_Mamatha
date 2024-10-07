document.addEventListener("DOMContentLoaded", function() {
    const convertBtnEl = document.getElementById("convertBtn");

    convertBtnEl.addEventListener("click", function() {
        const hoursInputEl = parseInt(document.getElementById("hoursInput").value);
        const minutesInputEl = parseInt(document.getElementById("minutesInput").value);
        const errorMsgEl = document.getElementById("errorMsg");
        const timeInSecondsEl = document.getElementById("timeInSeconds");

        if (isNaN(hoursInputEl) || isNaN(minutesInputEl)) {
            errorMsgEl.textContent = "Please enter valid numbers for hours and minutes.";
            errorMsgEl.style.color = "#f7faf5";
            timeInSecondsEl.textContent = "";
        } else {
            errorMsgEl.textContent = "";
            timeInSecondsEl.textContent = ((hoursInputEl * 60) + minutesInputEl) * 60;
            timeInSecondsEl.style.color = "#ffffff";
        }
    });
});