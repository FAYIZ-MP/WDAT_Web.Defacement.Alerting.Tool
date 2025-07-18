console.log("🚀 DefaceX Content Script Loaded!");

// Confirm Chrome APIs are available
if (typeof chrome !== "undefined" && chrome.runtime) {
    console.log("✅ Chrome runtime is available!");

    // Example: Log URL of the current page
    console.log("Current URL:", window.location.href);

    // 🚀 Send a test message to background.js
    chrome.runtime.sendMessage({ type: "test_message", message: "Hello from content.js!" }, (response) => {
        if (chrome.runtime.lastError) {
            console.error("❌ Message failed:", chrome.runtime.lastError.message);
        } else {
            console.log("📩 Message sent successfully! Response:", response);
        }
    });
} else {
    console.error("❌ Error: chrome.runtime is not available in this context.");
}
