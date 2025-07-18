document.getElementById("startMonitor").addEventListener("click", () => {
    const pin = document.getElementById("pinInput").value;
    
    if (pin === "3456") {
        alert(" Monitoring Enabled!");
        console.log("Monitoring started...");
    } else {
        alert(" Incorrect PIN! Access Denied.");
    }
});

document.getElementById("stopMonitor").addEventListener("click", () => {
    const pin = document.getElementById("pinInput").value;
    
    if (pin === "3456") {
        alert(" Monitoring Disabled!");
        console.log("Monitoring stopped...");
    } else {
        alert(" Incorrect PIN! Access Denied.");
    }
});
