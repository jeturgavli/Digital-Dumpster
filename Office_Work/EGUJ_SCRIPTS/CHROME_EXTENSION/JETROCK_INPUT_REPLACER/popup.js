document.getElementById("runBtn").addEventListener("click", async () => {
    const findText = document.getElementById("findText").value;
    const replaceText = document.getElementById("replaceText").value;

    if (!findText) {
        alert("Find text cannot be empty.");
        return;
    }

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            func: (findText, replaceText) => {
                document.querySelectorAll("input").forEach(i => {
                    if (i.value.includes(findText)) {
                        i.value = i.value.replaceAll(findText, replaceText);
                    }
                });
            },
            args: [findText, replaceText]
        });
    });
});
