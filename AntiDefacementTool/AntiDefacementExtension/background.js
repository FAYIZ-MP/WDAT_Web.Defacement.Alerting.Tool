console.log("🚀 Background script is running!");

// Check if scripting API is available
if (chrome.scripting) {
    chrome.action.onClicked.addListener((tab) => {
        console.log("🟢 Extension icon clicked. Injecting content.js...");

        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            files: ["content.js"]
        }).then(() => {
            console.log("📢 Injected content.js successfully!");
        }).catch((error) => {
            console.error("❌ Error injecting content.js:", error);
        });
    });
} else {
    console.error("❌ Error: chrome.scripting API is not available!");
}
